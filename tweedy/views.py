# -*- coding: utf-8 -*-
# Copyright (c) 2014 Stéphane Raimbault. All rights reserved.

from datetime import date
from django.contrib.auth.decorators import login_required
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

    yields = models.Yield.objects.order_by('date')
    ctxt = {
        'yields': yields,
        'form': form
    }
    return render(request, 'yield_list.html', ctxt)


def yield_json(request):
    yields = models.Yield.objects.all().order_by('date')
    data = {
        'yields': yields
    }
    return JsonResponse(data)
