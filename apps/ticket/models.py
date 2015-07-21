# coding=utf-8
from django.db import models

__author__ = 'alexy'


class Ticket(models.Model):

    class Meta:
        verbose_name = u'Заявка'
        verbose_name_plural = u'Заявки'
        app_label = 'ticket'

    def __unicode__(self):
        return self.name

    def performed_at(self):
        pass

    TICKET_STATUS_CHOICE = (
        (0, u'В обработке'),
        (1, u'Новая заявка'),
        (2, u'Отклонена'),
        (3, u'Нет ответа'),
    )

    SALE_STATUS_CHOICE = (
        (0, u'Ожидание оплаты'),
        (1, u'Уточнение деталей'),
        (2, u'Оплачено'),
    )

    name = models.CharField(verbose_name=u'Имя', max_length=256)
    phone = models.EmailField(verbose_name=u'Телефон', max_length=256)
    sale = models.BooleanField(verbose_name=u'Продажа', default=False)
    text = models.TextField(verbose_name=u'Дополнительная информация', blank=True, null=True)
    ticket_status = models.PositiveSmallIntegerField(verbose_name=u'Статус заявки',  choices=TICKET_STATUS_CHOICE, default=0, blank=True, null=True)
    ticket_comment = models.TextField(verbose_name=u'Комментарий', blank=True, null=True)

    sale_status = models.PositiveSmallIntegerField(verbose_name=u'Статус продажи', choices=SALE_STATUS_CHOICE, default=0, blank=True, null=True)
    sale_comment = models.TextField(verbose_name=u'Комментарий', blank=True, null=True)
    created = models.DateField(verbose_name=u'Дата создания', auto_now=True)