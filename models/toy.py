from abc import ABC, abstractmethod
from enums.size import Size


class Toy(ABC):

    def __init__(self, price=0, size=Size, toy_type=None):

        self.price = price
        self.size = size
        self.toy_type = toy_type

    @abstractmethod
    def play(self):
        pass

    def __str__(self):
        return "{ Toy type: " + str(self.toy_type) + ", price: " + str(self.price) + " }"
