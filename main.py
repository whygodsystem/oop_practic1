from heros import *
from items import *


while True:
    try:
        hero = input("Hero: ").lower()
        Hero_list[hero].set_hero()
        break

    except KeyError:
        print("This hero invalid. Please try again!\n")

while True:
    try:
        item = input("Item: ").lower()
        Item_list[item].set_item()
        break

    except KeyError:
        print("This item invalid. Please try again!\n")

print(f"\nDamage: {Hero.damage + Item.damage}")
print(f"Health: {Hero.hp + Item.hp}")
