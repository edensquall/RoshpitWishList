from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, FieldList, IntegerField, \
    FormField, validators, RadioField
from wtforms.validators import InputRequired, Length, Email, EqualTo, ValidationError

from app import User


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=20)])
    name = StringField('Display Name', validators=[InputRequired(), Length(min=4, max=20)])
    email = StringField('E-Mail', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=6, max=10)])
    password_confirm = PasswordField('Password(Confirm)', validators=[
        InputRequired(),
        Length(min=6, max=10),
        EqualTo('password', 'Password must match')])
    submit = SubmitField('Submit')

    def validate_username(self, username):
        user = User.query.filter_by(account=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose another.')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=6, max=10)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Submit')


class WishPropertyForm(FlaskForm):
    class Meta:
        csrf = False

    property_id = SelectField('', coerce=str, choices=[], render_kw={'class': 'custom-select'})
    roll = StringField('', filters=[lambda x: x or None])


class WishForm(FlaskForm):
    item_type = SelectField('Item Type', coerce=str, choices=[])
    item_id = SelectField('Item', coerce=str, choices=[], validators=[validators.required()])
    wish_properties = FieldList(FormField(WishPropertyForm))
    currency = SelectField('Currency', coerce=int,
                           choices=[(0, 'Choose'), (1, 'Mithril Shards'), (2, 'Arcane Crystals')],
                           validators=[validators.required()])
    min_level = IntegerField('Min Level', default=0)
    max_bid = IntegerField('Max Bid', default=0)
    max_buyout = IntegerField('Max Buyout', default=0)
    submit = SubmitField('Submit')


class SettingsForm(FlaskForm):
    name = StringField('Display Name', validators=[InputRequired(), Length(min=4, max=20)])
    email = StringField('E-Mail', validators=[InputRequired(), Email()])
    is_notification = BooleanField('Is Notification')
    notification_method = RadioField('Method', coerce=int, choices=[(1, 'E-mail'), (2, 'LINE')], default=1)
    submit = SubmitField('Submit')
