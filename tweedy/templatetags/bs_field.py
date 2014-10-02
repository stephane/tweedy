# -*- coding: utf-8 -*-
# Copyright (c) 2011-2014 Polyconseil SAS. All rights reserved.

from __future__ import unicode_literals

from django import template
from django.forms.fields import DateField
from django.template.loader import render_to_string

register = template.Library()


@register.filter(name='bs_field')
def bs_field(field, cols=None):
    if cols:
        label_col, value_col = cols.split(',')
    else:
        label_col = 'col-sm-2'
        value_col = 'col-sm-6'

    if isinstance(field.field, DateField):
        # Force HTML5 date
        field.field.widget.input_type = 'date'

    return render_to_string(
        'bs_field/field.html',
        {'field': field, 'label_col': label_col, 'value_col': value_col, 'required': False})
