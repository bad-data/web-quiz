from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, RadioField, SelectField
from wtforms.validators import DataRequired
import helper

class quizForm(FlaskForm):
    question1 = RadioField('', choices=[('trex','T-Rex'),('aerodactyl','Aerodactyl'),('velociraptor','Velociraptor'),('longneck','Long Neck')])
    question2 = RadioField('', choices=[('t','True'),('f','False')])
    question3 = RadioField('', choices=[('trex','T-Rex'),('aerodactyl','Aerodactyl'),('velociraptor','Velociraptor'),('longneck','Long Neck')])
    question4 = RadioField('', choices=[('10million','10 Million'),('yesterday','Yesterday'),('1billion','1 Billion'),('100thousand','100 Thousand')])
    question5 = RadioField('', choices=[('trex','T-Rex'),('aerodactyl','Aerodactyl'),('velociraptor','Velociraptor'),('longneck','Long Neck')])
    submit = SubmitField('Submit Quiz')

class submitForm(FlaskForm):
    submit = SubmitField('Start Quiz')

class questionForm(FlaskForm):
    question = RadioField('Choose From Below', choices=[])
    nextQuestion = SubmitField('Next Question')

class onePageQuizForm(FlaskForm):
    question1 = RadioField('Select Answer:', choices=[])
    question2 = RadioField('Select Answer:', choices=[])
    question3 = RadioField('Select Answer:', choices=[])
    submit = SubmitField('Next')