class Hero:
    damage = 0
    hp = 0

    def __init__(self, damage=0, hp=0):
        self.__damage = damage
        self.__hp = hp

    def set_hero(self):
        Hero.damage = self.__damage
        Hero.hp = self.__hp


class Item:
    damage = 0
    hp = 0

    def __init__(self, damage=0, hp=0):
        self.__damage = damage
        self.__hp = hp

    def set_item(self):
        Item.damage = self.__damage
        Item.hp = self.__hp
