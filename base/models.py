from django.db import models
from django.contrib.auth.models import User

class Car(models.Model):
    doors = models.IntegerField()
    make = models.ForeignKey(Make)
    model = models.CharField(max_length=200)
    year = models.IntegerField()

class Listing(models.Model):
    vendor = models.ForeignKey(Vendor)
    car = models.ForeignKey(Car)
    date_created = models.DateTimeField(auto_now_add=True)

class ListingImage(models.Model):
    image = models.ImageField(upload_to='listings/images')
    listing = models.ForeignKey(Listing)

class Vendor(models.Model):
    contact = models.ForeignKey(User,unique=True)
    website = models.URLField()
    approved = models.BooleanField(default=False)

class Make(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class Trim(models.Model):
    name = models.CharField(max_length=200)
    car = models.ForeignKey(Car)

    def __unicode__(self):
        return self.name

class Option(models.Model):
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
    trim = models.ManyToManyField(Trim)

    def __unicode__(self):
        return "{} - {}".format(self.name, self.value)
