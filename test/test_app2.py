from application import models, db, app
from application.models import Tenno, Customer
from flask_testing import TestCase
from flask import url_for

class TestBase(TestCase):
    def create_app(self):

        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    def setUp(self):
        db.create_all()
       
        custom1=Customer(first_name='slimes',
        last_name='1231',
        username='1231',
        password='sdasa',
        card_details='1231',
        membership=False)
        tenno1=Tenno(warframe='slime',
        health=12313,
        mp=213321,
        prime=False)
        db.session.add(custom1)
        db.session.add(tenno1)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):
    def test_customer_get(self):
        response = self.client.get(url_for('customers'))
        self.assertEqual(response.status_code, 200)

    def test_tenno_get(self):
        response = self.client.get(url_for('TENNO'))
        self.assertEqual(response.status_code, 200)

    def test_about_get(self):
        response = self.client.get(url_for('about'))
        self.assertEqual(response.status_code, 200)
    
    def test_add_customer_get(self):
        response = self.client.get(url_for('add_customer'))
        self.assertEqual(response.status_code, 200)
    
    def test_add_tenno_get(self):
        response = self.client.get(url_for('add_tenno'))
        self.assertEqual(response.status_code, 200)

    def test_update_customer_get(self):
        response = self.client.get(url_for('update_customer', id=1))
        self.assertEqual(response.status_code, 200)
    
    def test_update_tenno_get(self):
        response = self.client.get(url_for('update_tenno', id=1))
        self.assertEqual(response.status_code, 200)
    
    def test_delete_customer_get(self):
        response = self.client.get(url_for('delete_customer', id=1))
        self.assertEqual(response.status_code, 302)
    
    def test_delete_tenno_get(self):
        response = self.client.get(url_for('delete_tenno', id=1))
        self.assertEqual(response.status_code, 302)



class TestAddCustomer(TestBase):
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
        assert Customer.query.filter_by(first_name='qda').first().id == 2
        

class TestAddtenno(TestBase):
    def test_add_tenno(self):
        response = self.client.post(
            url_for('add_tenno'),
            data = dict(warframe='sasd',
            health=123,
            mp=1231,
            prime=True)
        )
        
        assert Tenno.query.filter_by(warframe='sasd').first().char_id == 2

class TestUpdateCustomer(TestBase):
    def test_update_customer(self):
        response = self.client.post(
            'update_customer/1',
            data = dict(first_name='qdasda',
                last_name='1231',
                username='1231',
                password='sdasa',
                card_details='1231',
                membership=False
        ),
        follow_redirects = True
        )
        self.assertIn(b'qdasda', response.data)

class TestupdateTenno(TestBase):
    def test_update_tenno(self):
        response = self.client.post(
            'updatetenno/1',
            data = dict(warframe='sasd',
            health=123,
            mp=1231,
            prime=True
        ),
        follow_redirects = True
        )
        self.assertIn(b'sasd', response.data)


class TestDeleteCustomer(TestBase):
    def test_delete_customer(self):
        response = self.client.get(
            url_for('delete_customer', id = 1)
        )
        assert len(Customer.query.all()) == 0

        
class TestDeleteTenno(TestBase):
    def test_delete_tenno(self):
        response = self.client.get(
            url_for('delete_tenno', id = 1)

        )
        assert len(Tenno.query.all()) == 0