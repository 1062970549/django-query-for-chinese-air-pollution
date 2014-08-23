from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from blog.models import city, region, cityAir, cityPM, regionPM
from django.template import loader, Context
from django.shortcuts import render_to_response
from django import forms
import urllib2
import json
from django.db import models

countreading=open('count_hourly.txt', 'r')
counting=int(countreading.readline())
countreading.close()
# Grad data using PM25.in's API
url = ('http://www.pm25.in/api/querys/all_cities.json?token=ou5URozsKHUrWLfLyDky')
content = urllib2.urlopen(url).read()
#content=open('all_cities.json','r').read()
data = json.loads(content)
for line in data:
    regionPM2 = regionPM(city=line['area'], area=line['position_name'], aqi=line['aqi'], quality=line['quality'],pm2_5=line['pm2_5'], pm10=line['pm10'], addTime=line['time_point'], count=counting)
    regionPM2.save()
#get_PM_and_Air_data_of_cities(counting)
# delete old data base on the counting value
items = []
items=regionPM.objects.filter(count=(counting - 1))
items.delete()

# delete invalid data
region_invalid_data = []
region_invalid_data = regionPM.objects.filter(pm2_5=0)
region_invalid_data.delete()
# update the counting value in a txt
writingcount=open('count_hourly.txt', 'w')
writingcount.write(str(counting + 1))
writingcount.close()
