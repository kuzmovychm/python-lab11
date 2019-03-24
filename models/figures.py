from models.toy import Toy
from models.size import Size


class Figures(Toy):

    def __init__(self, price=0, size=Size, toy_type=None, number=0, figures_type=None):

        if size == Size.SMALL:
            toy_type = "figures small"

        if size == Size.MEDIUM:
            toy_type = "figures medium"

        if size == Size.LARGE:
            toy_type = "figures large"

        super().__init__(price, size, toy_type)
        self.number = number
        self.figures_type = figures_type

    def play(self):

        print("Playing with a", self.__class__.__name__)
