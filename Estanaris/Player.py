# This class defines all attributes of the player character
# It is not yet link to a database
class Player:
    def __init__(self):
        self.lv = 0
        self.name = ''
        self.classe = ''  # classe = profession's combat orientation
        self.profession = ''
        self.soclasse = ''

        # Abilities scores
        self.strength = 10
        self.dexterity = 10
        self.constitution = 10
        self.intelligence = 10
        self.wisdom = 10
        self.charisma = 10
        #

        self.hp = 1
        self.armor_classe = 10
        self.total_hp = 1
        self.dv = 0  # Des de Vie = accumulated hit points depending of the "classe"
        self.reflex = 0
        self.will = 0
        self.fortitude = 0
        self.attack = 0
        self.dex_attack = 0  # attack roll based on dexterity for ranged and finesse attacks
        self.xp = 1000  # it always take 1000xp points to level up
        self.alignmentLC = 0
        self.alignmentGE = 0
        self.class_dc = 10
        self.spell_attribute = None
        self.lores = []
        self.feats_magic = []
        self.feats_combat = []
        self.feats_skill = []

        # Skills
        # The last letter of each skill indicates its related abilities score (except Constitution)
        self.acrobaticsD = 0
        self.arcanaI = 0
        self.athleticsS = 0
        self.craftingI = 0
        self.deceptionC = 0
        self.diplomacyC = 0
        self.intimidationC = 0
        self.loreI = 0
        self.medecineW = 0
        self.natureW = 0
        self.occultismI = 0
        self.performanceC = 0
        self.religionW = 0
        self.societyI = 0
        self.stealthD = 0
        self.survivalW = 0
        self.thieveryD = 0
        #

    def level_up_check(self):
        if self.lv >= 1000:
            return True
        return False

    def level_up(self):
        if self.level_up_check():
            self.decrease_attribute(1000, 'xp')
            self.increase_attribute(1, 'lv')
            self.add_dv()
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

    def add_dv(self):
        if self.classe == 'Caster':
            self.increase_attribute(6, 'dv')
        elif self.classe == 'Expert':
            self.increase_attribute(8, 'dv')
        elif self.classe == 'Fighter':
            self.increase_attribute(10, 'dv')

    def calculate_total_hp(self):
        total_hp = self.dv + (((self.constitution - 10) % 2) * self.lv)
        return total_hp

    def calculate_skill(self, skill):
        if skill[-1] == 'S':
            attribute = self.strength
        elif skill[-1] == 'D':
            attribute = self.dexterity
        elif skill[-1] == 'I':
            attribute = self.intelligence
        elif skill[-1] == 'W':
            attribute = self.wisdom
        elif skill[-1] == 'C':
            attribute = self.charisma
        skill_bonus = (self.skill * 2) + ((attribute - 10) % 2) + self.lv
        return skill_bonus

    def calculate_alignement(self):
        alignement = ['Neutre', '']
        if self.alignmentLC >= 1:
            alignement[0] = 'Loyal'
        if self.alignmentLC <= -1:
            alignement[0] = 'Chaotique'

        if self.alignmentGE >= 1:
            alignement[1] = 'Bon'
        elif self.alignmentGE <= -1:
            alignement[1] = 'Mauvais'
        else:
            if alignement[0] == 'Neutre':
                alignement[1] = 'Strict'
            else:
                alignement[1] = 'Neutre'
        alignement = alignement[0] + ' ' + alignement[1]
        return alignement

    def increase_attribute(self, increase, attribute):
        setattr(self, attribute, getattr(self, attribute) + increase)

    def decrease_attribute(self, decrease, attribute):
        setattr(self, attribute, getattr(self, attribute) - decrease)
