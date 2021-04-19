'''
File: test_commands.py
Project: test
File Created: Monday, 19th April 2021 11:21:48 am
Author: Ananda Yudhistira (anandabayu12@gmail.com)
-----
Last Modified: Monday, 19th April 2021 11:31:09 am
Modified By: Ananda Yudhistira (anandabayu12@gmail.com>)
-----
Copyright 2021 Ananda Yudhistira, FAN Integrasi Teknologi, PT
'''
from unittest.mock import patch

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import TestCase


class CommandTest(TestCase):

    def test_wait_db_ready(self):
        """Check if db available"""
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.return_value = True
            call_command('wait_for_db')

            self.assertEqual(gi.call_count, 1)

    @patch('time.sleep', return_value=True)
    def test_wait_for_db(self, ts):
        """Waiting for db"""
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.side_effect = [OperationalError] * 5 + [True]
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 6)
