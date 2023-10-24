# This class defines all attributes of the player character
from flask import session

from ..db import get_db


class Player:
    def __init__(self):
        # In database stats (21)
        # NOT NULL
        self.lv = 0
        self.name = ''
        self.house = ''
        self.classe = ''  # classe = profession's combat orientation
        self.profession = ''
        self.profession_en = ''
        self.renown = 0
        self.reputation = 0
        self.alive = 1
        self.hp = 1
        self.xp = 1000  # it always takes 1000xp points to level up
        self.attributes_aggregated = '101010101010'
        self.skills_aggregated = '000000000000000000'
        self.dv = 0  # Des de Vie = accumulated hit points depends on the "classe"
        self.alignment_lc = 0
        self.alignment_ge = 0
        self.location = 'Aléhandre'
        # NULL AUTHORISED
        self.spell_attribute = None
        self.feats = []
        self.spells_known = []
        self.lores = []
        # End of the database stats

        # Abilities scores
        self.strength = 10
        self.dexterity = 10
        self.constitution = 10
        self.intelligence = 10
        self.wisdom = 10
        self.charisma = 10

        # Others stats
        self.soclasse = ''
        self.armor_classe = 10
        self.total_hp = 1
        self.reflex = 0
        self.will = 0
        self.fortitude = 0
        self.attack = 0
        self.dex_attack = 0  # attack roll based on dexterity for ranged and finesse attacks
        self.alignment = ['','']
        self.class_dc = 10
        self.feats_magic = []
        self.feats_combat = []
        self.feats_skill = []
        self.spells_available = []

        # Skills 17
        # The last letter of each skill indicates its related abilities score (except Constitution)
        self.skills = {
            'acrobaticsD' : 0,
            'arcanaI' : 0,
            'athleticsS' : 0,
            'craftingI' : 0,
            'deceptionC' : 0,
            'diplomacyC' : 0,
            'intimidationC' : 0,
            'loreI' : 0,
            'medecineW' : 0,
            'natureW' : 0,
            'occultismI' : 0,
            'performanceC' : 0,
            'religionW' : 0,
            'societyI' : 0,
            'stealthD' : 0,
            'survivalW' : 0,
            'thieveryD' : 0,
        }
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

    def calculate_attributes(self, from_where):
        if from_where == 'db':
            self.strength = int(self.attributes_aggregated[0:2])
            self.dexterity = int(self.attributes_aggregated[2:4])
            self.constitution = int(self.attributes_aggregated[4:6])
            self.intelligence = int(self.attributes_aggregated[6:8])
            self.wisdom = int(self.attributes_aggregated[8:10])
            self.charisma = int(self.attributes_aggregated[10:12])
        elif from_where == 'ch':
            self.attributes_aggregated = str(self.strength) + str(self.dexterity) + str(self.constitution) + \
                                         str(self.intelligence) + str(self.wisdom) + str(self.charisma)
        return
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

    def calculate_skills(self, from_where):
        if from_where == 'db':
            i = 0
            for skill in self.skills:
                self.skills[skill] = int(self.skills_aggregated[i])
                i += 1
        elif from_where == 'ch':
            i = 0
            for skill in self.skills:
                self.skills_aggregated[i] = str(self.skills[skill] )
                i += 1
        return

    def calculate_skill(self, skill, skill_value):
        attribute = 0
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
        skill_bonus = (skill_value * 2) + ((attribute - 10) % 2) + self.lv
        return skill_bonus

    def calculate_skill_all(self):
        return


    def calculate_alignement(self, language):
        alignement = ['','']
        if language == 'fr' :
            alignement = ['Neutre', '']
            if self.alignment_lc >= 1:
                alignement[0] = 'Loyal'
            if self.alignment_lc <= -1:
                alignement[0] = 'Chaotique'

            if self.alignment_ge >= 1:
                alignement[1] = 'Bon'
            elif self.alignment_ge <= -1:
                alignement[1] = 'Mauvais'
            else:
                if alignement[0] == 'Neutre':
                    alignement[1] = 'Strict'
                else:
                    alignement[1] = 'Neutre'
        elif language == 'en':
            alignement = ['Neutral', '']
            if self.alignment_lc >= 1:
                alignement[0] = 'Lawful'
            if self.alignment_lc <= -1:
                alignement[0] = 'Chaotic'

            if self.alignment_ge >= 1:
                alignement[1] = 'Good'
            elif self.alignment_ge <= -1:
                alignement[1] = 'Evil'
            else:
                if alignement[0] == 'Neutral':
                    alignement[0] = 'True'
                    alignement[1] = 'Neutral'
                else:
                    alignement[1] = 'Neutral'
        alignement = alignement[0] + ' ' + alignement[1]
        return alignement

    def calculate_all(self, language):
        # From calculation
        self.calculate_attributes('db')
        self.calculate_skills('db')
        self.armor_classe = self.calculate_armor_class()
        self.will = self.calculate_save('will')
        self.reflex = self.calculate_save('reflex')
        self.fortitude = self.calculate_save('fortitude')
        self.alignment = self.calculate_alignement(language)
        self.attack = self.calculate_attack()
        self.dex_attack = self.calculate_dex_attack()
        self.total_hp = self.calculate_total_hp()
        return

    def increase_skill(self, increase, skill):
        self.skills[skill] += increase
    def decrease_skill(self, decrease, skill):
        self.skills[skill] += decrease

    def increase_attribute(self, increase, attribute):
        setattr(self, attribute, getattr(self, attribute) + increase)

    def decrease_attribute(self, decrease, attribute):
        setattr(self, attribute, getattr(self, attribute) - decrease)

    def initialize(self, temp_character, language):
        # From database
        self.lv = temp_character['lv']
        self.name = temp_character['name']
        self.house = temp_character['house']
        self.classe = temp_character['classe']
        self.profession = temp_character['profession']
        self.profession_en = temp_character['profession_en']
        self.renown = temp_character['renown']
        self.reputation = temp_character['reputation']
        self.alive = 1
        self.hp = temp_character['hp']
        self.xp = temp_character['xp']
        self.attributes_aggregated = temp_character['attribute']
        self.skills_aggregated = temp_character['skills']
        self.dv = temp_character['dv']
        self.alignment_lc = temp_character['alignment_lc']
        self.alignment_ge = temp_character['alignment_ge']
        self.location = temp_character['location']
        self.spell_attribute = temp_character['spell_attribute']
        self.feats = temp_character['feats']
        self.spells_known = temp_character['spells_known']
        self.lores = temp_character['lores']
        self.calculate_all(language)
        return None

    def db_save_character(self):
        self.calculate_attributes('ch')
        self.calculate_skills('ch')
        user_id = session.get('user_id')
        db = get_db()
        try:
            db.execute(
                "UPDATE character "
                "SET "
                "(alive, attribute, profession, profession_en, xp, alignment_lc, alignment_ge, "
                "location, lv, hp, skills, classe, renown, reputation, dv) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (getattr(self, 'alive'), getattr(self, 'attributes_aggregated'), getattr(self, 'profession'),
                 getattr(self, 'profession_en'), getattr(self, 'xp'), getattr(self, 'alignment_lc'),
                 getattr(self, 'alignment_ge'), getattr(self, 'location'), getattr(self, 'lv'),
                 getattr(self, 'hp'), getattr(self, 'skills_aggregated'), getattr(self, 'classe'),
                 getattr(self, 'renown'), getattr(self, 'reputation'), getattr(self, 'dv')),
                "WHERE (user_id = ? AND alive = 1)", (user_id,)
            )
            db.commit()
        except Exception as e:
            print(e)
        return

    def db_character_create(self, user_id, cname, chouse_name):
        db = get_db()
        db.execute(
            "INSERT INTO character "
            "(user_id, alive, name, house, attribute, profession, profession_en, xp, alignment_lc, alignment_ge, "
            "location, lv, hp, skills, classe, renown, reputation, dv) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (user_id, getattr(self, 'alive'), cname, chouse_name,
             getattr(self, 'attributes_aggregated'), getattr(self, 'profession'),
             getattr(self, 'profession_en'), getattr(self, 'xp'), getattr(self, 'alignment_lc'),
             getattr(self, 'alignment_ge'), getattr(self, 'location'), getattr(self, 'lv'),
             getattr(self, 'hp'), getattr(self, 'skills_aggregated'), getattr(self, 'classe'),
             getattr(self, 'renown'), getattr(self, 'reputation'), getattr(self, 'dv'))
        )
        db.commit()
        return