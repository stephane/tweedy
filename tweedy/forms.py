# -*- coding: utf-8 -*-
# Copyright (c) 2014 Stéphane Raimbault. All rights reserved.

from django import forms
from django.forms import widgets

from . import models


class BootstrapModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BootstrapModelForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            # Excepted for checkboxes
            if not isinstance(field.widget, widgets.CheckboxSelectMultiple):
                field.widget.attrs['class'] = 'form-control'


class YieldForm(BootstrapModelForm):
    class Meta:
        model = models.Yield
        fields = ('date', 'quantity', 'chicken')
