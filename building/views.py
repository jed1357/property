# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# from django.contrib.auth.decorators import login_required
from djgeojson.views import GeoJSONLayerView
import json,ast
# import ee
# from ee.ee_exception import EEException
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import *
from django.core.serializers import serialize



def home(request):
	

	return render(request, 'templates/base.html')


class conflictLayer(GeoJSONLayerView):
	# Options
	model = ConflictData
	precision = 3   
	simplify = 0.001
	properties = ('conflicts')


class healthLayer(GeoJSONLayerView):
	# Options
	model = HealthFacilities
	precision = 3   
	simplify = 0.001
	properties = ('name')



class districtLayer(GeoJSONLayerView):
	# Options
	model = Districtnew
	precision = 3   
	simplify = 0.001
	properties = ('district_n')



class roadsLayer(GeoJSONLayerView):
	# Options
	model = GisOsmRoadsFree1
	precision = 3   
	simplify = 0.001
	properties = ('name')


class policestationsLayer(GeoJSONLayerView):
	# Options
	model = PoliceStation
	precision = 3   
	simplify = 0.001
	properties = ('name')



class placesLayer(GeoJSONLayerView):
	# Options
	model = Places
	precision = 3   
	simplify = 0.001
	properties = ('name')



class schoolLayer(GeoJSONLayerView):
	# Options
	model = CollegeAcademicBuilding
	precision = 3   
	simplify = 0.001
	properties = ('name')


class FireStationLayer(GeoJSONLayerView):
	# Options
	model = FireStation
	precision = 3   
	simplify = 0.001
	properties = ('name')




class GamaDistrictLayer(GeoJSONLayerView):
	# Options
	model = GamaDistrict
	precision = 3   
	simplify = 0.001
	properties = ('region', 'district', 'safety', 'amenities')