from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from blog.models import city, region, cityPM
from django.template import loader, Context
from django.shortcuts import render_to_response
from django import forms
import urllib2
import json
from django.db import models

countreading=open('count.txt', 'r')
counting=int(countreading.readline())
countreading.close()
# Grad data using PM25.in's API
url_city = ('http://www.pm25.in/api/querys/aqi_ranking.json?token=ou5URozsKHUrWLfLyDky')
city_content = urllib2.urlopen(url_city).read()
city_data = json.loads(city_content)
for line in city_data:
    cityPM2save = cityPM(city=line['area'], aqi=line['aqi'], quality=line['quality'],pm2_5=line['pm2_5_24h'], pm10=line['pm10_24h'],o3=line['o3_24h'], co=line['co_24h'],no2=line['no2_24h'],so2=line['so2_24h'],addTime=line['time_point'], count=counting)
    cityPM2save.save()
#get_PM_and_Air_data_of_cities(counting)
# delete old data base on the counting value
items = []
items=cityPM.objects.filter(count=(counting - 1))
items.delete()

# delete invalid data
city_invalid_data = []
city_invalid_data = cityPM.objects.filter(pm2_5=0)
city_invalid_data.delete()
# update the counting value in a txt
writingcount=open('count.txt', 'w')
writingcount.write(str(counting + 1))
writingcount.close()
