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



