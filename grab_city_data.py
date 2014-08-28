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





# Feature: Grab the data of the best 30 city order by PM2.5
best_30_city = cityPM.objects.order_by('pm2_5','aqi')[:30]
worst_30_city = cityPM.objects.order_by('-pm2_5','-aqi')[:30]
	# Writing data into tsv file
write_first_line = open('blog/static/data/city_data.tsv','w')
write_first_line.write('city	PM2_5\n')
write_first_line.close()
	# open writing process in adding mode
write_data = open('blog/static/data/city_data.tsv','a')
for city in best_30_city:
	write_data.write(city.city.encode('utf-8')+'\t'+str(city.pm2_5)+'\n')
for worst_city in worst_30_city:
	write_data.write(worst_city.city.encode('utf-8')+'\t'+str(worst_city.pm2_5)+'\n')
write_data.close()




# update the counting value in a txt
writingcount=open('count.txt', 'w')
writingcount.write(str(counting + 1))
writingcount.close()
