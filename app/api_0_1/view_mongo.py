# -*- coding:utf8 -*-
from flask import request, jsonify

from app import db
from app.model.models import *
from . import api

@api.route('/')
def get_city():
    city = City.objects[:1]
    print(city)
    return city.as_json()

@api.route('/city', methods=['GET', 'POST'])
def op_city():
    if request.method == 'GET':
        start = request.args.get('start', 1)
        limit = request.args.get('limit', 10)
        if not start or not limit:
            start = 1
            limit = 10
        start = int(start) if int(start) >= 1 else 1
        limit = int(limit) if int(limit) >= 0 else 10

        print(start, limit)
        citys = City.objects[start-1:start+limit-1]
        print(citys)
        return jsonify([c.as_json() for c in citys])

    if request.method == 'POST':
        name = request.json.get('name')
        shortcut = request.json.get('shortcut')
        c = City(name=name, shortcut=shortcut, metros=[])
        #m = Metro.objects()
        try:
            c.save()
        except Exception as e:
            return jsonify({'error':str(e)})
        return jsonify({'status':'saved'})


@api.route('/hefei')
def hf():
    metro = Metro(name='合肥地铁1号线', direction='合肥火车站-九联圩站',total_station=23)
    metro.save()
    city = City.objects(name='合肥')[0]
    print(city.as_json())
    print(city.id)
    if not city:
        return 'null city'
    # city.update(push__stations__S = metro)
    city.update(push__metros=metro.id)
    return 'ok'