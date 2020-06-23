# -*- coding: utf-8 -*-
import peewee

db = peewee.SqliteDatabase('weather.db')


class BaseTable(peewee.Model):
    class Meta:
        database = db


class Weather(BaseTable):
    date = peewee.CharField()
    max_temperature = peewee.CharField()
    min_temperature = peewee.CharField()
    weather_type = peewee.CharField()


db.create_tables([Weather])
