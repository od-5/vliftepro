from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'apps.page',
    url(r'^$', 'views.home_view', name='home'),
    url(r'^ticket/$', 'ajax.ticket', name='ticket'),
    url(r'^map/$', 'ajax.map', name='map'),
    url(r'^city$', 'ajax.city_xhr'),
    url(r'^format$', 'ajax.format_xhr'),
    url(r'^calculator$', 'ajax.calculator', name='calculator'),
    url(r'^(?P<slug>[\w-]+)/$', 'views.city_view', name='city'),
)