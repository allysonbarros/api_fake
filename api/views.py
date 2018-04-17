# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from faker import Faker
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Person, JobDetail, Automotive
from api.serializers import PersonSerializer, JobDetailSerializer, AutomotiveSerializer


class PersonListAPI(generics.ListAPIView):
    queryset = Person.objects.all().order_by('?')
    serializer_class = PersonSerializer


class JobDetailListAPI(generics.ListAPIView):
    queryset = JobDetail.objects.all().order_by('?')
    serializer_class = JobDetailSerializer


class AutomotiveListAPI(generics.ListAPIView):
    queryset = Automotive.objects.all().order_by('?')
    serializer_class = AutomotiveSerializer


@api_view(['GET'])
def generate_person_data(request):
    fake = Faker()
    qtd = int(request.GET.get('qtd', 100))

    objects = [{
        'name': fake.name(),
        'address': fake.address(),
        'email': fake.email(),
        'city': fake.city(),
        'state': fake.state(),
        'state_abbr': fake.state_abbr(),
        'job_detail': {
            'company': fake.company(),
            'job': fake.job(),
            'city': fake.city(),
            'state': fake.state(),
            'website': fake.url(),
            'email': fake.company_email()
        },
        'automotive': {
            'color': fake.color_name(),
            'license_plate': fake.license_plate(),
            'license_date': fake.date_time(),
            'next_license_date': fake.future_date(),
            'token_plate': fake.ean13()
        }
    } for _ in range(qtd)]

    return Response(data=objects)
