# This script is directly linked to naissance.html page
# "Naissance" means birth

# The players has to answer several questions in order the define the basics attribute and the profession of its
# character but also its alignment (if he is good/evil, lawful/chaotic)
from PIL import Image
import random
def creation(player, choix):
    player.location = 'Aléhandre'
    ancestre = choix.get('ancestre')
    print('Ancestre : ' + ancestre)
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
            player.increase_attribute(1, 'alignment_lc')
        if alignment == "C":
            player.decrease_attribute(1, 'alignment_lc')
        if alignment == "G":
            player.increase_attribute(1, 'alignment_ge')
        if alignment == "E":
            player.decrease_attribute(1, 'alignment_ge')

    alignment_lc = getattr(player, 'alignment_lc')
    print('alignment_lc : ' + str(alignment_lc))

    alignment_ge = getattr(player, 'alignment_ge')
    print('alignment_ge : ' + str(alignment_ge))

#     Profession calculation
#     Caster
    player.increase_attribute(1, 'loreI')
    if player.classe == 'Caster':
        player.increase_attribute(6, 'dv')
        player.increase_attribute(2, 'dexterity')
        r = random.randint(1, 5)
        print('RDN INT : ' + str(r))
        if (reve == 'Connaissance') and alignment_lc < 2 and r > 3:
            player.profession = 'Cherche-Sorts'
            player.profession_en = 'Spell Seeker'
            player.spell_attribute = 'I'
            player.increase_attribute(2, 'wisdom')
            player.increase_attribute(4, 'intelligence')
            player.increase_attribute(1, 'arcanaI')
            player.increase_attribute(1, 'occultismI')
            player.lores.append('library')
        elif player.soclasse == 'Aristocrate':
            if player.alignment_ge >= 1 and (reve == 'Dieu' or ancestre == 'Fidele'):
                player.profession = 'Acolyte'
                player.profession_en = 'Acolyte'
                player.spell_attribute = 'W'
                player.increase_attribute(4, 'wisdom')
                player.increase_attribute(2, 'intelligence')
                player.increase_attribute(1, 'religionW')
                player.increase_attribute(1, 'societyI')
                player.lores.append('scribing')
            else:
                player.profession = 'Apprenti Mage'
                player.profession_en = 'Student of Magic'
                player.spell_attribute = 'I'
                player.increase_attribute(2, 'wisdom')
                player.increase_attribute(4, 'intelligence')
                player.increase_attribute(1, 'arcanaI')
                player.increase_attribute(1, 'craftingI')
                player.lores.append('academia')
        elif player.soclasse == 'Bourgeois':
            if (player.alignment_ge >= 0 and player.alignment_lc >= 0) or (player.alignment_ge >= 1):
                player.profession = 'Acolyte'
                player.profession_en = 'Acolyte'
                player.spell_attribute = 'W'
                player.increase_attribute(4, 'wisdom')
                player.increase_attribute(2, 'intelligence')
                player.increase_attribute(1, 'religionW')
                player.increase_attribute(1, 'societyI')
                player.lores.append('scribing')
            else:
            # elif player.alignment_ge <= 0 or (player.alignment_ge <= 0 and player.alignment_lc < 0):
                player.profession = 'Cultiste'
                player.profession_en = 'Cultist'
                player.spell_attribute = 'I'
                player.increase_attribute(2, 'charisma')
                player.increase_attribute(4, 'intelligence')
                player.increase_attribute(1, 'deceptionC')
                player.increase_attribute(1, 'occultismI')
                player.increase_attribute(1, 'religionW')
        elif player.soclasse == 'Roturier':
            if (player.alignment_ge >= 0 and player.alignment_lc >= 0) or (player.alignment_ge >= 1):
                player.profession = 'Pèlerin'
                player.profession_en = 'Pilgrim'
                player.spell_attribute = 'W'
                player.increase_attribute(4, 'wisdom')
                player.increase_attribute(2, 'charisma')
                player.increase_attribute(1, 'religionW')
                player.increase_attribute(1, 'survivalW')
                player.increase_attribute(1, 'natureW')
            else:
            # elif player.alignment_ge <= 0 or (player.alignment_ge <= 0 and player.alignment_lc < 0):
                player.profession = 'Cultiste'
                player.profession_en = 'Cultist'
                player.spell_attribute = 'I'
                player.increase_attribute(2, 'charisma')
                player.increase_attribute(4, 'intelligence')
                player.increase_attribute(1, 'deceptionC')
                player.increase_attribute(1, 'occultismI')
                player.increase_attribute(1, 'religionW')
#   Fighter
    if player.classe == 'Fighter':
        player.increase_attribute(10, 'dv')
        player.increase_attribute(2, 'dexterity')
        player.increase_attribute(2, 'strength')
        if player.alignment_lc < 0 and player.alignment_ge < 0 and (reve == 'Libre' or reve == 'Pouvoir'):
            player.profession = 'Bandit'
            player.profession_en = 'Bandit'
            player.increase_attribute(2, 'dexterity')
            player.increase_attribute(2, 'charisma')
            player.increase_attribute(1, 'intimidationC')
            player.increase_attribute(1, 'stealthD')
            player.increase_attribute(1, 'survivalW')
        elif player.soclasse == 'Aristocrate':
            if player.alignment_lc >= 1:
                player.profession = 'Ecuyer'
                player.profession_en = 'Squire'
                player.increase_attribute(2, 'strength')
                player.increase_attribute(2, 'constitution')
                player.increase_attribute(1, 'athleticsS')
                player.increase_attribute(1, 'societyI')
                player.lores.append('heraldry')
                player.lores.append('warfare')
            else:
                player.profession = 'Disciple Martial'
                player.profession_en = 'Martial Disciple'
                player.increase_attribute(2, 'strength')
                player.increase_attribute(2, 'dexterity')
                player.increase_attribute(1, 'athleticsS')
                player.increase_attribute(1, 'acrobaticsD')
                player.lores.append('warfare')
        elif player.soclasse == 'Bourgeois':
            if player.alignment_lc >= 1:
                player.profession = 'Cavalier'
                player.profession_en = 'Outrider'
                player.increase_attribute(2, 'wisdom')
                player.increase_attribute(2, 'constitution')
                player.increase_attribute(1, 'athleticsS')
                player.increase_attribute(1, 'natureW')
                player.lores.append('plains')
            else:
                player.profession = 'Guerrier'
                player.profession_en = 'Warrior'
                player.increase_attribute(2, 'strength')
                player.increase_attribute(2, 'constitution')
                player.increase_attribute(1, 'athleticsS')
                player.increase_attribute(1, 'intimidationC')
                player.lores.append('warfare')
        elif player.soclasse == 'Roturier':
            if player.alignment_lc >= 1:
                player.profession = 'Garde'
                player.profession_en = 'Guard'
                player.increase_attribute(2, 'wisdom')
                player.increase_attribute(2, 'constitution')
                player.increase_attribute(1, 'intimidationC')
                player.increase_attribute(1, 'diplomacyC')
                player.lores.append('legal')
            elif player.alignment_lc < 0 and (ancestre == 'Orc' or (reve == 'Pouvoir' or reve == 'Libre')):
                player.profession = 'Barbare'
                player.profession_en = 'Barbarian'
                player.increase_attribute(2, 'strength')
                player.increase_attribute(2, 'constitution')
                player.increase_attribute(1, 'athleticsS')
                player.increase_attribute(1, 'survivalW')
                player.lores.append('plains')
            else:
                player.profession = 'Gladiateur'
                player.profession_en = 'Gladiator'
                player.increase_attribute(2, 'strength')
                player.increase_attribute(2, 'charisma')
                player.increase_attribute(1, 'athleticsS')
                player.increase_attribute(1, 'performanceC')
                player.lores.append('warfare')
#   Expert
    if player.classe == 'Expert':
        player.increase_attribute(8, 'dv')
        player.increase_attribute(2, 'charisma')
        player.increase_attribute(2, 'intelligence')
        if player.soclasse == 'Aristocrate':
            if player.alignment_ge < 0:
                player.profession = 'Percepteur'
                player.profession_en = 'Tax Collector'
                player.increase_attribute(2, 'strength')
                player.increase_attribute(2, 'charisma')
                player.increase_attribute(1, 'intimidationC')
                player.increase_attribute(1, 'diplomacyC')
                player.lores.append('legal')
            else:
                player.profession = 'Noble'
                player.profession_en = 'Noble'
                player.increase_attribute(2, 'intelligence')
                player.increase_attribute(2, 'charisma')
                player.increase_attribute(1, 'societyI')
                player.increase_attribute(1, 'diplomacyC')
                player.lores.append('heraldry')
        elif player.soclasse == 'Bourgeois':
            if player.alignment_lc >= 1 and player.alignment_ge < 1:
                player.profession = 'Juriste'
                player.profession_en = 'Barrister'
                player.increase_attribute(2, 'intelligence')
                player.increase_attribute(2, 'charisma')
                player.increase_attribute(1, 'societyI')
                player.increase_attribute(1, 'diplomacyC')
                player.lores.append('legal')
            elif player.alignment_lc < 0 and (reve == 'Renom' or reve == 'Libre'):
                player.profession = 'Artiste'
                player.profession_en = 'Artist'
                player.increase_attribute(2, 'dexterity')
                player.increase_attribute(2, 'charisma')
                player.increase_attribute(1, 'craftingI')
                player.increase_attribute(1, 'performanceC')
                player.lores.append('art')
            elif player.alignment_ge >= 1:
                player.profession = 'Médecin'
                player.profession_en = 'Healer'
                player.increase_attribute(2, 'dexterity')
                player.increase_attribute(2, 'wisdom')
                player.increase_attribute(1, 'medecineW')
                player.increase_attribute(1, 'craftingI')
                player.lores.append('midwifery')
            elif player.alignment_lc < 1 and (ancestre == 'Riche' or reve == 'Libre'):
                player.profession = 'Marchand'
                player.profession_en = 'Physician'
                player.increase_attribute(2, 'intelligence')
                player.increase_attribute(2, 'charisma')
                player.increase_attribute(1, 'diplomacyC')
                player.increase_attribute(1, 'deceptionC')
                player.lores.append('mercantile')
            else:
                player.profession = 'Artisan'
                player.profession_en = 'Artisan'
                player.increase_attribute(2, 'intelligence')
                player.increase_attribute(2, 'strength')
                player.increase_attribute(1, 'athleticsS')
                player.increase_attribute(1, 'craftingI')
                player.lores.append('guild')
        elif player.soclasse == 'Roturier':
            if player.alignment_lc >= 1:
                player.profession = 'Eclaireur'
                player.profession_en = 'Scout'
                player.increase_attribute(2, 'dexterity')
                player.increase_attribute(2, 'wisdom')
                player.increase_attribute(1, 'survivalW')
                player.lores.append('plains')
                player.lores.append('forest')
                player.lores.append('river')
                player.lores.append('mountain')
            elif player.alignment_lc < 0 and (reve == 'Renom' or reve == 'Libre'):
                player.profession = 'Acrobate'
                player.profession_en = 'Acrobat'
                player.increase_attribute(2, 'dexterity')
                player.increase_attribute(2, 'strength')
                player.increase_attribute(1, 'acrobaticsD')
                player.increase_attribute(1, 'performanceC')
                player.lores.append('circus')
            elif player.alignment_ge >= 1:
                player.profession = 'Herboriste'
                player.profession_en = 'Herbalist'
                player.increase_attribute(2, 'constitution')
                player.increase_attribute(2, 'wisdom')
                player.increase_attribute(1, 'natureW')
                player.increase_attribute(1, 'craftingI')
                player.lores.append('herbalism')
            elif player.alignment_lc < 1 and (ancestre == 'Riche' or reve == 'Libre'):
                player.profession = 'Parieur'
                player.profession_en = 'Gambler'
                player.increase_attribute(2, 'dexterity')
                player.increase_attribute(2, 'charisma')
                player.increase_attribute(1, 'deceptionC')
                player.increase_attribute(1, 'stealthD')
                player.lores.append('games')
            else:
                player.profession = 'Enfant des Rues'
                player.profession_en = 'Street Urchin'
                player.increase_attribute(2, 'dexterity')
                player.increase_attribute(2, 'constitution')
                player.increase_attribute(1, 'thieveryD')
                player.increase_attribute(1, 'stealthD')
                player.increase_attribute(1, 'survivalW')

def final_creation(player, choix):
    attribut = choix.get('attribut')
    print('Attribut : ' + attribut)
    player.increase_attribute(8, 'dv')
    if attribut == 'Force':
        player.increase_attribute(2, 'strength')
    elif attribut == 'Dexterite':
        player.increase_attribute(2, 'dexterity')
    elif attribut == 'Constitution':
        player.increase_attribute(2, 'constitution')
    elif attribut == 'Intelligence':
        player.increase_attribute(2, 'intelligence')
    elif attribut == 'Sagesse':
        player.increase_attribute(2, 'wisdom')
    elif attribut == 'Charisme':
        player.increase_attribute(2, 'charisma')

def profession_description(prof, language):
    description = ''
    if language == 'fr' :
        if prof == 'Acolyte':
            description = 'Vous avez passé vos premiers jours dans un monastère religieux ou un couvent. Vous avez ' \
                          'peut-être voyagé à travers le monde pour diffuser le message de votre religion ou parce ' \
                          'que vous avez rejeté les enseignements de votre foi, mais au fond de vous, vous porterez ' \
                          'toujours avec vous les leçons que vous avez apprises.'
        elif prof == 'Acrobate':
            description = 'Dans un cirque ou dans les rues, vous gagniez votre salaire en vous produisant en tant ' \
                          'qu\'acrobate. Lorsque l\'argent s\'est fait rare, vous avez peut-être choisi de vous tourner ' \
                          'vers l\'aventure ou simplement décidé de mettre vos compétences à meilleur escient.'
        elif prof == 'Apprenti Mage':
            description = 'Vous êtes actuellement inscrit à l\'école de magie de Pelagius où vous apprenez les fondements de ' \
                          'la magie arcanique. Que vos aventures se déroulent pendant les pauses entre les semestres, dans ' \
                          'le cadre d\'un programme d\'études rémunéré, ou même au sein des couloirs de l\'académie ' \
                          'elle-même, vous devrez apprendre à jongler entre votre double vie.'
        elif prof == 'Artisan':
            description = 'En tant qu\'apprenti, vous pratiquiez une forme particulière de construction ou d\'artisanat, ' \
                          'développant des compétences spécialisées. Vous auriez pu être l\'apprenti d\'un forgeron ' \
                          'travaillant dur à la forge pendant des heures innombrables, un jeune tailleur cousant des ' \
                          'vêtements de toutes sortes, ou un charpentier de marine donnant forme aux coques de navires.'
        elif prof == 'Artiste':
            description = 'Votre art est votre plus grande passion, quelle que soit sa forme. L\'aventure pourrait vous ' \
                          'aider à trouver l\'inspiration ou simplement être un moyen de subsistance jusqu\'à ce que vous ' \
                          'deveniez un artiste mondialement célèbre.'
        elif prof == 'Bandit':
            description = 'Votre passé est loin d\'être exempt de brigandage rural, volant les voyageurs sur la route et ' \
                          'vous débrouillant comme vous le pouviez. Que votre brigandage ait été autorisé par un noble' \
                          ' local ou que vous l\'ayez fait de votre propre chef, vous vous êtes finalement lancé dans ' \
                          'la vie d\'aventurier. Désormais, l\'aventure est votre gagne-pain, et des années de camping ' \
                          'et de combats ne vous ont fait que progresser davantage.'
        elif prof == 'Barbare':
            description = 'En parcourant les contrées lointaines et variées, vous avez acquis les tactiques de base pour ' \
                          'survivre sur la route et dans des terres inconnues, vous débrouillant avec peu de provisions ' \
                          'et encore moins de confort. En tant qu\'aventurier, vous continuez de voyager, souvent vers ' \
                          'des endroits encore plus dangereux.'
        elif prof == 'Cavalier':
            description = 'Dans votre jeunesse, vous galopiez à cheval sur de vastes prairies, servant d\'avant-garde à ' \
                          'votre établissement, à une armée ou à un autre groupe. Le fait de voir tant de terres ' \
                          'différentes a éveillé en vous une soif d\'aventure et d\'exploration du monde plutôt que de ' \
                          'simplement le traverser à toute allure.'
        elif prof == 'Cherche-Sorts':
            description = 'La magie conventionnelle ne peut captiver votre attention que pendant un certain temps. ' \
                          'À la place, vous vous êtes consacré à la compréhension de sorts vraiment particuliers, ' \
                          'ce qui vous pousse invariablement à explorer le monde et toutes ses traditions ésotériques.'
        elif prof == 'Cultiste':
            description = 'Vous étiez (ou êtes toujours) membre d\'une secte dont les rituels peuvent impliquer des ' \
                          'danses sacrées pour assurer une récolte abondante ou des rituels sinistres qui invoquent des ' \
                          'forces obscures. Vous avez peut-être entrepris des aventures pour promouvoir les objectifs de ' \
                          'votre culte, vous initier aux mystères plus grands du monde ou fuir des pratiques ou ' \
                          'des contraintes peu recommandables.'
        elif prof == 'Disciple Martial':
            description = 'Vous vous êtes consacré à un entraînement intensif et à des études rigoureuses pour devenir un' \
                          ' grand guerrier. L\'école à laquelle vous avez fréquenté aurait pu être un monastère ' \
                          'traditionaliste, une académie militaire d\'élite ou la succursale locale d\'une prestigieuse ' \
                          'organisation de mercenaires.'
        elif prof == 'Eclaireur':
            description = 'Vous considériez la nature sauvage comme votre foyer alors que vous trouviez des sentiers et ' \
                          'guidiez les voyageurs. Votre soif d\'aventure aurait pu vous attirer vers la vie d\'aventurier, ' \
                          'ou peut-être avez-vous servi d\'éclaireur pour les soldats et avez découvert que vous aimiez ' \
                          'le combat.'
        elif prof == 'Ecuyer':
            description = 'Vous vous êtes entraîné aux côtés d\'un chevalier, en entretenant son équipement et en le ' \
                          'soutenant lors des tournois et des batailles. Maintenant, vous cherchez un défi qui prouvera ' \
                          'que vous êtes digne de devenir un chevalier à part entière, ou bien vous avez dédaigné les fastes' \
                          ' et les cérémonies pour vous tester dans des combats honnêtes, bien que moins formels. '
        elif prof == 'Enfant des Rues':
            description = 'Vous vous débrouilliez pour survivre en volant dans les poches dans les rues d\'une grande ' \
                          'ville, ne sachant jamais où vous trouveriez votre prochain repas. Alors que certaines ' \
                          'personnes s\'engagent dans l\'aventure pour la gloire, vous le faites simplement pour survivre.'
        elif prof == 'Garde':
            description = 'Vous avez servi dans la garde, par patriotisme ou par nécessité financière. Quoi qu\'il en soit, ' \
                          'vous savez comment faire parler un suspect récalcitrant. Peu importe la raison pour laquelle ' \
                          'vous avez quitté la garde, vous considérez peut-être l\'aventure comme un moyen d\'utiliser ' \
                          'vos compétences sur une scène plus vaste.'
        elif prof == 'Gladiateur':
            description = 'Les jeux sanglants de l\'arène vous ont enseigné l\'art du combat. Avant d\'atteindre la ' \
                          'véritable renommée, vous avez quitté - ou vous êtes échappé - l\'arène pour explorer le monde. ' \
                          'Votre habileté à faire couler le sang et à attirer l\'attention de la foule porte ses fruits ' \
                          'dans cette nouvelle vie d\'aventurier.'
        elif prof == 'Guerrier':
            description = 'Dans votre jeunesse, vous vous êtes lancé dans la bataille en tant que mercenaire, guerrier ' \
                          'défendant un peuple nomade, ou membre d\'une milice ou d\'une armée. Vous auriez peut-être ' \
                          'voulu vous émanciper de la structure rigide de ces forces, ou vous avez toujours été un ' \
                          'guerrier indépendant comme vous l\'êtes maintenant.'
        elif prof == 'Herboriste':
            description = 'En tant qu\'apothicaire formé ou praticien rural de médecine populaire, vous avez appris les ' \
                          'propriétés curatives de diverses herbes. Vous êtes doué pour collecter les bons remèdes ' \
                          'naturels dans tous types d\'environnements et les préparer correctement.'
        elif prof == 'Juriste':
            description = 'Des piles de manuels de droit, des enseignants sévères et une expérience dans les salles ' \
                          'd\'audience vous ont instruit dans les affaires juridiques. Vous êtes capable de monter ' \
                          'une accusation ou une défense devant un tribunal, et vous avez tendance à vous tenir au ' \
                          'courant des lois locales, car on ne sait jamais quand vous pourriez avoir besoin de les ' \
                          'connaître rapidement.'
        elif prof == 'Marchand':
            description = 'Dans une boutique poussiéreuse, un étal de marché ou une caravane de marchands, vous ' \
                          'marchandiez des marchandises contre de l\'argent et des biens d\'échange. Les compétences ' \
                          'que vous avez acquises sont toujours utiles dans la vie d\'aventurier, où une bonne affaire ' \
                          'sur une armure pourrait vous éviter la mort.'
        elif prof == 'Médecin':
            description = 'Les coupes de cheveux, la dentisterie, les saignées et la chirurgie - si cela requiert une ' \
                          'main ferme et un rasoir, vous le faites. Vous avez peut-être pris la route pour développer ' \
                          'vos compétences ou vous confronter à un monde qui laisse vos patients si meurtris et blessés.'
        elif prof == 'Noble':
            description = 'Pour le peuple commun, la vie d\'un noble semble être celle d\'un luxe idyllique, mais en ' \
                          'grandissant en tant que noble ou membre de la petite noblesse ambitieuse, vous connaissez la ' \
                          'réalité : la vie d\'un noble est faite d\'obligations et d\'intrigues. Que vous cherchiez à ' \
                          'échapper à vos devoirs en vous lançant dans l\'aventure ou à améliorer votre condition, ' \
                          'vous avez troqué les soies et les fastes pour la vie d\'un aventurier.'
        elif prof == 'Parieur':
            description = 'Le frisson de la victoire vous a attiré dans les jeux de hasard. Cela aurait pu être une ' \
                          'activité lucrative en parallèle qui ne se comparait en rien aux véritables risques de ' \
                          'l\'aventure, ou vous auriez pu connaître des moments difficiles en raison de vos jeux ' \
                          'd\'argent et vous tourner vers l\'aventure comme une manière de sortir de cette spirale.'
        elif prof == 'Pèlerin':
            description = 'Dans votre jeunesse, vous avez effectué plusieurs pèlerinages vers des sanctuaires importants ' \
                          'et des sites saints. Vous auriez pu être un frère mendiant, un vendeur de reliques sacrées ' \
                          '(réelles ou frauduleuses) ou simplement un simple fermier suivant les préceptes de votre foi. ' \
                          'Quels que soient les objectifs de vos errances aujourd\'hui, votre foi vous protège toujours ' \
                          'sur la route.'
        elif prof == 'Percepteur':
            description = 'Détesté mais nécessaire, vous étiez envoyé lorsque les impôts étaient dus. Accomplir votre ' \
                          'travail pouvait nécessiter des déplacements et de la persuasion, ou peut-être étiez-vous ' \
                          'responsable de la collecte des taxes sur le commerce. Dans tous les cas, cela signifiait ' \
                          'parfois se salir les mains, et l\'aventure vous semblait être la prochaine étape logique.'
    if language == 'en':
        if prof == 'Acolyte':
            description = 'You spent your early days in a religious monastery or cloister. You may have traveled out ' \
                          'into the world to spread the message of your religion or because you cast away the ' \
                          'teachings of your faith, but deep down you’ll always carry within you the lessons you learned.'
        elif prof == 'Acrobate':
            description = 'In a circus or on the streets, you earned your pay by performing as an acrobat. You might ' \
                          'have turned to adventuring when the money dried up, or simply decided to put your skills to ' \
                          'better use.'
        elif prof == 'Apprenti Mage':
            description = 'You are currently enrolled at the school of magic of Pelagius, where you\'re learning the ' \
                          'fundamentals of your magical tradition. Whether your adventuring occurs during breaks ' \
                          'between semesters, as part of a work study program, or even within the halls of the ' \
                          'academy itself, you\'ll have to learn to juggle your dual life.'
        elif prof == 'Artisan':
            description = 'As an apprentice, you practiced a particular form of building or crafting, developing ' \
                          'specialized skill. You might have been a blacksmith’s apprentice toiling over the forge ' \
                          'for countless hours, a young tailor sewing garments of all kinds, or a shipwright shaping ' \
                          'the hulls of ships.'
        elif prof == 'Artiste':
            description = 'Your art is your greatest passion, whatever form it takes. Adventuring might help you find' \
                          ' inspiration, or simply be a way to survive until you become a world-famous artist.'
        elif prof == 'Bandit':
            description = 'Your past includes no small amount of rural banditry, robbing travelers on the road and ' \
                          'scraping by. Whether your robbery was sanctioned by a local noble or you did so of your ' \
                          'own accord, you eventually got caught up in the adventuring life. Now, adventure is your ' \
                          'stock and trade, and years of camping and skirmishing have only helped.'
        elif prof == 'Barbare':
            description = 'Traveling far and wide, you picked up basic tactics for surviving on the road and in' \
                          ' unknown lands, getting by with few supplies and even fewer comforts. As an adventurer, ' \
                          'you travel still, often into even more dangerous places.'
        elif prof == 'Cavalier':
            description = 'In your youth, you galloped on horseback over vast prairies, serving as a vanguard for ' \
                          'your settlement, an army, or another group. Seeing so many different lands built a thirst ' \
                          'in you to adventure and explore the world instead of just racing past it.'
        elif prof == 'Cherche-Sorts':
            description = 'Conventional magic can only hold your attention for so long. Instead, you\'ve devoted ' \
                          'yourself to understanding truly esoteric spells, which invariably draws you to explore the ' \
                          'world and all its eldritch traditions.'
        elif prof == 'Cultiste':
            description = 'You were (or still are) a member of a cult whose rites may involve sacred dances to ' \
                          'ensure a strong harvest or dire rituals that call upon dark powers. You might have taken ' \
                          'up adventuring to further your cult’s aims, to initiate yourself into the world’s ' \
                          'grander mysteries, or to flee unsavory practices or strictures.'
        elif prof == 'Disciple Martial':
            description = 'You dedicated yourself to intense training and rigorous study to become a great warrior. ' \
                          'The school you attended might have been a traditionalist monastery, an elite military ' \
                          'academy, or the local branch of a prestigious mercenary organization.'
        elif prof == 'Eclaireur':
            description = 'You called the wilderness home as you found trails and guided travelers. Your wanderlust' \
                          ' could have called you to the adventuring life, or perhaps you served as a scout for ' \
                          'soldiers and found you liked battle.'
        elif prof == 'Ecuyer':
            description = 'You trained at the feet of a knight, maintaining their gear and supporting them at ' \
                          'tourneys and in battle. Now you search for a challenge that will prove you worthy of ' \
                          'full knighthood, or you\'ve spurned pomp and ceremony to test yourself in honest, albeit ' \
                          'less formal, combat.'
        elif prof == 'Enfant des Rues':
            description = 'You eked out a living by picking pockets on the streets of a major city, never knowing' \
                          ' where you’d find your next meal. While some folk adventure for the glory,' \
                          ' you do so to survive.'
        elif prof == 'Garde':
            description = 'You served in the guard, out of either patriotism or the need for coin. Either way, you' \
                          ' know how to get a difficult suspect to talk. However you left the guard, you might ' \
                          'think of adventuring as a way to use your skills on a wider stage.'
        elif prof == 'Gladiateur':
            description = 'The bloody games of the arena taught you the art of combat. Before you attained true' \
                          ' fame, you departed—or escaped—the arena to explore the world. Your skill at drawing' \
                          ' both blood and a crowd’s attention pay off in a new adventuring life.'
        elif prof == 'Guerrier':
            description = 'In your younger days, you waded into battle as a mercenary, a warrior defending a ' \
                          'nomadic people, or a member of a militia or army. You might have wanted to break out ' \
                          'from the regimented structure of these forces, or you could have always been as ' \
                          'independent a warrior as you are now.'
        elif prof == 'Herboriste':
            description = 'As a formally trained apothecary or a rural practitioner of folk medicine, you learned ' \
                          'the healing properties of various herbs. You’re adept at collecting the right natural ' \
                          'cures in all sorts of environments and preparing them properly.'
        elif prof == 'Juriste':
            description = 'Piles of legal manuals, stern teachers, and experience in the courtroom have instructed' \
                          ' you in legal matters. You’re capable of mounting a prosecution or defense in court, and' \
                          ' you tend to keep abreast of local laws, as you never can tell when you might need to know' \
                          ' them on short notice.'
        elif prof == 'Marchand':
            description = 'In a dusty shop, market stall, or merchant caravan, you bartered wares for coin and' \
                          ' trade goods. The skills you picked up still apply in the adventuring life, in which a' \
                          ' good deal on a suit of armor could prevent your death.'
        elif prof == 'Médecin':
            description = 'Haircuts, dentistry, bloodletting, and surgery—if it takes a steady hand and a razor, you' \
                          ' do it. You may have taken to the road to expand your skills, or to test yourself against' \
                          ' a world that leaves your patients so battered and bruised.'
        elif prof == 'Noble':
            description = 'To the common folk, the life of a noble seems one of idyllic luxury, but growing up as a' \
                          ' noble or member of the aspiring gentry, you know the reality: a noble’s lot is obligation' \
                          ' and intrigue. Whether you seek to escape your duties by adventuring or to better your' \
                          ' station, you have traded silks and pageantry for an adventurer’s life.'
        elif prof == 'Parieur':
            description = 'The thrill of the win drew you into games of chance. This might have been a lucrative ' \
                          'sideline that paled in comparison to the real risks of adventuring, or you might have ' \
                          'fallen on hard times due to your gambling and pursued adventuring as a way out of a spiral.'
        elif prof == 'Pèlerin':
            description = 'In your youth, you made several pilgrimages to important shrines and holy sites. You might' \
                          ' have been a mendicant friar, a seller of holy relics (real or fraudulent), or just a ' \
                          'simple farmer following the dictates of your faith. Whatever the aims of your wanderings ' \
                          'now, your faith still protects you on the road.'
        elif prof == 'Percepteur':
            description = 'Reviled but required, you were sent when taxes were due. Performing your job might have ' \
                          'required travel and persuasion, or perhaps you were responsible for collecting taxes on' \
                          ' trade. Either way, it sometimes meant dirty hands, and adventuring seemed the next logical' \
                          ' step to you.'

    return description
def profession_picture(prof):
    picture_wh = [0,0]
    try :
        width, height = Image.open('project\static\classes_images\\' + prof + '.webp').size
        picture_wh = [width * 0.6, height * 0.6]
    except Exception as e :
        print(e)
    return picture_wh