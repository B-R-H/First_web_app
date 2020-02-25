from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import *
from application import db
from application.models import Posts, Users

def Unique():

    message = 'value must be unique'

    def _Unique(form, feild):
        if str(Posts.query.filter_by(title = feild.data).all()) == '[]':
            raise ValidationError("Vlaue entered not unique.")
            print('failed validation test for uniqueness')

    return _Unique

class RegistrationForm(FlaskForm):
    email = StringField('Email',
        validators = [
            DataRequired(),
            Email()
        ]
    )
    password = PasswordField('Password',
        validators = [
            DataRequired(),
        ]
    )
    confirm_password = PasswordField('Confirm Password',
        validators = [
            DataRequired(),
            EqualTo('password')
        ]
    )
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('Email already in use')


class PostForm(FlaskForm):

    first_name = StringField('First Name',
        validators = [
            DataRequired(),
            Length(min=1, max=30)
        ]
    )
    last_name = StringField('Last Name',
        validators = [
            DataRequired(),
            Length(min=1, max=30)
        ]
    )
    title = StringField('Title',
        validators = [
            DataRequired(),
            Length(min=1, max=100),
            Unique()
        ]
    )
    content = StringField('Content',
        validators = [
            DataRequired(),
            Length(min=1, max=1000),
            #Unique(Posts.content)
        ]
    )
    submit = SubmitField('Post!')
