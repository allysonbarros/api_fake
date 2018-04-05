# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.management.base import BaseCommand

from faker import Faker

from api.models import Person, JobDetail, Automotive


class Command(BaseCommand):
    help = 'Realiza o cadastro de dados fake no banco de dados.'

    def add_arguments(self, parser):
        parser.add_argument('qtd', nargs='+', type=int)

    def handle(self, *args, **options):
        # self._create_person_fake_data(options.get('qtd')[0])
        self._create_job_detail_fake_data(options.get('qtd')[0])
        self._create_automotive_fake_data(options.get('qtd')[0])

    def _create_person_fake_data(self, qtd):
        fake = Faker()
        for _ in range(qtd):
            Person.objects.create(**{
                'name': fake.name(),
                'address': fake.address(),
                'email': fake.email(),
                'city': fake.city(),
                'state': fake.state(),
                'state_abbr': fake.state_abbr(),
            })

    def _create_job_detail_fake_data(self, qtd):
        fake = Faker()
        for _ in range(qtd):
            JobDetail.objects.create(**{
                'company': fake.company(),
                'job': fake.job(),
                'city': fake.city(),
                'state': fake.state(),
                'website': fake.url(),
                'email': fake.company_email()
            })

    def _create_automotive_fake_data(self, qtd):
        fake = Faker()
        for _ in range(qtd):
            Automotive.objects.create(**{
                'color': fake.color_name(),
                'license_plate': fake.license_plate(),
                'license_date': fake.date_time(),
                'next_license_date': fake.future_date(),
                'token_plate': fake.ean13()
            })