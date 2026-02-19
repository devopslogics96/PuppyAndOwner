from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField        
class AddPuppyForm(FlaskForm):
    name = StringField('Puppy Name')
    submit = SubmitField('Add Puppy')