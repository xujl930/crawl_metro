# -*- coding:utf8 -*-
import json
from mongoengine import *
from app import db

class Schedule(EmbeddedDocument):
    direction = StringField(max_length=15)
    weekday = StringField()
    offday = StringField()


class Staion(EmbeddedDocument):
    name = StringField(max_length=15),
    door_open = StringField(max_length=40)
    schedule = EmbeddedDocumentListField(Schedule)


class Metro(Document):
    name = StringField(max_length=30, required=True, unique=True)
    origin = StringField(max_length=30)
    terminus = StringField(max_length=30)
    total_station = IntField()
    stations = EmbeddedDocumentListField(Staion)

    def as_json(self):
        return {
            'name': self.name,
            'origin': self.origin,
            'terminus': self.terminus,
            'total_station': self.total_station
        }


class City(Document):
    name = StringField(max_length=25, required=True, unique=True)
    shortcut = StringField(max_length=15, unique=True)
    # metros = EmbeddedDocumentListField(Metro)
    metros = ListField(ObjectIdField(db_field='Metro', unique=True))

    def as_json(self):
        return {
            'name':self.name,
            'shortcut':self.shortcut}
