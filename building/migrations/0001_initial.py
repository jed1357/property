# Generated by Django 2.2.5 on 2019-09-27 22:34

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CollegeAcademicBuilding',
            fields=[
                ('id', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('geom', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326)),
                ('categories', models.CharField(blank=True, max_length=250, null=True)),
                ('location_city', models.CharField(blank=True, db_column='location.city', max_length=250, null=True)),
                ('location_lat', models.FloatField(blank=True, db_column='location.lat', null=True)),
                ('location_lng', models.FloatField(blank=True, db_column='location.lng', null=True)),
                ('location_state', models.CharField(blank=True, db_column='location.state', max_length=250, null=True)),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'db_table': 'College Academic Building',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ConflictData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('event_id_n', models.BigIntegerField(blank=True, null=True)),
                ('event_date', models.DateField(blank=True, null=True)),
                ('year', models.BigIntegerField(blank=True, null=True)),
                ('event_type', models.CharField(blank=True, max_length=254, null=True)),
                ('actor1', models.CharField(blank=True, max_length=254, null=True)),
                ('inter1', models.BigIntegerField(blank=True, null=True)),
                ('interactio', models.BigIntegerField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=254, null=True)),
                ('admin1', models.CharField(blank=True, max_length=254, null=True)),
                ('admin2', models.CharField(blank=True, max_length=254, null=True)),
                ('admin3', models.CharField(blank=True, max_length=254, null=True)),
                ('location', models.CharField(blank=True, max_length=254, null=True)),
                ('geo_precis', models.BigIntegerField(blank=True, null=True)),
                ('source_sca', models.CharField(blank=True, max_length=254, null=True)),
                ('notes', models.CharField(blank=True, max_length=254, null=True)),
            ],
            options={
                'db_table': 'Conflict_data',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Districtnew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326)),
                ('model', models.CharField(blank=True, max_length=17, null=True)),
                ('district_n', models.CharField(blank=True, max_length=29, null=True)),
                ('district', models.CharField(blank=True, max_length=8, null=True)),
                ('fid', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'districtnew',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FireStation',
            fields=[
                ('id', models.CharField(max_length=1, primary_key=True, serialize=False)),
                ('geom', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326)),
                ('categories', models.CharField(blank=True, max_length=100, null=True)),
                ('location_city', models.CharField(blank=True, db_column='location.city', max_length=100, null=True)),
                ('location_lat', models.FloatField(blank=True, db_column='location.lat', null=True)),
                ('location_lng', models.FloatField(blank=True, db_column='location.lng', null=True)),
                ('location_state', models.CharField(blank=True, db_column='location.state', max_length=100, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'Fire Station',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GamaDistrict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326)),
                ('region', models.CharField(blank=True, max_length=254, null=True)),
                ('district', models.CharField(blank=True, max_length=254, null=True)),
                ('dist_code', models.CharField(blank=True, max_length=254, null=True)),
                ('area_km', models.FloatField(blank=True, null=True)),
                ('shape_star', models.FloatField(blank=True, null=True)),
                ('shape_stle', models.FloatField(blank=True, null=True)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('long', models.FloatField(blank=True, null=True)),
                ('safety', models.CharField(blank=True, max_length=200, null=True)),
                ('amenities', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'GAMA_District',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GisOsmRoadsFree1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326)),
                ('osm_id', models.CharField(blank=True, max_length=10, null=True)),
                ('code', models.IntegerField(blank=True, null=True)),
                ('fclass', models.CharField(blank=True, max_length=20, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('ref', models.CharField(blank=True, max_length=20, null=True)),
                ('oneway', models.CharField(blank=True, max_length=1, null=True)),
                ('maxspeed', models.IntegerField(blank=True, null=True)),
                ('layer', models.BigIntegerField(blank=True, null=True)),
                ('bridge', models.CharField(blank=True, max_length=1, null=True)),
                ('tunnel', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'gis.osm_roads_free_1',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HealthFacilities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326)),
                ('objectid', models.BigIntegerField(blank=True, null=True)),
                ('fid_1', models.BigIntegerField(blank=True, null=True)),
                ('unitid', models.CharField(blank=True, max_length=254, null=True)),
                ('unittype', models.CharField(blank=True, max_length=254, null=True)),
                ('unittypena', models.CharField(blank=True, max_length=254, null=True)),
                ('lvlid', models.CharField(blank=True, max_length=254, null=True)),
                ('region', models.CharField(blank=True, max_length=254, null=True)),
                ('code', models.CharField(blank=True, max_length=254, null=True)),
                ('name', models.CharField(blank=True, max_length=254, null=True)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('long', models.FloatField(blank=True, null=True)),
                ('comment', models.CharField(blank=True, max_length=254, null=True)),
                ('code_1', models.CharField(blank=True, max_length=17, null=True)),
                ('name_1', models.CharField(blank=True, max_length=51, null=True)),
            ],
            options={
                'db_table': 'Health_Facilities',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326)),
                ('osm_id', models.BigIntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=48, null=True)),
                ('type', models.CharField(blank=True, max_length=16, null=True)),
                ('population', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'places',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PoliceStation',
            fields=[
                ('id', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('geom', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326)),
                ('categories', models.CharField(blank=True, max_length=250, null=True)),
                ('location_city', models.CharField(blank=True, db_column='location.city', max_length=250, null=True)),
                ('location_lat', models.FloatField(blank=True, db_column='location.lat', null=True)),
                ('location_lng', models.FloatField(blank=True, db_column='location.lng', null=True)),
                ('location_state', models.CharField(blank=True, db_column='location.state', max_length=250, null=True)),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'db_table': 'Police Station',
                'managed': False,
            },
        ),
    ]
