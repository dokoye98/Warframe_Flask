from application.models import Customer,Tenno
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,IntegerField,SelectField, SubmitField
class Customerform(FlaskForm):
    first_name = StringField("First name")
    last_name = StringField("Last name")
    username=StringField("Username")
    password=StringField("Password")
    card_details=StringField("Card details")
    membership=BooleanField("Membership")
    submit = SubmitField("Submit")

class Tennoform(FlaskForm):
    warframe=StringField("Warframe")
    prime=BooleanField("Prime")
    health=IntegerField("Health")
    mp=IntegerField("MP")
    submit = SubmitField("Submit")

