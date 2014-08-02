# -*- coding: utf-8 -*-

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
		form = UserForm() #default
	return render_to_response('register.html',{'form':form})

# Create your views here.


def hello(request):
	return HttpResponse("Hello World!")

def current_url_view_good(request):
    return HttpResponse("Welcome to the page  host: %s " % request.get_host())


def getCities(request):
	# city and quality may be null

	
	# API 填写处:'xxxxxxxxxxxx'
	url = ('http://www.pm25.in/api/querys/all_cities.json?token=xxxxxxxxxxxx')
	content = urllib2.urlopen(url).read()
	data = json.loads(content)
	l = list()
	l.append(data[0]['area'])
	for i in range(1,len(data)-1):
		if data[i]['area'] != data[i-1]['area']:
			l.append(data[i]['area'])  # 拿到城市的列表

	l2 = list(set(l))
	
	for  j in range(0,len(l2)-1):
		city2 = city(name = l2[j])
		city2.save()


	for i in range(0,len(data)-1):
		region2 = region(name = data[i]['area'], area = data[i]['position_name'])
		region2.save()

	for i in range(0,len(data)-1):
		cityAir2 = cityAir(name = data[i]['area'], CO = data[i]['co'], NO2 = data[i]['no2'], O3 = data[i]['o3'], SO2 = data[i]['so2'])
		cityAir2.save()

	for i in range(0,len(data)-1):
		regionPM2 = regionPM(city = data[i]['area'], area = data[i]['position_name'], aqi = data[i]['aqi'], quality = data[i]['quality'], pm2_5 = data[i]['pm2_5'], pm10 = data[i]['pm10'])
		regionPM2.save()

	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			#print form.cleaned_data
			inputValue = form.cleaned_data['name']
			searchResult = regionPM.objects.filter(city = inputValue)
			return render_to_response('result.html', {'inputValue': inputValue, 'searchResult':searchResult})
			# return HttpResponse(searchResult[1])
	else:
		form = UserForm() 


	regionDisplay = regionPM.objects.all()
	return render_to_response('select.html', {'regionPMDisplay': regionDisplay, 'form':form})


def index(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			inputValue = form.cleaned_data['name']
			searchResult = regionPM.objects.filter(city = inputValue)
			return render_to_response('result.html', {'inputValue': inputValue, 'form':form, 'searchResult':searchResult})
	else:
		form = UserForm() 


	regionDisplay = regionPM.objects.all()
	r = list()
	r.append(regionDisplay[0])
	for i in range(1,len(regionDisplay)-1):
		r.append(regionDisplay[i])
	
	return render_to_response('select.html', {'regionPMDisplay': r, 'form':form})
	

def first_page(request):
	return render_to_response('index.html')




