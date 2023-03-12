from . import db

class PropertyProfile(db.Model):
    
    __tablename__ = 'property_profiles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(180))
    desc = db.Column(db.String(250))
    bedrooms = db.Column(db.Integer)
    bathrooms = db.Column(db.Integer)
    price = db.Column(db.String(80))
    property_type = db.Column(db.String(80))
    location = db.Column(db.String(180))
    photo_filename = db.Column(db.String(80))
    
    def __init__(self, title, desc, bedrooms, bathrooms, price, prop_type, location, photo_filename):
        self.title = title
        self.desc = desc
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.price = price
        self.property_type = prop_type
        self.location = location
        self.photo_filename = photo_filename
        
