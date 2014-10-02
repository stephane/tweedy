# -*- coding: utf-8 -*-
# Copyright (c) 2014 Stéphane Raimbault. All rights reserved.

from __future__ import division

from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User


class Chicken(models.Model):
    name = models.CharField(max_length=64)
    begin = models.DateField(u"Date de début")
    end = models.DateField(u"Date de fin", blank=True, null=True)

    class Meta:
        db_table = 'chicken'
        verbose_name = u"Chicken"

    def __unicode__(self):
        return self.name


class Yield(models.Model):
    date = models.DateField(u"Date")
    quantity = models.PositiveIntegerField(u"Quantité")
    chicken = models.ForeignKey(Chicken, verbose_name=u"Poule", blank=True, null=True)
    by_user = models.ForeignKey(User)

    class Meta:
        db_table = 'yield'
        verbose_name = u"Production"
        unique_together = (('date', 'chicken'),)

    def __unicode__(self):
        return "%s : %s œuf%s" % (
            self.date, self.quantity, u"s" if self.quantity > 1 else u"")
