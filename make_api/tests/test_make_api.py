from flask import url_for
from flask_testing import TestCase
from app import app
from unittest.mock import patch

class TestBase(TestCase):
    def create_app(self):
        return app

class TestHome(TestBase):
    def test_get_make(self):
        with patch('random.choice') as r:
            r.return_value = 'BMW'
        i = 0
        for i in range(6):
            response = self.client.get(url_for('get_make'))
            make_list = [b'BMW',b'Mercedes',b'Vauxhall',b'Honda',b'Audi',b'Volkswagen']
            self.assertIn(response.data, make_list)
            i += 1