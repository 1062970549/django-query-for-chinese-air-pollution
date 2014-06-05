from django.db import models

class city(models.Model):
    name = models.CharField(max_length=30)
    #address = models.CharField(max_length=50)
    #city = models.CharField(max_length=60)
    #state_province = models.CharField(max_length=30)
    #country = models.CharField(max_length=50)
    #website = models.URLField()
    def __unicode__(self):
        return self.name

class cityPM(models.Model):
    name = models.CharField(max_length=30)
    aqi = models.IntegerField(default = 0)
    quality = models.CharField(max_length=40)
    pm2_5 = models.IntegerField(default = 0)
    pm10 = models.IntegerField(default = 0)

    def __unicode__(self):
        return u'%s %s %s %s %s' % (self.name, self.aqi, self.quality, self.pm2_5, self.pm10)
    


class cityAir(models.Model):
    name = models.CharField(max_length=30)
    CO = models.IntegerField(default = 0)
    NO2 = models.IntegerField(default = 0)
    O3 = models.IntegerField(default = 0)
    SO2 = models.IntegerField(default = 0)

    def __unicode__(self):
        return u'%s %s %s %s %s' % (self.name, self.CO, self.NO2, self.O3, self.SO2)

class region(models.Model):
    name = models.CharField(max_length=30)
    area = models.CharField(max_length=30)

    def __unicode__(self):
        return u'%s %s' % (self.name, self.area)


class regionPM(models.Model):
    city = models.CharField(max_length=30)
    area = models.CharField(max_length=30)
    aqi = models.IntegerField(default = 0)
    quality = models.CharField(max_length=40,null = True, blank = True, default = '')
    pm2_5 = models.IntegerField(default = 0)
    pm10 = models.IntegerField(default = 0)
    addTime = models.DateTimeField(auto_now = True)

    def __unicode__(self):
        return u'%s %s %f %s %f %f' % (self.city, self.area, float(self.aqi), self.quality, float(self.pm2_5), float(self.pm10))
   

