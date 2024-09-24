from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class MorseForm(FlaskForm):
    text_to_morse = StringField(validators=[DataRequired()])
    submit = SubmitField(label='Translate')