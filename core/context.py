# coding=utf-8
from .models import Setup
from apps.city.models import City

__author__ = 'alexy'


def site_settings(request):
    query = Setup.objects.first()
    city_query = City.objects.all()
    return {
        'SITE_SETTINGS': query,
        'CITY_LIST': city_query
    }
