import os
import datetime
from config import db, image_path

class Costumer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    consumer_unit = db.Column(db.String(8), unique=True, nullable=False)
    consumption_limit = db.Column(db.Integer, nullable=False)
    measurements = db.relationship('Measurement', backref='costumer', lazy=True)

    def __init__(self, consumer_unit, consumption_limit):
        self.consumer_unit = consumer_unit
        self.consumption_limit = consumption_limit


class Measurement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float, nullable=False)
    image_path = db.Column(db.String(200), unique=True, nullable=False)
    costumer_id = db.Column(db.Integer, db.ForeignKey('costumer.id'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

    def __init__(self, value, image_path, costumer_id):
        self.value = value
        self.image_path = image_path
        self.costumer_id = costumer_id


if __name__ == '__main__':
    db.create_all()
    if not os.path.exists(image_path):
        os.makedirs(image_path)