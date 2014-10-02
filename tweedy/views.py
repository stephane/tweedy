# -*- coding: utf-8 -*-
# Copyright (c) 2014 Stéphane Raimbault. All rights reserved.

from datetime import date

from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import redirect, render

from . import models
from . import forms

def yield_list(request):
    # Post to add a new yield
    if request.user.is_authenticated():
        if request.method == 'POST' and request.user:
            form = forms.YieldForm(request.POST)
            if form.is_valid():
                new_yield = form.save(commit=False)
                new_yield.by_user = request.user
                new_yield.save()
                return redirect('yield_list')
        else:
            form = forms.YieldForm(initial={'date': date.today().isoformat()})
    else:
        # No form for anonymous user
        form = None

    yields = models.Yield.objects.select_related('by_user').order_by('-date')[:10]
    ctxt = {
        'yields': yields,
        'form': form
    }
    return render(request, 'yield_list.html', ctxt)


def yield_json(request):
    yields = (models.Yield.objects.values('date')
              .annotate(total=Sum('quantity')).order_by('date'))
    yield_data = []
    for y in yields:
        yield_data.append({
            'date': y['date'].isoformat(),
            'total': y['total']
        })
    data = {
        'yields': yield_data
    }
    return JsonResponse(data)
