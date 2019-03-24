from models.toy import Toy
from models.size import Size


class Doll(Toy):

    def __init__(self, price=0, size=Size, toy_type=None, name="unknown"):

        if size == Size.SMALL:
            toy_type = "doll small"

        if size == Size.MEDIUM:
            toy_type = "doll medium"

        if size == Size.LARGE:
            toy_type = "doll large"

        super().__init__(price, size, toy_type)
        self.name = name

    def play(self):

        print("Playing with a", self.__class__.__name__)
