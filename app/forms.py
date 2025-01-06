from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FloatField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Email

class InvoiceForm(FlaskForm):
    from_name = StringField('From Name', validators=[DataRequired()])
    from_business = StringField('Business Name')
    from_email = StringField('Email', validators=[Email()])
    from_address = StringField('Address')
    from_phone = StringField('Phone')
    from_gst = StringField('GST #')
    to_name = StringField('To Name', validators=[DataRequired()])
    to_email = StringField('Email', validators=[Email()])
    to_address = StringField('Address')
    to_phone = StringField('Phone')
    to_mobile = StringField('Mobile')
    to_fax = StringField('Fax')
    number = StringField('Invoice Number', validators=[DataRequired()])
    terms = StringField('Terms')
    description = TextAreaField('Description')
    rate = FloatField('Rate')
    quantity = IntegerField('Quantity')
    tax_rate = FloatField('Tax Rate (%)')
    submit = SubmitField('Generate Invoice')
