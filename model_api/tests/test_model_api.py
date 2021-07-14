from flask import url_for
from flask_testing import TestCase
from app import app
from unittest.mock import patch

class TestBase(TestCase):
    def create_app(self):
        return app

class TestHome(TestBase):
    def test_get_model(self):
        with patch('random.choice') as p:
            p.return_value = '4 series'
        i = 0
        for i in range(6):
            response = self.client.get(url_for('get_model'))
            model_list = [b'4 series',b'C63s',b'GTC',b'Civic',b'RS7',b'Scirocco']
            self.assertIn(response.data, model_list)
            i += 1