# coding=utf-8
from django.db import models

__author__ = 'alexy'


class Setup(models.Model):
    title = models.CharField(verbose_name=u'Заголовок <TITLE>...</TITLE>', max_length=256, blank=True)
    phone = models.CharField(verbose_name=u'Телефон', max_length=256, blank=True, null=True)
    email = models.EmailField(verbose_name=u'e-mail для приёма заявок', blank=True)
    video = models.TextField(verbose_name=u'HTML-код видео', blank=True, null=True)
    meta_key = models.TextField(verbose_name=u'Ключевые слова META_KEYWORDS', blank=True)
    meta_desc = models.TextField(verbose_name=u'Описание META_DESCRIPTION', blank=True)
    top_js = models.TextField(verbose_name=u'Скрипты в <HEAD>..</HEAD>', blank=True)
    bottom_js = models.TextField(verbose_name=u'Скрипты перед закрывающим </BODY>', blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'Настройки сайта'
        verbose_name_plural = u'Настройки сайта'
