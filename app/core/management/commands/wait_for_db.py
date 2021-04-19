'''
File: wait_for_db.py
Project: commands
File Created: Monday, 19th April 2021 11:34:09 am
Author: Ananda Yudhistira (anandabayu12@gmail.com)
-----
Last Modified: Monday, 19th April 2021 11:39:32 am
Modified By: Ananda Yudhistira (anandabayu12@gmail.com>)
-----
Copyright 2021 Ananda Yudhistira, FAN Integrasi Teknologi, PT
'''
import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write('Waiting for database...')

        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write('Database unavailable, waiting for a sec...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database running...'))
