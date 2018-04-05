# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=60)
    state_abbr = models.CharField(max_length=20)

    def __unicode__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'Persons'


class JobDetail(models.Model):
    name = models.CharField(max_length=120)
    company = models.CharField(max_length=120)
    job = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=60)
    website = models.URLField()
    email = models.EmailField()

    def __unicode__(self):
        return '%s (%s)' % (self.name, self.job)

    class Meta:
        verbose_name = 'Job Detail'
        verbose_name_plural = 'Job Details'


class Automotive(models.Model):
    color = models.CharField(max_length=120)
    license_plate = models.CharField(max_length=120)
    license_date = models.DateTimeField()
    next_license_date = models.DateTimeField()
    token_plate = models.CharField(max_length=255)

    def __unicode__(self):
        return '%s (%s)' % (self.license_plate, self.color)

    class Meta:
        verbose_name = 'Job Detail'
        verbose_name_plural = 'Job Details'
