from functools import reduce


class Hero:
    def __init__(self, name, damage=0, hp=0):
        self.name = name
        self.damage = damage
        self.hp = hp


class Item:
    def __init__(self, name, damage=0, hp=0):
        self.name = name
        self.damage = damage
        self.hp = hp


Hero_list = {
    "pudge": Hero("pudge", damage=20, hp=2000),
    "phantom_assassin": Hero("phantom_assassin", damage=100, hp=500),
    "sven": Hero("sven", damage=50, hp=1000),
}

Item_list = {
    "satanic": Item("satanic", damage=20, hp=200),
    "divine_rapier": Item("divine_rapier", damage=300),
    "black_king_bar": Item("black_king_bar", damage=50, hp=100),
}


def get_choice(prompt, options):
    while True:
        try:
            choice = input(prompt).strip().lower()
            return options[choice]
        except KeyError:
            print("Invalid choice. Please try again!\n")


def aggregate_stats(objects):
    return reduce(lambda acc, obj: {
        "damage": acc["damage"] + obj.damage,
        "hp": acc["hp"] + obj.hp
    }, objects, {"damage": 0, "hp": 0})


hero = get_choice("Hero: ", Hero_list)
item = get_choice("Item: ", Item_list)

total_stats = aggregate_stats([hero, item])

print(f"\nDamage: {total_stats['damage']}")
print(f"Health: {total_stats['hp']}")
