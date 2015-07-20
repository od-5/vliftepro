# coding=utf-8
from django import forms
from apps.city.models import City, Format

__author__ = 'alexy'


class TicketForm(forms.Form):

    name = forms.CharField(
        max_length=100,
        label=u'Имя',
        widget=forms.TextInput(
            attrs={
                'placeholder': u'Как вас зовут?',
                'class': 'nm'
            }
        )
    )
    phone = forms.CharField(
        max_length=100,
        label=u'Телефон',
        widget=forms.TextInput(
            attrs={
                'placeholder': u'Ваш номер телефона?',
                'class': 'tele'
            }
        )
    )



class CalculatorForm(forms.Form):

    # DEFAULT_CHOICE = ((u'--------', u'--------'),)
    # try:
    #     CITY_CHOICES = DEFAULT_CHOICE + tuple([(i.name, i.name) for i in City.objects.all()])
    # except:
    #     CITY_CHOICES = DEFAULT_CHOICE
    # try:
    #     FORMAT_CHOICES = DEFAULT_CHOICE + tuple([(i.name, i.name) for i in Format.objects.all()])
    # except:
    #     FORMAT_CHOICES = DEFAULT_CHOICE

    lift = forms.DecimalField(max_digits=5, decimal_places=0, required=False)
    # city = forms.ChoiceField(choices=CITY_CHOICES, required=False)
    city = forms.ModelChoiceField(City.objects.all(), required=False)
    # format = forms.ChoiceField(choices=FORMAT_CHOICES, required=False)
    format = forms.ModelChoiceField(Format.objects.all(), required=False)
    price = forms.DecimalField(max_digits=5, decimal_places=0, required=False)
    sum = forms.DecimalField(max_digits=10, decimal_places=0, required=False)