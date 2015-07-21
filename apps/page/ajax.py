# coding=utf-8
from django.conf import settings
from django.core.mail import send_mail
from django.forms.formsets import formset_factory
from django.http import HttpResponseRedirect

from django.views.decorators.csrf import csrf_exempt
from apps.city.models import Address, City, Format
from apps.ticket.models import Ticket
from .forms import TicketForm, CalculatorForm
from apps.page.common import render_to_json
from core.models import Setup

__author__ = 'alexy'

@csrf_exempt
@render_to_json
def ticket(request):
    try:
        mail = Setup.objects.first().email
    except:
        mail = False
    if mail:
        recepient = mail
    else:
        recepient = 'direktor@vlifte.pro'

    form = TicketForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['name']
        phone = form.cleaned_data['phone']
        ticket = Ticket(name=name, phone=phone, text = u'')
        ticket.save()

        send_mail(
            u'vlifte.pro - Заявка с сайта',
            u'Имя: %s\nТелефон: %s\n' % (name, phone),
            settings.DEFAULT_FROM_EMAIL,
            [recepient, ]
        )
        return {'success': 'Сообщение успешно отправлено!'}
    else:
        return {'error': 'Сообщение не может быть отправлено!'}

@render_to_json
def map(request):
    # request.encoding = 'utf-8'
    # if request.is_ajax():
    #     query = City.objects.all()
    #     result = []
    #     for item in query:
    #         result_json = {}
    #         result_json['name'] = item.name
    #         result.append(result_json)
    #     data = simplejson.dumps(result)
    # else:
    #     data = 'fail'
    # return HttpResponse(data)
    request.encoding = 'utf-8'
    if request.is_ajax():
        query = Address.objects.all()
        result = []
        for item in query:
            result_json = {}
            result_json['name'] = item.name
            result_json['address'] = item.address
            result_json['coord_x'] = float(item.coord_x)
            result_json['coord_y'] = float(item.coord_y)
            result.append(result_json)
        data = result
    else:
        data = {'msg': 'fail'}
    return data


def calculator(request):
    try:
        mail = Setup.objects.first().email
    except:
        mail = False
    if mail:
        recepient = mail
    else:
        recepient = 'direktor@vlifte.pro'
    CalcFormSet = formset_factory(CalculatorForm)
    if request.method == "POST":
        form = TicketForm(request.POST)
        calc_formset = CalcFormSet(data=request.POST)
        if calc_formset.is_valid() and form.is_valid():
            cd = calc_formset.cleaned_data
            cd_form = form.cleaned_data
            text_name = u'Заявка: \nИмя: %s\nТелефон: %s\n' % (cd_form['name'], cd_form['phone'])
            text_form = ''
            # print cd


            for i in cd:
                # text_form = text_form + i['city'].name + ': ' + i['format'].name + '\n'
                if i:
                    text_form = text_form + i['city'].name + ': ' + i['format'].name + '\n'
            text = text_name + text_form

            ticket = Ticket(name=cd_form['name'], phone=cd_form['phone'], text = text)
            ticket.save()

            send_mail(
                u'vlifte.pro - Заказ рекламы с сайта',
                text,
                settings.DEFAULT_FROM_EMAIL,
                [recepient, ]
            )
            return HttpResponseRedirect('/')
    else:
        calc_formset = CalcFormSet()
        form = TicketForm()
    return HttpResponseRedirect('/')


@render_to_json
def city_xhr(request):
    request.encoding = 'utf-8'
    if request.is_ajax():
        xhr_value = request.GET['name']
        query = City.objects.get(id=xhr_value)
        lift = int(query.lift)
        city_dict = {'lift': lift}
        return city_dict
    else:
        return {'error': 'fail'}


@render_to_json
def format_xhr(request):
    request.encoding = 'utf-8'
    if request.is_ajax():
        xhr_value = request.GET['name']
        query = Format.objects.get(id=int(xhr_value))
        price = int(query.price)
        format_dict = {'price': price}
        return format_dict
    else:
        return {'error': 'fail'}