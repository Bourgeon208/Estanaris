class Item:
    def __init__(self, name, name_en, slot, price, bulk, description, item_category):
        self.name = name
        self.name_en = name_en
        self.slot = slot
        self.price = price
        self.bulk = bulk
        self.description = description
        self.item_category = item_category

class Weapon(Item):
    def __init__(self, name, name_en, slot, price, bulk, description, item_category, range, hands, damage, damage_type, traits, weapon_group,
                 weapon_category, reload):
        super().__init__(name, slot, price, bulk, description)
        self.name = name
        self.name_en = name_en
        self.slot = slot
        self.price = price
        self.bulk = bulk
        self.description = description
        self.range = range
        self.hands = hands
        self.damage = damage
        self.damage_type = damage_type
        self.traits = traits
        self.weapon_group = weapon_group
        self.weapon_category = weapon_category
        self.reload = reload
        self.item_category = item_category

class Armor(Item):
    def __init__(self, name, name_en, slot, price, bulk, description, item_category, armor_category, ac_bonus, dex_mod_cap, check_penalty,
                 strength, armor_group, traits):
        super().__init__(name, slot, price, bulk, description)
        self.name = name
        self.name_en = name_en
        self.slot = slot
        self.price = price
        self.bulk = bulk
        self.description = description
        self.armor_category = armor_category
        self.ac_bonus = ac_bonus
        self.dex_mod_cap = dex_mod_cap
        self.check_penalty = check_penalty
        self.strength = strength
        self.armor_group = armor_group
        self.traits = traits
        self.item_category = item_category

# class MagicItem(Item):
#     def __init__(self, name, slot, price, bulk, description, usable):
#
