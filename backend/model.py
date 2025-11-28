

# Class
# Set variables
# function toJson
# map kv pairs

from config import db

class Products(db.Model):
    prod_id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(80))
    g_name = db.Column(db.String(80))
    b_name = db.Column(db.String(80))
    d_arrived = db.Column(db.String(80))
    d_expired = db.Column(db.String(80))
    cost = db.Column(db.String(80))
    price = db.Column(db.String(80))
    qty = db.Column(db.String(80))
    stock_status = db.Column(db.String(80))
    created_at = db.Column(db.String(80))
    
    def to_json(self):
        return {
            'prod_id': self.prod_id,
            'category': self.category,
            'gName' : self.g_name,
            'bName': self.b_name,
            'dArrived': self.d_arrived,
            'dExpired': self.d_expired,
            'cost': self.cost,
            'price': self.price,
            'qty': self.qty,
            'stockStatus': self.stock_status,
            'createdAt': self.created_at
        }