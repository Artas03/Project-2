from flask import url_for
from flask_testing import TestCase
from app import app
from unittest.mock import patch

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_BMW1(self):
        response = self.client.get(url_for('get_mot'), json={'make':'BMW', 'model':'4 series'})
        self.assertEqual(b'3', response.data)
    def test_BMW2(self):
        response = self.client.get(url_for('get_mot'), json={'make':'BMW', 'model':'C63s'})
        self.assertEqual(b'0', response.data)
    def test_BMW3(self):
        response = self.client.get(url_for('get_mot'), json={'make':'BMW', 'model':'GTC'})
        self.assertEqual(b'0', response.data)
    def test_BMW4(self):
        response = self.client.get(url_for('get_mot'), json={'make':'BMW', 'model':'Civic'})
        self.assertEqual(b'2', response.data)
    def test_BMW5(self):
        response = self.client.get(url_for('get_mot'), json={'make':'BMW', 'model':'RS7'})
        self.assertEqual(b'0', response.data)
    def test_BMW6(self):
        response = self.client.get(url_for('get_mot'), json={'make':'BMW', 'model':'Scirocco'})
        self.assertEqual(b'3', response.data)
    def test_Mercedes1(self):
        response = self.client.get(url_for('get_mot'), json={'make':'Mercedes', 'model':'4 series'})
        self.assertEqual(b'6', response.data)
    def test_Mercedes2(self):
        response = self.client.get(url_for('get_mot'), json={'make':'Mercedes', 'model':'C63s'})
        self.assertEqual(b'3', response.data)
    def test_Mercedes3(self):
        response = self.client.get(url_for('get_mot'), json={'make':'Mercedes', 'model':'GTC'})
        self.assertEqual(b'3', response.data)
    def test_Mercedes4(self):
        response = self.client.get(url_for('get_mot'), json={'make':'Mercedes', 'model':'Civic'})
        self.assertEqual(b'5', response.data)
    def test_Mercedes5(self):
        response = self.client.get(url_for('get_mot'), json={'make':'Mercedes', 'model':'RS7'})
        self.assertEqual(b'3', response.data)
    def test_Mercedes6(self):
        response = self.client.get(url_for('get_mot'), json={'make':'Mercedes', 'model':'Scirocco'})
        self.assertEqual(b'6', response.data)
    def test_Vauxhall1(self):
        response = self.client.get(url_for('get_mot'), json={'make':'Vauxhall', 'model':'4 series'})
        self.assertEqual(b'6', response.data)
    def test_Vauxhall2(self):
        response = self.client.get(url_for('get_mot'), json={'make':'Vauxhall', 'model':'C63s'})
        self.assertEqual(b'3', response.data)
    def test_Vauxhall3(self):
        response = self.client.get(url_for('get_mot'), json={'make':'Vauxhall', 'model':'GTC'})
        self.assertEqual(b'3', response.data)
    def test_Vauxhall4(self):
        response = self.client.get(url_for('get_mot'), json={'make':'Vauxhall', 'model':'Civic'})
        self.assertEqual(b'5', response.data)
    def test_Vauxhall5(self):
        response = self.client.get(url_for('get_mot'), json={'make':'Vauxhall', 'model':'RS7'})
        self.assertEqual(b'3', response.data)
    def test_Vauxhall6(self):
        response = self.client.get(url_for('get_mot'), json={'make':'Vauxhall', 'model':'Scirocco'})
        self.assertEqual(b'6', response.data)
    def test_Honda1(self):
        response = self.client.get(url_for('get_mot'), json={'make':'Honda', 'model':'4 series'})
        self.assertEqual(b'5', response.data)
    def test_Honda2(self):
        response = self.client.get(url_for('get_mot'), json={'make':'Honda', 'model':'C63s'})
        self.assertEqual(b'2', response.data)
    def test_Honda3(self):
        response = self.client.get(url_for('get_mot'), json={'make':'Honda', 'model':'GTC'})
        self.assertEqual(b'2', response.data)
    def test_Honda4(self):
        response = self.client.get(url_for('get_mot'), json={'make':'Honda', 'model':'Civic'})
        self.assertEqual(b'4', response.data)
    def test_Honda5(self):
        response = self.client.get(url_for('get_mot'), json={'make':'Honda', 'model':'RS7'})
        self.assertEqual(b'2', response.data)
    def test_Honda6(self):
        response = self.client.get(url_for('get_mot'), json={'make':'Honda', 'model':'Scirocco'})
        self.assertEqual(b'5', response.data)
    def test_Audi1(self):
        response = self.client.get(url_for('get_mot'), json={'make':'Audi', 'model':'4 series'})
        self.assertEqual(b'5', response.data)
    def test_Audi2(self):
        response = self.client.get(url_for('get_mot'), json={'make':'Audi', 'model':'C63s'})
        self.assertEqual(b'2', response.data)
    def test_Audi3(self):
        response = self.client.get(url_for('get_mot'), json={'make':'Audi', 'model':'GTC'})
        self.assertEqual(b'2', response.data)
    def test_Audi4(self):
        response = self.client.get(url_for('get_mot'), json={'make':'Audi', 'model':'Civic'})
        self.assertEqual(b'4', response.data)
    def test_Audi5(self):
        response = self.client.get(url_for('get_mot'), json={'make':'Audi', 'model':'RS7'})
        self.assertEqual(b'2', response.data)
    def test_Audi6(self):
        response = self.client.get(url_for('get_mot'), json={'make':'Audi', 'model':'Scirocco'})
        self.assertEqual(b'5', response.data)
    def test_Volkswagen1(self):
        response = self.client.get(url_for('get_mot'), json={'make':'Volkswagen', 'model':'4 series'})
        self.assertEqual(b'6', response.data)
    def test_Volkswagen2(self):
        response = self.client.get(url_for('get_mot'), json={'make':'Volkswagen', 'model':'C63s'})
        self.assertEqual(b'3', response.data)
    def test_Volkswagen3(self):
        response = self.client.get(url_for('get_mot'), json={'make':'Volkswagen', 'model':'GTC'})
        self.assertEqual(b'3', response.data)
    def test_Volkswagen4(self):
        response = self.client.get(url_for('get_mot'), json={'make':'Volkswagen', 'model':'Civic'})
        self.assertEqual(b'5', response.data)
    def test_Volkswagen5(self):
        response = self.client.get(url_for('get_mot'), json={'make':'Volkswagen', 'model':'RS7'})
        self.assertEqual(b'3', response.data)
    def test_Volkswagen6(self):
        response = self.client.get(url_for('get_mot'), json={'make':'Volkswagen', 'model':'Scirocco'})
        self.assertEqual(b'6', response.data)

