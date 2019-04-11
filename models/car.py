from models.toy import Toy
from enums.size import Size


class Car(Toy):

    def __init__(self, price=0, size=Size, toy_type=None, car_type="unknown"):

        if size == Size.SMALL:
            toy_type = "car small"

        if size == Size.MEDIUM:
            toy_type = "car medium"

        if size == Size.LARGE:
            toy_type = "car large"

        super().__init__(price, size, toy_type)
        self.car_type = car_type

    def play(self):

        print("Playing with a", self.__class__.__name__)


