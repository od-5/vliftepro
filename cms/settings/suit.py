# coding=utf-8
__author__ = 'alexy'


SUIT_CONFIG = {
    'ADMIN_NAME': u'Сафари',
    'HEADER_DATE_FORMAT': 'l, j. F Y',
    'HEADER_TIME_FORMAT': 'H:i',
    'MENU_EXCLUDE': ('auth.group',),
    'MENU': (
        'sites',
        {'label': u'Перейти на сайт', 'url': 'home'},
        {'label': u'Настройки', 'icon': 'icon-cog', 'models': ('auth.user', 'auth.group', 'core.setup', )},
        {'label': u'Города и адреса', 'icon': 'icon-cog', 'models': ('city.city', 'city.address')},
        {'label': u'Цены и форматы', 'icon': 'icon-cog', 'models': ('city.format',)},
        {'label': u'Акции', 'icon': 'icon-cog', 'models': ('city.article',)},
        {'label': u'Слайдер', 'icon': 'icon-cog', 'models': ('city.slider',)},
    ),
}
