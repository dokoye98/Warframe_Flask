from flask_testing import TestCase
from application import app,db,models
from flask import redirect, url_for, render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField
from application import __init__,routes,models
from application.models import Customer,Tenno

class TestBase(TestCase):

    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI='sqlite:///test.db',
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app

    def setUp_customer(self):
        db.create_all()
        custom1=Customer(first_name='slimes',last_name='1231',username='1231',password='sdasa',card_details='1231',membership=False)
        db.session.add(custom1)
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestAdd(TestBase):
    def test_add_customer(self):
        # add a new customer to the database
        response = self.client.post(
            url_for('add_customer'),
            data = dict(first_name='qda',
                last_name='1231',
                username='1231',
                password='sdasa',
                card_details='1231',
                membership=False
            )
        )
        # as it's the second dog that's been added to the database
        # after Chewbarka in the setUp() method
        assert Customer.query.filter_by(first_name='qda').first().id == 2


class TestDelete(TestBase):
    def test_delete_customer(self):
        # delete Chewbarka from the database
        response = self.client.delete(
            url_for('delete_customer'),
            data = dict(first_name='qda',last_name='1231',username='1231',password='sdasa',card_details='1231',membership=False)
        )
        # query the dog table - if Chewbarka has been deleted,
        # the query should return an empty list
        assert len(Customer.query.all()) == 0

class TestViews(TestBase):
    def test_view_customer(self):
        response = self.client.get(url_for('about')) # send a GET request
        self.assertEqual(response.status_code, 200) # assert that the response code is 200
        self.assertIn(b'This is the about here you can create an account and character or "Tenno" page', response.data)   

class Testupdate(TestBase):
    def test_update_customer(self):
        respone = self.client.post(
            url_for('update_customer', id=1),
            data = dict(first_name='qdas',last_name='1231',username='1231',password='sdasa',card_details='1231',membership=False)
            )
        assert len(Customer.query.all()) == 1
        assert Customer.query.filter_by(first_name= 'qdas')

        