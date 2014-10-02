# -*- coding: utf-8 -*-
# Copyright (c) 2014 Stéphane Raimbault. All rights reserved.

from django.contrib import admin

from . import models


admin.site.register(models.Chicken)
admin.site.register(models.Yield)


