# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from sklearn.externals import joblib

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def index(request):
    return render(request, 'index.html')


def predict(request):
    model = joblib.load(BASE_DIR + '/static/bj_housing.pkl')
    client_data = []  # Client 3

    client_data.append(request.GET.get('area', '1'))
    client_data.append(request.GET.get('room', '1'))
    client_data.append(request.GET.get('living', '1'))

    is_school = request.GET.get('school', 'false')

    if is_school:
        is_school = 1
    else:
        is_school = 0

    client_data.append(is_school)

    client_data.append(request.GET.get('year', '1'))

    client_data.append(request.GET.get('floor', '1'))

    ans = format(int(model.predict(client_data) * 10000), ',')

    return HttpResponse(ans)
