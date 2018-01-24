# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import json
from scrapy import Item, Field

class ScheduleItem(Item):
    direction = Field()
    weekday = Field()
    offday = Field()

class scheduleItemSerializer(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ScheduleItem):
            return dict({'direction': o['direction'],
                         'weekday': o['weekday'],
                         'offday': o['offday']
                         })
        else:
            return json.JSONEncoder.default(self, o)


class StationItem(Item):
    name = Field()
    door_open = Field()
    schedule = Field()


class StationItemSerializer(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, StationItem):
            return dict({'name': o['name'],'door_open':o['door_open'], 'schedule':o['schedule']})
        else:
            return json.JSONEncoder.default(self, o)

class MetroItem(Item):
    name = Field()
    origin = Field()
    terminus = Field()
    total_station = Field()
    stations = Field(serializer=StationItem)






class CityItem(Item):
    name = Field()
    shortcut = Field()
    metros = Field()
