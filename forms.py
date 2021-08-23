from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AddTaskForm(FlaskForm): # all forms are inherited from FlaskForm
    title = StringField('Title', validators=[DataRequired()]) # add validators for text field
    submit = SubmitField('Submit') # add submit button

class DeleteTaskForm(FlaskForm):
    submit = SubmitField('Delete')