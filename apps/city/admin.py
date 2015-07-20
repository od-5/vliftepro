# coding=utf-8
from django.contrib import admin
from .models import City, Address, Format, Article, Slider, CitySlider

__author__ = 'alexey'


class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'lift')
    readonly_fields = ['slug',]


class AddressAdmin(admin.ModelAdmin):
    list_display = ('address', 'name', 'city')
    list_filter = ('city',)


class FormatAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('city', 'text')
    list_filter = ('city',)


class SliderAdmin(admin.ModelAdmin):
    list_display = ('city', 'name', 'preview')
    list_filter = ('city',)

    def preview(self, img):
        return "<img src='%s' />" % img.image_resize.url
    preview.short_description = u"Превью"
    preview.allow_tags = True


class CitySliderAdmin(admin.ModelAdmin):
    list_display = ('city', 'name', 'preview')
    list_filter = ('city',)

    def preview(self, img):
        return "<img src='%s' style='width: 300px;' />" % img.image.url
    preview.short_description = u"Превью"
    preview.allow_tags = True


admin.site.register(City, CityAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Format, FormatAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(CitySlider, CitySliderAdmin)