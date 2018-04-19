# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from rest_framework import generics
from rest_framework.response import Response

from api.models import Person, JobDetail, Automotive
from api.serializers import PersonSerializer, JobDetailSerializer, AutomotiveSerializer


class PersonListAPI(generics.ListAPIView):
    queryset = Person.objects.all().order_by('?')
    serializer_class = PersonSerializer

    def list(self, request, *args, **kwargs):
        qtd_registros = request.GET.get('qtd', 1000)

        queryset = self.get_queryset()[:qtd_registros]
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class JobDetailListAPI(generics.ListAPIView):
    queryset = JobDetail.objects.all().order_by('?')
    serializer_class = JobDetailSerializer

    def list(self, request, *args, **kwargs):
        qtd_registros = request.GET.get('qtd', 1000)

        queryset = self.get_queryset()[:qtd_registros]
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class AutomotiveListAPI(generics.ListAPIView):
    queryset = Automotive.objects.all().order_by('?')
    serializer_class = AutomotiveSerializer

    def list(self, request, *args, **kwargs):
        qtd_registros = request.GET.get('qtd', 1000)

        queryset = self.get_queryset()[:qtd_registros]
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
