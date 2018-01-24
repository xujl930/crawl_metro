# -*- coding:utf8 -*-
import re
import json
import scrapy
import datetime
import requests
import logging
from scrapy import Request, Spider, Selector
from metro_spider.items import *
from metro_spider.langconv import CONNECTOR, Converter
# from lxml import etree
# from scrapy.shell import inspect_response
# from metro_spider.stations import LINES, STATIONS
# from metro_spider.metro_spider.items import *

class MetroSpider(Spider):
    name = 'shanghai_metro'

    url = 'https://zh.wikipedia.org/wiki/上海轨道交通' # 从维基百科上获取地铁开门方向

    stations_schedule_url = 'http://m.shmetro.com/interface/metromap/metromap.aspx?func=fltime&line={}' # 获取指定地铁线路的所有站点时刻数据接口
    schedule_url = 'http://m.shmetro.com/interface/metromap/metromap.aspx?func=fltime&stat_id={}' # 获取指定站点时刻数据接口

    allowed_domain = ['https://zh.wikipedia.org', 'http://m.shmetro.com']

    @staticmethod
    def extract_by_xpath(parent, selector):
        return parent.xpath(selector).extract()

    def start_requests(self):
        yield Request(url=self.url, callback=self.parse_metro)

    def parse_metro(self, response):
        city = CityItem()
        city['name'] = '上海'
        city['shortcut'] = 'SHANG_HAI'
        yield city

        selector = Selector(response)
        # select = "//table[contains(@class,'wikitable') and contains(@log-set-param, 'table_view')]/tr"
        select = "table.wikitable.sortable tr"

        metros = selector.css(select)[1:-1]
        # metros = selector.css(select)[10:11]

        # array_metro = []
        sname = './th//a/text()'
        sorigin = './td[1]//text()'
        sterminus = './td[2]//text()'
        stotal = './td[5]//text()'

        for met in metros:
            metro = MetroItem()

            name = self.extract_by_xpath(met, sname)
            origin = self.extract_by_xpath(met, sorigin)
            terminus = self.extract_by_xpath(met, sterminus)
            total = self.extract_by_xpath(met, stotal)

            if not (name and origin and terminus and total):
                logging.warning('metro item {} not fulfilled'.format(name))
                return

            metro['name'] = Converter('zh-hans').convert(name[0])
            metro['origin'] = Converter('zh-hans').convert(''.join(origin).replace('[l]', ''))
            metro['terminus'] = Converter('zh-hans').convert(''.join(terminus))
            metro['total_station'] = int(total[0])

            request = Request(url =self.url + metro['name'], callback=self.parse_station, dont_filter=True)
            r = requests.get(self.stations_schedule_url.format(int(re.match('^(\d+)\w*', metro['name']).group(1)))) # 该地铁所有站点信息
            request.meta['metro'] = metro
            request.meta['r'] = r
            yield request
        # city['metros'] = array_metro
        # yield city

    def parse_station(self, response):
        metro = response.meta['metro']
        r = response.meta['r']
        selector = Selector(response)
        # inspect_response(response, self)
        select = "table.wikitable[width='100%'] > tr"
        rs = selector.css(select)[1:]
        stations = rs if rs else selector.css("table.wikitable[style*='width:100%'] > tr")[1:]

        sname = './td/a[1]/text()'  # 取第一个
        sdoor = './td[last()]/text()' # 双边开门 ['左/右侧(富锦路方向)', '\n左侧(莘庄方向)']
        array_station = list()
        idx = 0
        for stat in stations:
            station = StationItem()

            name = self.extract_by_xpath(stat, sname)
            door = self.extract_by_xpath(stat, sdoor)

            if not (name and door) or self.extract_by_xpath(stat, './td/i'):  # 过滤掉未开通的站点
                logging.warning('station item {} not fulfilled'.format(name))
                continue
            station['name'] = Converter('zh-hans').convert(name[0])
            station['door_open'] = ''.join(door).replace("\n", ",")

            array_sche = []
            try:
                # 从上海地铁官网抓取站点时刻表
                # r = requests.get(self.stations_schedule_url.format(int(metro['name'][0])))
                if r.status_code == 200:
                    sches = json.loads(r.text, encoding='utf-8')
                    for sche in sches:
                        if sche.get('name') == (Converter('zh-hans').convert(station['name'])):
                            sche_item = ScheduleItem()
                            sche_item['direction'] = sche.get('description')
                            # 首末班车时间
                            first_time = sche.get('first_time')
                            if sche.get('last_time_desc'):
                                last_time_desc = json.loads(sche.get('last_time_desc'))
                                time = self.get_last_time(sche.get('last_time'), last_time_desc)
                                last_time = time if time else sche.get('last_time')
                                sche_item['weekday'] = first_time + '/' + sche.get('last_time')
                                sche_item['offday'] = first_time + '/' + last_time
                            else:
                                sche_item['weekday'] = first_time + '/' + sche.get('last_time')
                                sche_item['offday'] = sche_item['weekday']
                            # array_sche.append(json.dumps(sche_item, cls=scheduleItemSerializer, ensure_ascii=False))
                            array_sche.append(dict(sche_item))
                        station['schedule'] = array_sche
            except Exception as e:
                logging.error('获取时刻信息出错', e)

            station['schedule'] = array_sche
            # array_station.append(json.dumps(station, cls=StationItemSerializer, ensure_ascii=False))
            array_station.append(dict(station))

        metro['stations'] = array_station
        # logging.debug(json.dumps(json.dumps(station, cls=StationItemSerializer), ensure_ascii=False))
        # logging.debug(json.dumps(array_station))
        yield metro

    """
    地铁末班车时间会依据具体日期做调整，爬虫目前只做最基本的周五，六时刻表
    """
    @staticmethod
    def get_last_time(last_time, last_time_desc):
        now = datetime.datetime.now()
        # 根据当前日期判断末班车是否延长
        weekday = last_time_desc.get('weekday')
        date_dajust = last_time_desc.get('dateday')

        hour = last_time.split(':')[0]
        hour = hour[1:] if hour.startswith('0') else hour

        minute = last_time.split(':')[1]
        minute = minute[1:] if minute.startswith('0') else minute

        last = now.replace(hour=int(hour), minute=int(minute))
        last_delay = last + datetime.timedelta(minutes=int(weekday[-1]))
        delta = last_delay.date() - last.date()

        if delta.days > 0:
            return '次日'+ str(last_delay.hour) +':'+str(last_delay.minute)
        else:
            return str(last_delay.hour) +':'+str(last_delay.minute)
