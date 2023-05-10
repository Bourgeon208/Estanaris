class Player:
    def __init__(self):
        self.lv = 0
        self.name = ''
        self.classe = ''
        self.profession = ''
        self.soclasse = ''
        self.strength = 10
        self.dexterity = 10
        self.constitution = 10
        self.intelligence = 10
        self.wisdom = 10
        self.charisma = 10
        self.hp = 1
        self.armor_classe = 10
        self.total_hp = 1
        self.dv = 0
        self.reflex = 0
        self.will = 0
        self.fortitude = 0
        self.attack = 0
        self.dex_attack = 0
        self.xp = 1000
        self.alignmentLC = 0
        self.alignmentGE = 0
        self.spell_attribute = None
        self.lores = []
        self.feats = {
            'magic': [],
            'combat': [],
            'skill': []
        }
        self.skills = {
            'acrobatics': 0,
            'arcana': 0,
            'athletics': 0,
            'crafting': 0,
            'deception': 0,
            'diplomacy': 0,
            'intimidation': 0,
            'lore': 0,
            'medecine': 0,
            'nature': 0,
            'occultism': 0,
            'performance': 0,
            'religion': 0,
            'society': 0,
            'stealth': 0,
            'survival': 0,
            'thievery': 0,
        }

    def level_up_check(self):
        if self.lv >= 1000:
            return True
        return False

    def level_up(self):
        if self.level_up_check():
            self.decrease_attribute(1000, 'xp')
            self.increase_attribute(1, 'lv')
            self.attack = self.calculate_attack()
            self.dex_attack = self.calculate_dex_attack()
            self.reflex = self.calculate_save('reflex')
            self.will = self.calculate_save('will')
            self.fortitude = self.calculate_save('fortitude')
            self.total_hp = self.calculate_total_hp()

    def calculate_save(self, roll):
        attribute = 0
        if roll == 'reflex':
            attribute = ((self.dexterity - 10) % 2)
        if roll == 'will':
            attribute = ((self.wisdom - 10) % 2)
        if roll == 'fortitude':
            attribute = ((self.constitution - 10) % 2)
        save = self.lv + attribute
        return save

    def calculate_armor_class(self):
        AC = 10 + self.lv + ((self.dexterity - 10) % 2)
        return AC

    def calculate_attack(self):
        attack = self.lv + ((self.strength - 10) % 2)
        return attack

    def calculate_dex_attack(self):
        dex_attack = self.lv + ((self.dexterity - 10) % 2)
        return dex_attack

    def calculate_total_hp(self):
        total_hp = self.dv + (((self.constitution - 10) % 2) * self.lv)
        return total_hp

    # def increase_attribute(self, increase, attribute):
    #     self.attribute += increase
    def increase_attribute(self, increase, attribute):
        setattr(self, attribute, getattr(self, attribute) + increase)

    def decrease_attribute(self, decrease, attribute):
        setattr(self, attribute, getattr(self, attribute) - decrease)

