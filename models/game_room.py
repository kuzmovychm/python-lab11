class GameRoom:

    def __init__(self, playground_area=0, present_children=0,
                 money_available=0, age_group="unknown", toys=[], children=[]):
        self.playground_area = playground_area
        self.present_children = present_children
        self.money_available = money_available
        self.age_group = age_group
        self.toys = toys
        self.children = children

    def add_child(self, child):

        if child in self.children:
            return
        elif self.calculate_free_places() > 0:
            if self.age_group == child.age_group:
                self.children.append(child)
        else:
            return

    def add_toy(self, toy):

        if toy in self.toys:
            return
        else:
            self.toys.append(toy)

    def remove_child(self, child):

        if child in self.children:
            self.children.remove(child)

    def calculate_maximal_number_of_places(self):

        return self.playground_area / 4

    def calculate_free_places(self):

        return self.calculate_maximal_number_of_places() - self.present_children
    