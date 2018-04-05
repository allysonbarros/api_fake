# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers

from api.models import Person, JobDetail, Automotive


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'name', 'address', 'email', 'city', 'state', 'state_abbr')


class JobDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JobDetail
        fields = ('id', 'name', 'company', 'job', 'city', 'state', 'website', 'email')


class AutomotiveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Automotive
        fields = ('id', 'color', 'license_plate', 'license_date', 'next_license_date', 'token_plate')
