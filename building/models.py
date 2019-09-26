# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.gis.db import models

class ConflictData(models.Model):
    geom = models.GeometryField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    event_id_n = models.BigIntegerField(blank=True, null=True)
    event_date = models.DateField(blank=True, null=True)
    year = models.BigIntegerField(blank=True, null=True)
    event_type = models.CharField(max_length=254, blank=True, null=True)
    actor1 = models.CharField(max_length=254, blank=True, null=True)
    inter1 = models.BigIntegerField(blank=True, null=True)
    interactio = models.BigIntegerField(blank=True, null=True)
    country = models.CharField(max_length=254, blank=True, null=True)
    admin1 = models.CharField(max_length=254, blank=True, null=True)
    admin2 = models.CharField(max_length=254, blank=True, null=True)
    admin3 = models.CharField(max_length=254, blank=True, null=True)
    location = models.CharField(max_length=254, blank=True, null=True)
    geo_precis = models.BigIntegerField(blank=True, null=True)
    source_sca = models.CharField(max_length=254, blank=True, null=True)
    notes = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Conflict_data'


class HealthFacilities(models.Model):
    geom = models.GeometryField(blank=True, null=True)
    objectid = models.BigIntegerField(blank=True, null=True)
    fid_1 = models.BigIntegerField(blank=True, null=True)
    unitid = models.CharField(max_length=254, blank=True, null=True)
    unittype = models.CharField(max_length=254, blank=True, null=True)
    unittypena = models.CharField(max_length=254, blank=True, null=True)
    lvlid = models.CharField(max_length=254, blank=True, null=True)
    region = models.CharField(max_length=254, blank=True, null=True)
    code = models.CharField(max_length=254, blank=True, null=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    comment = models.CharField(max_length=254, blank=True, null=True)
    code_1 = models.CharField(max_length=17, blank=True, null=True)
    name_1 = models.CharField(max_length=51, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Health_Facilities'



class Districtnew(models.Model):
    geom = models.GeometryField(blank=True, null=True)
    model = models.CharField(max_length=17, blank=True, null=True)
    district_n = models.CharField(max_length=29, blank=True, null=True)
    district = models.CharField(max_length=8, blank=True, null=True)
    fid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'districtnew'


class GisOsmRoadsFree1(models.Model):
    geom = models.GeometryField(blank=True, null=True)
    osm_id = models.CharField(max_length=10, blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)
    fclass = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    ref = models.CharField(max_length=20, blank=True, null=True)
    oneway = models.CharField(max_length=1, blank=True, null=True)
    maxspeed = models.IntegerField(blank=True, null=True)
    layer = models.BigIntegerField(blank=True, null=True)
    bridge = models.CharField(max_length=1, blank=True, null=True)
    tunnel = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis.osm_roads_free_1'


class Places(models.Model):
    geom = models.GeometryField(blank=True, null=True)
    osm_id = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=48, blank=True, null=True)
    type = models.CharField(max_length=16, blank=True, null=True)
    population = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'places'


class PoliceStation(models.Model):
    id = models.CharField(primary_key=True, max_length=250)
    geom = models.GeometryField(blank=True, null=True)
    categories = models.CharField(max_length=250, blank=True, null=True)
    location_city = models.CharField(db_column='location.city', max_length=250, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    location_lat = models.FloatField(db_column='location.lat', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    location_lng = models.FloatField(db_column='location.lng', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    location_state = models.CharField(db_column='location.state', max_length=250, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    name = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Police Station'


class CollegeAcademicBuilding(models.Model):
    id = models.CharField(primary_key=True, max_length=250)
    geom = models.GeometryField(blank=True, null=True)
    categories = models.CharField(max_length=250, blank=True, null=True)
    location_city = models.CharField(db_column='location.city', max_length=250, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    location_lat = models.FloatField(db_column='location.lat', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    location_lng = models.FloatField(db_column='location.lng', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    location_state = models.CharField(db_column='location.state', max_length=250, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    name = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'College Academic Building'


class FireStation(models.Model):
    id = models.CharField(primary_key=True, max_length=1)
    geom = models.GeometryField(blank=True, null=True)
    categories = models.CharField(max_length=100, blank=True, null=True)
    location_city = models.CharField(db_column='location.city', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    location_lat = models.FloatField(db_column='location.lat', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    location_lng = models.FloatField(db_column='location.lng', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    location_state = models.CharField(db_column='location.state', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Fire Station'


class GamaDistrict(models.Model):
    geom = models.GeometryField(blank=True, null=True)
    region = models.CharField(max_length=254, blank=True, null=True)
    district = models.CharField(max_length=254, blank=True, null=True)
    dist_code = models.CharField(max_length=254, blank=True, null=True)
    area_km = models.FloatField(blank=True, null=True)
    shape_star = models.FloatField(blank=True, null=True)
    shape_stle = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    safety = models.CharField(max_length=200, blank=True, null=True)
    amenities = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'GAMA_District'