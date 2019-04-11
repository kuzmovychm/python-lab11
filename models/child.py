from enums.age_group import AgeGroup


class Child:

    def __init__(self, name=None, age=None, parent_name=None):
        self.age = age
        self.name = name
        self.parent_name = parent_name

        if age is None:
            self.age_group = None
        elif age <= 6:
            self.age_group = AgeGroup.PRESCHOOLERS
        elif age <= 9:
            self.age_group = AgeGroup.SCHOOL_AGE_UNDER_9
        elif age <= 12:
            self.age_group = AgeGroup.SCHOOL_AGE_UNDER_12
        elif age <= 16:
            self.age_group = AgeGroup.YOUNG_TEENS

    def __str__(self):
        return str(self.name) + " , " + str(self.age) + " y.o."
