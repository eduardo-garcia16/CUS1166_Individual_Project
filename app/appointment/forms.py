from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField, DateTimeField
from wtforms.validators import ValidationError, DataRequired, Length

class AppointmentForm(FlaskForm):
    appo_title = StringField('appo_title', validators=[DataRequired()])
    appo_date = DateTimeField('appo_date', validators=[DataRequired()], format='%Y-%m-%d %H:%M:%S')
    appo_duration = StringField('appo_duration', validators=[DataRequired()])
    appo_location = StringField('appo_location', validators=[DataRequired()])
    appo_customer_name = StringField('appo_customer_name', validators=[DataRequired()])
    appo_notes = StringField('appo_notes', validators=[Length(min=0, max=300)])
