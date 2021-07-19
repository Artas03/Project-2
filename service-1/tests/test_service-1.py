from flask import url_for
from flask_testing import TestCase
import requests_mock 
from unittest.mock import patch

from application import app, db
from application.models import Vehicles

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI = "sqlite:///data.db")
        return app

    def setUp(self):
        db.create_all()
        db.session.add(Vehicles(make="BMW", model="4 series", mot="3"))
        db.session.commit 
    
    def tearDown(self):
        db.session.remove()

class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for("index"))
        self.assertEqual(response.status_code, 500)

class TestResponse(TestBase):
    def test_BMW1(self):
        with requests_mock.mock() as test:
            test.get("http://make_api:5001/get_make", text='BMW')
            test.get("http://model_api:5002/get_model", text='4 series')
            test.get("http://mot_api:5003/get_mot", text='3')
            response = self.client.get(url_for('index'))
            self.assertIn(b'BMW', response.data)
            self.assertIn(b'4 series', response.data)
            self.assertIn(b'3', response.data)
    def test_BMW2(self):
        with requests_mock.mock() as test:
            test.get("http://make_api:5001/get_make", text='BMW')
            test.get("http://model_api:5002/get_model", text='C63s')
            test.get("http://mot_api:5003/get_mot", text='0')
            response = self.client.get(url_for('index'))
            self.assertIn(b'BMW', response.data)
            self.assertIn(b'C63s', response.data)
            self.assertIn(b'0', response.data)
    def test_BMW3(self):
        with requests_mock.mock() as test:
            test.get("http://make_api:5001/get_make", text='BMW')
            test.get("http://model_api:5002/get_model", text='GTC')
            test.get("http://mot_api:5003/get_mot", text='0')
            response = self.client.get(url_for('index'))
            self.assertIn(b'BMW', response.data)
            self.assertIn(b'GTC', response.data)
            self.assertIn(b'0', response.data)
    def test_BMW4(self):
        with requests_mock.mock() as test:
            test.get("http://make_api:5001/get_make", text='BMW')
            test.get("http://model_api:5002/get_model", text='Civic')
            test.get("http://mot_api:5003/get_mot", text='2')
            response = self.client.get(url_for('index'))
            self.assertIn(b'BMW', response.data)
            self.assertIn(b'Civic', response.data)
            self.assertIn(b'2', response.data)
    def test_BMW5(self):
        with requests_mock.mock() as test:
            test.get("http://make_api:5001/get_make", text='BMW')
            test.get("http://model_api:5002/get_model", text='RS7')
            test.get("http://mot_api:5003/get_mot", text='0')
            response = self.client.get(url_for('index'))
            self.assertIn(b'BMW', response.data)
            self.assertIn(b'RS7', response.data)
            self.assertIn(b'0', response.data)
    def test_BMW6(self):
        with requests_mock.mock() as test:
            test.get("http://make_api:5001/get_make", text='BMW')
            test.get("http://model_api:5002/get_model", text='Scirocco')
            test.get("http://mot_api:5003/get_mot", text='3')
            response = self.client.get(url_for('index'))
            self.assertIn(b'BMW', response.data)
            self.assertIn(b'Scirocco', response.data)
            self.assertIn(b'3', response.data)

    def test_Mercedes1(self):
        with requests_mock.mock() as test:
            test.get("http://make_api:5001/get_make", text='Mercedes')
            test.get("http://model_api:5002/get_model", text='4 series')
            test.get("http://mot_api:5003/get_mot", text='6')
            response = self.client.get(url_for('index'))
            self.assertIn(b'Mercedes', response.data)
            self.assertIn(b'4 series', response.data)
            self.assertIn(b'6', response.data)
    def test_Mercedes2(self):
        with requests_mock.mock() as test:
            test.get("http://make_api:5001/get_make", text='Mercedes')
            test.get("http://model_api:5002/get_model", text='C63s')
            test.get("http://mot_api:5003/get_mot", text='3')
            response = self.client.get(url_for('index'))
            self.assertIn(b'Mercedes', response.data)
            self.assertIn(b'C63s', response.data)
            self.assertIn(b'3', response.data)
    def test_Mercedes3(self):
        with requests_mock.mock() as test:
            test.get("http://make_api:5001/get_make", text='Mercedes')
            test.get("http://model_api:5002/get_model", text='GTC')
            test.get("http://mot_api:5003/get_mot", text='3')
            response = self.client.get(url_for('index'))
            self.assertIn(b'Mercedes', response.data)
            self.assertIn(b'GTC', response.data)
            self.assertIn(b'3', response.data)
    def test_Mercedes4(self):
        with requests_mock.mock() as test:
            test.get("http://make_api:5001/get_make", text='Mercedes')
            test.get("http://model_api:5002/get_model", text='Civic')
            test.get("http://mot_api:5003/get_mot", text='5')
            response = self.client.get(url_for('index'))
            self.assertIn(b'Mercedes', response.data)
            self.assertIn(b'Civic', response.data)
            self.assertIn(b'5', response.data)
    def test_Mercedes5(self):
        with requests_mock.mock() as test:
            test.get("http://make_api:5001/get_make", text='Mercedes')
            test.get("http://model_api:5002/get_model", text='RS7')
            test.get("http://mot_api:5003/get_mot", text='3')
            response = self.client.get(url_for('index'))
            self.assertIn(b'Mercedes', response.data)
            self.assertIn(b'RS7', response.data)
            self.assertIn(b'3', response.data)
    def test_Mercedes6(self):
        with requests_mock.mock() as test:
            test.get("http://make_api:5001/get_make", text='Mercedes')
            test.get("http://model_api:5002/get_model", text='Scirocco')
            test.get("http://mot_api:5003/get_mot", text='6')
            response = self.client.get(url_for('index'))
            self.assertIn(b'Mercedes', response.data)
            self.assertIn(b'Scirocco', response.data)
            self.assertIn(b'6', response.data)

    def test_Vauxhall1(self):
        with requests_mock.mock() as test:
            test.get("http://make_api:5001/get_make", text='Vauxhall')
            test.get("http://model_api:5002/get_model", text='4 series')
            test.get("http://mot_api:5003/get_mot", text='6')
            response = self.client.get(url_for('index'))
            self.assertIn(b'Vauxhall', response.data)
            self.assertIn(b'4 series', response.data)
            self.assertIn(b'6', response.data)
    def test_Vauxhall2(self):
        with requests_mock.mock() as test:
            test.get("http://make_api:5001/get_make", text='Vauxhall')
            test.get("http://model_api:5002/get_model", text='C63s')
            test.get("http://mot_api:5003/get_mot", text='3')
            response = self.client.get(url_for('index'))
            self.assertIn(b'Vauxhall', response.data)
            self.assertIn(b'C63s', response.data)
            self.assertIn(b'3', response.data)
    def test_Vauxhall3(self):
        with requests_mock.mock() as test:
            test.get("http://make_api:5001/get_make", text='Vauxhall')
            test.get("http://model_api:5002/get_model", text='GTC')
            test.get("http://mot_api:5003/get_mot", text='3')
            response = self.client.get(url_for('index'))
            self.assertIn(b'Vauxhall', response.data)
            self.assertIn(b'GTC', response.data)
            self.assertIn(b'3', response.data)
    def test_Vauxhall4(self):
        with requests_mock.mock() as test:
            test.get("http://make_api:5001/get_make", text='Vauxhall')
            test.get("http://model_api:5002/get_model", text='Civic')
            test.get("http://mot_api:5003/get_mot", text='5')
            response = self.client.get(url_for('index'))
            self.assertIn(b'Vauxhall', response.data)
            self.assertIn(b'Civic', response.data)
            self.assertIn(b'5', response.data)
    def test_Vauxhall5(self):
        with requests_mock.mock() as test:
            test.get("http://make_api:5001/get_make", text='Vauxhall')
            test.get("http://model_api:5002/get_model", text='RS7')
            test.get("http://mot_api:5003/get_mot", text='3')
            response = self.client.get(url_for('index'))
            self.assertIn(b'Vauxhall', response.data)
            self.assertIn(b'RS7', response.data)
            self.assertIn(b'3', response.data)
    def test_Vauxhall6(self):
        with requests_mock.mock() as test:
            test.get("http://make_api:5001/get_make", text='Vauxhall')
            test.get("http://model_api:5002/get_model", text='Scirocco')
            test.get("http://mot_api:5003/get_mot", text='6')
            response = self.client.get(url_for('index'))
            self.assertIn(b'Vauxhall', response.data)
            self.assertIn(b'Scirocco', response.data)
            self.assertIn(b'6', response.data)

    def test_Honda1(self):
        with requests_mock.mock() as test:
            test.get("http://make_api:5001/get_make", text='Honda')
            test.get("http://model_api:5002/get_model", text='4 series')
            test.get("http://mot_api:5003/get_mot", text='5')
            response = self.client.get(url_for('index'))
            self.assertIn(b'Honda', response.data)
            self.assertIn(b'4 series', response.data)
            self.assertIn(b'5', response.data)
    def test_Honda2(self):
        with requests_mock.mock() as test:
            test.get("http://make_api:5001/get_make", text='Honda')
            test.get("http://model_api:5002/get_model", text='C63s')
            test.get("http://mot_api:5003/get_mot", text='2')
            response = self.client.get(url_for('index'))
            self.assertIn(b'Honda', response.data)
            self.assertIn(b'C63s', response.data)
            self.assertIn(b'2', response.data)
    def test_Honda3(self):
        with requests_mock.mock() as test:
            test.get("http://make_api:5001/get_make", text='Honda')
            test.get("http://model_api:5002/get_model", text='GTC')
            test.get("http://mot_api:5003/get_mot", text='2')
            response = self.client.get(url_for('index'))
            self.assertIn(b'Honda', response.data)
            self.assertIn(b'GTC', response.data)
            self.assertIn(b'2', response.data)
    def test_Honda4(self):
        with requests_mock.mock() as test:
            test.get("http://make_api:5001/get_make", text='Honda')
            test.get("http://model_api:5002/get_model", text='Civic')
            test.get("http://mot_api:5003/get_mot", text='4')
            response = self.client.get(url_for('index'))
            self.assertIn(b'Honda', response.data)
            self.assertIn(b'Civic', response.data)
            self.assertIn(b'4', response.data)
    def test_Honda5(self):
        with requests_mock.mock() as test:
            test.get("http://make_api:5001/get_make", text='Honda')
            test.get("http://model_api:5002/get_model", text='RS7')
            test.get("http://mot_api:5003/get_mot", text='2')
            response = self.client.get(url_for('index'))
            self.assertIn(b'Honda', response.data)
            self.assertIn(b'RS7', response.data)
            self.assertIn(b'2', response.data)
    def test_Honda6(self):
        with requests_mock.mock() as test:
            test.get("http://make_api:5001/get_make", text='Honda')
            test.get("http://model_api:5002/get_model", text='Scirocco')
            test.get("http://mot_api:5003/get_mot", text='5')
            response = self.client.get(url_for('index'))
            self.assertIn(b'Honda', response.data)
            self.assertIn(b'Scirocco', response.data)
            self.assertIn(b'5', response.data)

    def test_Audi1(self):
        with requests_mock.mock() as test:
            test.get("http://make_api:5001/get_make", text='Audi')
            test.get("http://model_api:5002/get_model", text='4 series')
            test.get("http://mot_api:5003/get_mot", text='5')
            response = self.client.get(url_for('index'))
            self.assertIn(b'Audi', response.data)
            self.assertIn(b'4 series', response.data)
            self.assertIn(b'5', response.data)
    def test_Audi2(self):
        with requests_mock.mock() as test:
            test.get("http://make_api:5001/get_make", text='Audi')
            test.get("http://model_api:5002/get_model", text='C63s')
            test.get("http://mot_api:5003/get_mot", text='2')
            response = self.client.get(url_for('index'))
            self.assertIn(b'Audi', response.data)
            self.assertIn(b'C63s', response.data)
            self.assertIn(b'2', response.data)
    def test_Audi3(self):
        with requests_mock.mock() as test:
            test.get("http://make_api:5001/get_make", text='Audi')
            test.get("http://model_api:5002/get_model", text='GTC')
            test.get("http://mot_api:5003/get_mot", text='2')
            response = self.client.get(url_for('index'))
            self.assertIn(b'Audi', response.data)
            self.assertIn(b'GTC', response.data)
            self.assertIn(b'2', response.data)
    def test_Audi4(self):
        with requests_mock.mock() as test:
            test.get("http://make_api:5001/get_make", text='Audi')
            test.get("http://model_api:5002/get_model", text='Civic')
            test.get("http://mot_api:5003/get_mot", text='4')
            response = self.client.get(url_for('index'))
            self.assertIn(b'Audi', response.data)
            self.assertIn(b'Civic', response.data)
            self.assertIn(b'4', response.data)
    def test_Audi5(self):
        with requests_mock.mock() as test:
            test.get("http://make_api:5001/get_make", text='Audi')
            test.get("http://model_api:5002/get_model", text='RS7')
            test.get("http://mot_api:5003/get_mot", text='2')
            response = self.client.get(url_for('index'))
            self.assertIn(b'Audi', response.data)
            self.assertIn(b'RS7', response.data)
            self.assertIn(b'2', response.data)
    def test_Audi6(self):
        with requests_mock.mock() as test:
            test.get("http://make_api:5001/get_make", text='Audi')
            test.get("http://model_api:5002/get_model", text='Scirocco')
            test.get("http://mot_api:5003/get_mot", text='5')
            response = self.client.get(url_for('index'))
            self.assertIn(b'Audi', response.data)
            self.assertIn(b'Scirocco', response.data)
            self.assertIn(b'5', response.data)

    def test_Volkswagen1(self):
        with requests_mock.mock() as test:
            test.get("http://make_api:5001/get_make", text='Volkswagen')
            test.get("http://model_api:5002/get_model", text='4 series')
            test.get("http://mot_api:5003/get_mot", text='6')
            response = self.client.get(url_for('index'))
            self.assertIn(b'Volkswagen', response.data)
            self.assertIn(b'4 series', response.data)
            self.assertIn(b'6', response.data)
    def test_Volkswagen2(self):
        with requests_mock.mock() as test:
            test.get("http://make_api:5001/get_make", text='Volkswagen')
            test.get("http://model_api:5002/get_model", text='C63s')
            test.get("http://mot_api:5003/get_mot", text='3')
            response = self.client.get(url_for('index'))
            self.assertIn(b'Volkswagen', response.data)
            self.assertIn(b'C63s', response.data)
            self.assertIn(b'3', response.data)
    def test_Volkswagen3(self):
        with requests_mock.mock() as test:
            test.get("http://make_api:5001/get_make", text='Volkswagen')
            test.get("http://model_api:5002/get_model", text='GTC')
            test.get("http://mot_api:5003/get_mot", text='3')
            response = self.client.get(url_for('index'))
            self.assertIn(b'Volkswagen', response.data)
            self.assertIn(b'GTC', response.data)
            self.assertIn(b'3', response.data)
    def test_Volkswagen4(self):
        with requests_mock.mock() as test:
            test.get("http://make_api:5001/get_make", text='Volkswagen')
            test.get("http://model_api:5002/get_model", text='Civic')
            test.get("http://mot_api:5003/get_mot", text='5')
            response = self.client.get(url_for('index'))
            self.assertIn(b'Volkswagen', response.data)
            self.assertIn(b'Civic', response.data)
            self.assertIn(b'5', response.data)
    def test_Volkswagen5(self):
        with requests_mock.mock() as test:
            test.get("http://make_api:5001/get_make", text='Volkswagen')
            test.get("http://model_api:5002/get_model", text='RS7')
            test.get("http://mot_api:5003/get_mot", text='3')
            response = self.client.get(url_for('index'))
            self.assertIn(b'Volkswagen', response.data)
            self.assertIn(b'RS7', response.data)
            self.assertIn(b'3', response.data)
    def test_Volkswagen6(self):
        with requests_mock.mock() as test:
            test.get("http://make_api:5001/get_make", text='Volkswagen')
            test.get("http://model_api:5002/get_model", text='Scirocco')
            test.get("http://mot_api:5003/get_mot", text='6')
            response = self.client.get(url_for('index'))
            self.assertIn(b'Volkswagen', response.data)
            self.assertIn(b'Scirocco', response.data)
            self.assertIn(b'6', response.data)