from models.game_room import GameRoom
from models.toy import Toy


class GameRoomManager:

    def __init__(self, game_rooms=[]):

        self.game_rooms = game_rooms

    def add_game_room(self, game_room=None):

        if game_room in self.game_rooms:
            return

        else:
            self.game_rooms.append(game_room)

    def buy_toy(self, game_room=GameRoom, toy=Toy):

        if game_room.money_available > toy.price:

            game_room.toys.append(toy)
            game_room.money_available -= toy.price

        else:

            print("not enough money to buy", toy.__class__.__name__)

    def sort_toys_by_price(self, game_room=GameRoom(), ascending=True):

        if ascending:
            game_room.toys.sort(key=lambda toy: toy.price, reverse=False)

        else:
            game_room.toys.sort(key=lambda toy: toy.price, reverse=True)

        return game_room.toys

    def sort_toys_by_type(self, game_room=GameRoom(), ascending=True):

        if ascending:
            game_room.toys.sort(key=lambda toy: toy.toy_type, reverse=False)

        else:
            game_room.toys.sort(key=lambda toy: toy.toy_type, reverse=True)

        return game_room.toys
