from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import data_required
from models import headphones,washingmachin,PC,mobilephones


class Add(FlaskForm):

    s_q = StringField("s_q", validators=[data_required()])
    name = StringField("name", validators=[data_required()])
    info1 = IntegerField("info1", validators=[data_required()])
    info2 = IntegerField("info2", validators=[data_required()])
    info3 = IntegerField("info3", validators=[data_required()])
    image_url = StringField("image_url", validators=[data_required()])
    add_password = StringField("add_password", validators=[data_required()])
    submit = SubmitField("submit")


class login(FlaskForm):
    name = StringField("name", validators=[data_required()])
    email = StringField("email", validators=[data_required()])
    password = StringField("password", validators=[data_required()])
    submit = SubmitField("submit")










