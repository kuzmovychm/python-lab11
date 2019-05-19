from managers.game_room_manager import GameRoomManager
from models.game_room import GameRoom
from enums.size import Size
from models.ball import Ball
from models.car import Car
from models.doll import Doll
from models.figures import Figures
from models.child import Child
from enums.age_group import AgeGroup


manager = GameRoomManager()
game_room = GameRoom(money_available=12000, age_group=AgeGroup.SCHOOL_AGE_UNDER_12, playground_area=124)


# Checking sorting

ball = Ball(price=100, size=Size.SMALL)
car = Car(price=80, size=Size.SMALL)
doll = Doll(price=140, size=Size.SMALL)
figures = Figures(price=90, size=Size.SMALL)

manager.buy_toy(game_room, ball)
manager.buy_toy(game_room, car)
manager.buy_toy(game_room, doll)
manager.buy_toy(game_room, figures)

toys = game_room.toys
print("\there are all toys in game room:")
for toy in toys:
    print(str(toys.index(toy) + 1) + ". " + str(toy))
print("\n")

manager.sort_toys_by_price(game_room, True)
print("\ttoys sorted by price by ascending:")
for toy in toys:
    print(str(toys.index(toy) + 1) + ". " + str(toy))
print("\n")

manager.sort_toys_by_price(game_room, False)
print("\ttoys sorted by price by descending:")
for toy in toys:
    print(str(toys.index(toy) + 1) + ". " + str(toy))
print("\n")

manager.sort_toys_by_type(game_room, True)
print("\ttoys sorted by type by ascending:")
for toy in toys:
    print(str(toys.index(toy) + 1) + ". " + str(toy))
print("\n")

manager.sort_toys_by_type(game_room, False)
print("\ttoys sorted by type by descending:")
for toy in toys:
    print(str(toys.index(toy) + 1) + ". " + str(toy))
print("\n")

# Checking whether removing a child works correctly

Max = Child(name="Max", age=10, parent_name="Oksana")
Vitos = Child(name="Vitos", age=11)
Andriy = Child(name="Andriy", age=9)

game_room.add_child(Max)
game_room.add_child(Vitos)
game_room.add_child(Andriy)

print("present children in game room:")
for child in game_room.children:
    print(str(game_room.children.index(child) + 1) + ". " + str(child))
print("\n")

print("removing Max ...")
game_room.remove_child(Max)
print("\n")

print("present children in game room:")
for child in game_room.children:
    print(str(game_room.children.index(child) + 1) + ". " + str(child))

print("removing Vitos ...")
game_room.remove_child(Vitos)
print("\n")

print("present children in game room:")
for child in game_room.children:
    print(str(game_room.children.index(child) + 1) + ". " + str(child))
