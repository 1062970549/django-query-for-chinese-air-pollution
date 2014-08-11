#!/usr/bin/python
# -*- coding: utf-8 -*-

#from models import city, region, cityAir, cityPM, regionPM
from django import *
#from django import forms
from blog.models import city, region, cityAir, cityPM, regionPM

import urllib2
import json



def get_PM_and_Air_data_of_cities(the_counting):
    url = ('http://www.pm25.in/api/querys/all_cities.json?token=ou5URozsKHUrWLfLyDky')
    content = urllib2.urlopen(url).read()
    data = json.loads(content)

    # City air condition of the cities
    # PM and aqi condition of the cities
    for line in data:
        cityAir2 = cityAir(name=line['area'], CO=line['co'], NO2=line['no2'], O3=line['o3'], SO2=line['so2'])
        regionPM2 = regionPM(city=line['area'], area=line['position_name'], aqi=line['aqi'], quality=line['quality'],pm2_5=line['pm2_5'], pm10=line['pm10'], addTime=line['time_point'], count=the_counting)

        # Writing data into database.
        cityAir2.save()
        regionPM2.save()


# city and quality may be null
# read count of the update
f = open('count.txt', 'r')
counting = int(f.readline())
f.close()

# Grad data using PM25.in's API
get_PM_and_Air_data_of_cities(counting)

# delete old data base on the counting value
data_to_delete = regionPM.objects.filter(count=(counting - 1)).delete()

# update the counting value in a txt
w = open('count.txt', 'w')
w.write(str(counting + 1))
w.close()  # TODO Delete the null values: PM 2.5 values = 0


