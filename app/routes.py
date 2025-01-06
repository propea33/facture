from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Invoice
from app.forms import InvoiceForm

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    form = InvoiceForm()
    if form.validate_on_submit():
        invoice = Invoice(
            from_name=form.from_name.data,
            from_business=form.from_business.data,
            from_email=form.from_email.data,
            from_address=form.from_address.data,
            from_phone=form.from_phone.data,
            from_gst=form.from_gst.data,
            to_name=form.to_name.data,
            to_email=form.to_email.data,
            to_address=form.to_address.data,
            to_phone=form.to_phone.data,
            to_mobile=form.to_mobile.data,
            to_fax=form.to_fax.data,
            number=form.number.data,
            terms=form.terms.data,
            description=form.description.data,
            rate=form.rate.data,
            quantity=form.quantity.data,
            tax_rate=form.tax_rate.data
        )
        db.session.add(invoice)
        db.session.commit()
        return redirect(url_for('main.invoice', id=invoice.id))
    return render_template('index.html', form=form)

@main.route('/invoice/<int:id>')
def invoice(id):
    invoice = Invoice.query.get_or_404(id)
    subtotal = invoice.rate * invoice.quantity
    tax = subtotal * (invoice.tax_rate / 100)
    total = subtotal + tax
    return render_template('invoice.html', invoice=invoice, subtotal=subtotal, tax=tax, total=total)
