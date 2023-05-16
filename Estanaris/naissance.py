# This script is directly linked to naissance.html page
# "Naissance" means birth

# The players has to answer several questions in order the define the basics attribute and the profession of its
# character but also its alignment (if he is good/evil, lawful/chaotic)

def creation(player, choix):
    ancestre = choix.get('ancestre')
    print('Ancestre : ' + ancestre)
    player.increase_attribute(8, 'dv')
    if ancestre == 'Noble':
        player.increase_attribute(2, 'charisma')
        # ou sagesse
    elif ancestre == 'Riche':
        player.increase_attribute(2, 'intelligence')
        # ou dexte
    elif ancestre == 'Fidele':
        player.increase_attribute(2, 'wisdom')
        # ou charisme
    elif ancestre == 'Misere':
        player.increase_attribute(2, 'constitution')
        # ou force
    elif ancestre == 'Orc':
        player.increase_attribute(2, 'strength')
        # ou constit
    elif ancestre == 'Elf':
        player.increase_attribute(2, 'dexterity')
        # ou intell

    soclasse = choix.get('soclasse')
    player.soclasse = soclasse
    print('Soclasse : ' + soclasse)
    if soclasse == 'Aristocrate':
        player.increase_attribute(2, 'charisma')
        player.increase_attribute(2, 'strength')
    elif soclasse == 'Bourgeois':
        player.increase_attribute(2, 'intelligence')
        player.increase_attribute(2, 'dexterity')
    elif soclasse == 'Roturier':
        player.increase_attribute(2, 'wisdom')
        player.increase_attribute(2, 'constitution')

    classe = choix.get('classe')
    player.classe = classe
    print('Classe : ' + classe)

    reve = choix.get('reve')
    print('Reve : ' + reve)
    if reve == 'Renom' and ancestre != 'Noble':
        player.increase_attribute(2, 'charisma')
    elif reve == 'Renom' and ancestre == 'Noble':
        player.increase_attribute(2, 'wisdom')
    elif reve == 'Connaissance' and ancestre != 'Riche':
        player.increase_attribute(2, 'intelligence')
    elif reve == 'Connaissance' and ancestre == 'Riche':
        player.increase_attribute(2, 'dexterity')
    elif reve == 'Dieu' and ancestre != 'Fidele':
        player.increase_attribute(2, 'wisdom')
    elif reve == 'Dieu' and ancestre == 'Fidele':
        player.increase_attribute(2, 'charisma')
    elif reve == 'Vivre' and ancestre != 'Misere':
        player.increase_attribute(2, 'constitution')
    elif reve == 'Vivre' and ancestre == 'Misere':
        player.increase_attribute(2, 'strength')
    elif reve == 'Pouvoir' and ancestre != 'Orc':
        player.increase_attribute(2, 'strength')
    elif reve == 'Pouvoir' and ancestre == 'Orc':
        player.increase_attribute(2, 'constitution')
    elif reve == 'Libre' and ancestre != 'Elf':
        player.increase_attribute(2, 'dexterity')
    elif reve == 'Libre' and ancestre == 'Elf':
        player.increase_attribute(2, 'intelligence')


    for i in range(4):
        alignment = choix.get('alignement' + str(i))
        print('Alignement' + str(i) + ' : ' + str(alignment))
        if alignment == "L":
            player.increase_attribute(1, 'alignmentLC')
        if alignment == "C":
            player.decrease_attribute(1, 'alignmentLC')
        if alignment == "G":
            player.increase_attribute(1, 'alignmentGE')
        if alignment == "E":
            player.decrease_attribute(1, 'alignmentGE')

    alignmentLC = getattr(player, 'alignmentLC')
    print('alignmentLC : ' + str(alignmentLC))

    alignmentGE = getattr(player, 'alignmentGE')
    print('alignmentGE : ' + str(alignmentGE))

#     Profession calculation
#     Caster
    player.increase_attribute(1, 'loreI')
    if player.classe == 'Caster':
        player.increase_attribute(2, 'dexterity')
        if player.soclasse == 'Aristocrate':
            if player.alignmentGE >= 1 and (reve == 'Dieu' or ancestre == 'Fidele'):
                player.profession = 'Acolyte'
                player.spell_attribute = 'W'
                player.increase_attribute(4, 'wisdom')
                player.increase_attribute(2, 'intelligence')
                player.increase_attribute(1, 'religionW')
                player.increase_attribute(1, 'societyI')
                player.lores.append('scribing')
            else:
                player.profession = 'Apprenti Mage'
                player.spell_attribute = 'I'
                player.increase_attribute(2, 'wisdom')
                player.increase_attribute(4, 'intelligence')
                player.increase_attribute(1, 'arcanaI')
                player.increase_attribute(1, 'craftingI')
                player.lores.append('academia')
        elif player.soclasse == 'Bourgeois':
            if (player.alignmentGE >= 0 and player.alignmentLC >= 0) or (player.alignmentGE >= 1):
                player.profession = 'Acolyte'
                player.spell_attribute = 'W'
                player.increase_attribute(4, 'wisdom')
                player.increase_attribute(2, 'intelligence')
                player.increase_attribute(1, 'religionW')
                player.increase_attribute(1, 'societyI')
                player.lores.append('scribing')
            else:
            # elif player.alignmentGE <= 0 or (player.alignmentGE <= 0 and player.alignmentLC < 0):
                player.profession = 'Cultiste'
                player.spell_attribute = 'I'
                player.increase_attribute(2, 'charisma')
                player.increase_attribute(4, 'intelligence')
                player.increase_attribute(1, 'deceptionC')
                player.increase_attribute(1, 'occultismI')
                player.increase_attribute(1, 'religionW')
        elif player.soclasse == 'Roturier':
            if (player.alignmentGE >= 0 and player.alignmentLC >= 0) or (player.alignmentGE >= 1):
                player.profession = 'Pelerin'
                player.spell_attribute = 'W'
                player.increase_attribute(4, 'wisdom')
                player.increase_attribute(2, 'charisma')
                player.increase_attribute(1, 'religionW')
                player.increase_attribute(1, 'survivalW')
                player.increase_attribute(1, 'natureW')
            else:
            # elif player.alignmentGE <= 0 or (player.alignmentGE <= 0 and player.alignmentLC < 0):
                player.profession = 'Cultiste'
                player.spell_attribute = 'I'
                player.increase_attribute(2, 'charisma')
                player.increase_attribute(4, 'intelligence')
                player.increase_attribute(1, 'deceptionC')
                player.increase_attribute(1, 'occultismI')
                player.increase_attribute(1, 'religionW')
#   Fighter
    if player.classe == 'Fighter':
        player.increase_attribute(2, 'dexterity')
        player.increase_attribute(2, 'strength')
        if player.soclasse == 'Aristocrate':
            if player.alignmentLC >= 1:
                player.profession = 'Ecuyer'
                player.increase_attribute(2, 'strength')
                player.increase_attribute(2, 'constitution')
                player.increase_attribute(1, 'athleticsS')
                player.increase_attribute(1, 'societyI')
                player.lores.append('heraldry')
                player.lores.append('warfare')
            else:
                player.profession = 'Disciple Martial'
                player.increase_attribute(2, 'strength')
                player.increase_attribute(2, 'dexterity')
                player.increase_attribute(1, 'athleticsS')
                player.increase_attribute(1, 'acrobaticsD')
                player.lores.append('warfare')
        elif player.soclasse == 'Bourgeois':
            if player.alignmentLC >= 1:
                player.profession = 'Cavalier'
                player.increase_attribute(2, 'wisdom')
                player.increase_attribute(2, 'constitution')
                player.increase_attribute(1, 'athleticsS')
                player.increase_attribute(1, 'natureW')
                player.lores.append('plains')
            else:
                player.profession = 'Guerrier'
                player.increase_attribute(2, 'strength')
                player.increase_attribute(2, 'constitution')
                player.increase_attribute(1, 'athleticsS')
                player.increase_attribute(1, 'intimidationC')
                player.lores.append('warfare')
        elif player.soclasse == 'Roturier':
            if player.alignmentLC >= 1:
                player.profession = 'Garde'
                player.increase_attribute(2, 'wisdom')
                player.increase_attribute(2, 'constitution')
                player.increase_attribute(1, 'intimidationC')
                player.increase_attribute(1, 'diplomacyC')
                player.lores.append('legal')
            else:
                player.profession = 'Gladiateur'
                player.increase_attribute(2, 'strength')
                player.increase_attribute(2, 'charisma')
                player.increase_attribute(1, 'athleticsS')
                player.increase_attribute(1, 'performanceC')
                player.lores.append('warfare')
#   Expert
    if player.classe == 'Expert':
        player.increase_attribute(2, 'charisma')
        player.increase_attribute(2, 'intelligence')
        if player.soclasse == 'Aristocrate':
            if player.alignmentGE < 0:
                player.profession = "Collecteur d'Impots"
                player.increase_attribute(2, 'strength')
                player.increase_attribute(2, 'charisma')
                player.increase_attribute(1, 'intimidationC')
                player.increase_attribute(1, 'diplomacyC')
                player.lores.append('legal')
            else:
                player.profession = 'Noble'
                player.increase_attribute(2, 'intelligence')
                player.increase_attribute(2, 'charisma')
                player.increase_attribute(1, 'societyI')
                player.increase_attribute(1, 'diplomacyC')
                player.lores.append('heraldry')
        elif player.soclasse == 'Bourgeois':
            if player.alignmentLC >= 1 and player.alignmentGE < 1:
                player.profession = 'Juriste'
                player.increase_attribute(2, 'intelligence')
                player.increase_attribute(2, 'charisma')
                player.increase_attribute(1, 'societyI')
                player.increase_attribute(1, 'diplomacyC')
                player.lores.append('legal')
            elif player.alignmentLC < 0 and (reve == 'Renom' or 'Libre'):
                player.profession = 'Artiste'
                player.increase_attribute(2, 'dexterity')
                player.increase_attribute(2, 'charisma')
                player.increase_attribute(1, 'craftingI')
                player.increase_attribute(1, 'performanceC')
                player.lores.append('art')
            elif player.alignmentGE >= 1:
                player.profession = 'Medecin'
                player.increase_attribute(2, 'constitution')
                player.increase_attribute(2, 'wisdom')
                player.increase_attribute(1, 'medecineW')
                player.increase_attribute(1, 'craftingI')
                player.lores.append('midwifery')
            elif player.alignmentLC < 1 and (ancestre == 'Riche' or reve == 'Libre'):
                player.profession = 'Marchand'
                player.increase_attribute(2, 'intelligence')
                player.increase_attribute(2, 'charisma')
                player.increase_attribute(1, 'diplomacyC')
                player.increase_attribute(1, 'deceptionC')
                player.lores.append('mercantile')
            else:
                player.profession = 'Artisan'
                player.increase_attribute(2, 'intelligence')
                player.increase_attribute(2, 'strength')
                player.increase_attribute(1, 'athleticsS')
                player.increase_attribute(1, 'craftingI')
                player.lores.append('guild')
        elif player.soclasse == 'Roturier':
            if player.alignmentLC >= 1:
                player.profession = 'Eclaireur'
                player.increase_attribute(2, 'dexterity')
                player.increase_attribute(2, 'wisdom')
                player.increase_attribute(1, 'survivalW')
                player.lores.append('plains')
                player.lores.append('forest')
                player.lores.append('river')
                player.lores.append('mountain')
            elif player.alignmentLC < 0 and (reve == 'Renom' or 'Libre'):
                player.profession = 'Acrobate'
                player.increase_attribute(2, 'dexterity')
                player.increase_attribute(2, 'strength')
                player.increase_attribute(1, 'acrobaticsD')
                player.increase_attribute(1, 'performanceC')
                player.lores.append('circus')
            elif player.alignmentGE >= 1:
                player.profession = 'Herboriste'
                player.increase_attribute(2, 'constitution')
                player.increase_attribute(2, 'wisdom')
                player.increase_attribute(1, 'natureW')
                player.increase_attribute(1, 'craftingI')
                player.lores.append('herbalism')
            elif player.alignmentLC < 1 and (ancestre == 'Riche' or reve == 'Libre'):
                player.profession = 'Parieur'
                player.increase_attribute(2, 'dexterity')
                player.increase_attribute(2, 'charisma')
                player.increase_attribute(1, 'deceptionC')
                player.increase_attribute(1, 'stealthD')
                player.lores.append('games')
            else:
                player.profession = 'Enfant des rues'
                player.increase_attribute(2, 'dexterity')
                player.increase_attribute(2, 'constitution')
                player.increase_attribute(1, 'thieveryD')
                player.increase_attribute(1, 'stealthD')
                player.increase_attribute(1, 'survivalW')
