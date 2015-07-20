# coding=utf-8
from django.conf import settings
from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import SmartResize
from pytils.translit import slugify
from apps.page.common import get_slider_path
import geotagging as api

__author__ = 'alexy'

api_key = settings.YANDEX_MAPS_API_KEY


class City(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'Город')
    lift = models.DecimalField(max_digits=5, decimal_places=0, verbose_name=u'Кол-во лифтов')
    slug = models.SlugField(max_length=100, verbose_name=u'url', blank=True)

    def __unicode__(self):
        return self.name

    def save(self):
      self.slug = slugify(self.name)
      super(City, self).save()

    class Meta:
        verbose_name = u'Город'
        verbose_name_plural = u'Города'


class Address(models.Model):
    city = models.ForeignKey(City, verbose_name=u'Город')
    name = models.CharField(max_length=100, blank=True, verbose_name=u'Здание')
    address = models.CharField(max_length=100, verbose_name=u'Адрес')
    coord_x = models.DecimalField(max_digits=8, decimal_places=6, blank=True, null=True, editable=True, verbose_name=u'Ширина')
    coord_y = models.DecimalField(max_digits=8, decimal_places=6, blank=True, null=True, editable=True, verbose_name=u'Долгота')

    def __unicode__(self):
        return u'%s %s' % (self.city, self.address)

    def save(self, *args, **kwargs):
        super(Address, self).save()
        pos = api.geocode(api_key, self)
        self.coord_x = float(pos[0])
        self.coord_y = float(pos[1])
        super(Address, self).save()

    class Meta:
        verbose_name = u'Адрес'
        verbose_name_plural = u'Адреса'


class Format(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'Формат')
    price = models.DecimalField(max_digits=6, decimal_places=0, verbose_name=u'Цена')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Цены и форматы'
        verbose_name_plural = u'Цены и форматы'


class Article(models.Model):
    city = models.ForeignKey(to=City, verbose_name=u'Город')
    text = models.TextField(verbose_name=u'Текст')

    def __unicode__(self):
        return self.city.name

    class Meta:
        verbose_name = u'Текст'
        verbose_name_plural = u'Текста'


class Slider(models.Model):
    class Meta:
        verbose_name = u'Слайд'
        verbose_name_plural = u'Слайды'

    def __unicode__(self):
        return u'%s г.%s' % (self.name, self.city.name)

    city = models.ForeignKey(to=City, verbose_name=u'Город')
    name = models.CharField(verbose_name=u'Здание', max_length=255)
    image = models.ImageField(verbose_name=u'Изображение', upload_to=get_slider_path)
    image_resize = ImageSpecField(
        [SmartResize(*settings.CITY_SLIDER_SIZE)], source='image', format='JPEG', options={'quality': 94}
    )


class CitySlider(models.Model):
    class Meta:
        verbose_name = u'Бизнес центр'
        verbose_name_plural = u'Бизнес центры'

    def __unicode__(self):
        return self.name

    city = models.ForeignKey(to=City, verbose_name=u'Город')
    name = models.CharField(verbose_name=u'Название и адрес объекта', max_length=255)
    type = models.CharField(verbose_name=u'Класс', max_length=255, blank=True, null=True)
    lift = models.IntegerField(verbose_name=u'Количество лифтов', blank=True, null=True, default=1)
    floor = models.IntegerField(verbose_name=u'Количество этажей', blank=True, null=True, default=1)
    maneuverability = models.IntegerField(verbose_name=u'Примерная проходимость ежедневно', blank=True, null=True, default=1)
    image = models.ImageField(verbose_name=u'Изображение', upload_to=get_slider_path)