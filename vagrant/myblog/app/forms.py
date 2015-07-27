from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired


# subclassed from base class Form
class LoginForm(Form):
	# DataRequired validator simply checks that the field is not submitted empty
	# openid is authentication done by the provider of the OpenID
	# StringField and BooleanField are form field imported to save the openid and rememember me boolean
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)