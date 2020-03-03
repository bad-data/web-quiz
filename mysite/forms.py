from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, RadioField
from wtforms.validators import DataRequired
import helper

class quizForm(FlaskForm):
    question1 = RadioField('1. Which dinosaur was known for it\'s wings?', choices=[('trex','T-Rex'),('aerodactyl','Aerodactyl'),('velociraptor','Velociraptor'),('longneck','Long Neck')])
    question2 = RadioField('2. Could dinosaurs swim?', choices=[('t','True'),('f','False')])
    question3 = RadioField('3. What was the tallest dinosaur?', choices=[('trex','T-Rex'),('aerodactyl','Aerodactyl'),('velociraptor','Velociraptor'),('longneck','Long Neck')])
    question4 = RadioField('4. How many years ago did dinosaurs go extinct', choices=[('10million','10 Million'),('yesterday','Yesterday'),('1billion','1 Billion'),('100thousand','100 Thousand')])
    question5 = RadioField('5. Which dinosaur was at hole #6?', choices=[('trex','T-Rex'),('aerodactyl','Aerodactyl'),('velociraptor','Velociraptor'),('longneck','Long Neck')])
    submit = SubmitField('Submit Quiz')

class submitForm(FlaskForm):
    submit = SubmitField('Start Quiz')