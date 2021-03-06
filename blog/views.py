﻿# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from blog.models import city, region, cityAir, cityPM, regionPM
from django.template import loader, Context
from django.shortcuts import render_to_response
from django import forms
import urllib2
import json


class UserForm(forms.Form):
    name = forms.CharField()


def reg(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            print form.cleaned_data
            return HttpResponse('OK')
    else:
        form = UserForm()  # default
    return render_to_response('register.html', {'form': form})




def hello(request):
    return render_to_response('data_visual_test.html')


def current_url_view_good(request):
    return HttpResponse("Welcome to the page  host: %s " % request.get_host())


def getCities(request):
    # city and quality may be null


    # Filter to choose the specific cities.
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            #print form.cleaned_data
            inputValue = form.cleaned_data['name']
            # filter: return the values which matches the scheme.
            searchResult = regionPM.objects.filter(city=inputValue)
            return render_to_response('result.html', {'inputValue': inputValue, 'searchResult': searchResult})
        # return HttpResponse(searchResult[1])
    else:
        form = UserForm()

    regionDisplay = regionPM.objects.all()
    return render_to_response('select.html', {'regionPMDisplay': regionDisplay, 'form': form})


def index(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            inputValue = form.cleaned_data['name']
            searchResult = regionPM.objects.filter(city=inputValue)
            return render_to_response('result.html',
                                      {'inputValue': inputValue, 'form': form, 'searchResult': searchResult})
    else:
        form = UserForm()

    regionDisplay = regionPM.objects.all()
    r = list()
    r.append(regionDisplay[0])
    for i in range(1, len(regionDisplay) - 1):
        r.append(regionDisplay[i])

    return render_to_response('select.html', {'regionPMDisplay': r, 'form': form})



def indexcity(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            inputValue = form.cleaned_data['name']
            searchResult = cityPM.objects.filter(city=inputValue)
            return render_to_response('cityResult.html',
                                      {'inputValue': inputValue, 'form': form, 'searchResult': searchResult})
    else:
        form = UserForm()

    cityPMDisplay = cityPM.objects.all()
    r = list()
    r.append(cityPMDisplay[0])
    for i in range(1, len(cityPMDisplay) - 1):
        r.append(cityPMDisplay[i])

    return render_to_response('citypm.html', {'cityPMDisplay': r, 'form': form})



def first_page(request):
    return render_to_response('index_bootstrap.html')


# initialize the database which represents the variables of the city
def initialize_database(request):
    url = ('http://www.pm25.in/api/querys/all_cities.json?token=')
    content = urllib2.urlopen(url).read()
    data = json.loads(content)
    l = list()
    l.append(data[0]['area'])
    for i in range(1, len(data) - 1):
        if data[i]['area'] != data[i - 1]['area']:
            l.append(data[i]['area'])  # 拿到城市的列表

    l2 = list(set(l))

    # Save city 数据库
    for j in range(0, len(l2) - 1):
        city2 = city(name=l2[j])
        city2.save()

    # Save Region city 数据库
    for i in range(0, len(data) - 1):
        region2 = region(name=data[i]['area'], area=data[i]['position_name'])
        region2.save()
    return HttpResponse('initialize_database: OK!')


def top_30_city(request):
    top_30_city = cityPM.objects.order_by('pm2_5','aqi')[:30]
    top_city_list = list(top_30_city)
    return render_to_response('billboard.html', {'cityPMDisplay': top_city_list})

def worst_30_city(request):
    worst_30_city = cityPM.objects.order_by('-pm2_5','-aqi')[:30]
    worst_city_list = list(worst_30_city)
    return render_to_response('billboard.html', {'cityPMDisplay': worst_city_list})

def PM2_5_visualization(request):
    return render_to_response('PM2_5_visualization.html')

def china_map_histogram(request):
    return render_to_response('footprint-china.html')


# Ref: 
# 1. 一次更新多个对象:http://docs.oneele.com/django/topics/db/queries.html#topics-db-queries-update




