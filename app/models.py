from app import db
from datetime import datetime

class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    from_name = db.Column(db.String(100), nullable=False)
    from_business = db.Column(db.String(100))
    from_email = db.Column(db.String(120))
    from_address = db.Column(db.String(200))
    from_phone = db.Column(db.String(20))
    from_gst = db.Column(db.String(20))
    to_name = db.Column(db.String(100), nullable=False)
    to_email = db.Column(db.String(120))
    to_address = db.Column(db.String(200))
    to_phone = db.Column(db.String(20))
    to_mobile = db.Column(db.String(20))
    to_fax = db.Column(db.String(20))
    number = db.Column(db.String(20), unique=True, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    terms = db.Column(db.String(50))
    description = db.Column(db.Text)
    rate = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    tax_rate = db.Column(db.Float)

    def __repr__(self):
        return f'<Invoice {self.number}>'
