from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application import db
from application.models import Posts, Users

def Unique_title():
    #attempt to colaspe to singel unique function
    message = 'value must be unique'

    def _Unique_title(form, feild):
        if str(Posts.query.filter_by(title = feild.data).all()) != '[]':
            raise ValidationError("Value entered not unique.")
            print('failed validation test for uniqueness')

    return _Unique_title

def Unique_content():

    message = 'value must be unique'

    def _Unique_content(form, feild):
        if str(Posts.query.filter_by(content = feild.data).all()) != '[]':
            raise ValidationError("Value entered not unique.")
            print('failed validation test for uniqueness')

    return _Unique_content


class LoginForm(FlaskForm):
    email = StringField('Email',
        validators=[
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField('Password',
        validators=[
            DataRequired()
        ]
    )

    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

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
            Unique_title()
        ]
    )
    content = StringField('Content',
        validators = [
            DataRequired(),
            Length(min=1, max=1000),
            Unique_content()
        ]
    )
    submit = SubmitField('Post!')
