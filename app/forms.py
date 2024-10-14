from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators
from wtforms.validators import DataRequired

class CompanyInformationForm(FlaskForm):
    phoneNumber = StringField('Phone Number', validators=[DataRequired(), validators.Length(max=32)])
    submit = SubmitField('Submit')