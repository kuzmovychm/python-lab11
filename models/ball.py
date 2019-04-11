from models.toy import Toy
from enums.size import Size


class Ball(Toy):

    def __init__(self, price=0, size=Size, toy_type=None, color="unknown"):

        if size == Size.SMALL:
            toy_type = "ball small"

        if size == Size.MEDIUM:
            toy_type = "ball medium"

        if size == Size.LARGE:
            toy_type = "ball large"

        super().__init__(price, size, toy_type)
        self.color = color

    def play(self):

        print("Playing with a", self.__class__.__name__)
