from abc import ABC, abstractmethod
from enums.size import Size
from app import db


class Toy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer)
    size = db.Column(db.String)
    toy_type = db.Column(db.String)

    def __init__(self, price=0, size=Size, toy_type=None):

        self.price = price
        self.size = size
        self.toy_type = toy_type

    @abstractmethod
    def play(self):
        pass

    def __str__(self):
        return "{ Toy type: " + str(self.toy_type) + ", price: " + str(self.price) + " }"
