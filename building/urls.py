from django.urls import path
from . import views
from djgeojson.views import GeoJSONLayerView

app_name = 'building'

urlpatterns = [
    path('', views.home, name='home'),
    path('conflict', views.conflictLayer.as_view(), name='conflict'),
    path('health', views.healthLayer.as_view(), name='health'),
    path('district', views.districtLayer.as_view(), name='district'),
    path('places', views.placesLayer.as_view(), name='places'),
    path('roads', views.roadsLayer.as_view(), name='roads'),
    path('school', views.schoolLayer.as_view(), name='school'),
    path('police', views.policestationsLayer.as_view(), name='police'),
    path('fire', views.FireStationLayer.as_view(), name='fire'),
    path('gama', views.GamaDistrictLayer.as_view(), name='gama'),
]
