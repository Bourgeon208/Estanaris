# This script is directly linked to naissance.html page
# "Naissance" means birth

# The players has to answer several questions in order the define the basics attribute and the profession of its
# character but also its alignment (if he is good/evil, lawful/chaotic)
from PIL import Image
import random
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
        r = random.randint(1, 5)
        print('RDN INT : ' + str(r))
        if (reve == 'Connaissance') and alignmentLC < 2 and r > 3:
            player.profession = 'Cherche-Sorts'
            player.spell_attribute = 'I'
            player.increase_attribute(2, 'wisdom')
            player.increase_attribute(4, 'intelligence')
            player.increase_attribute(1, 'arcanaI')
            player.increase_attribute(1, 'occultismI')
            player.lores.append('library')
        elif player.soclasse == 'Aristocrate':
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
                player.profession = 'Pèlerin'
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
        if player.alignmentLC < 0 and player.alignmentGE < 0 and (reve == 'Libre' or reve == 'Pouvoir'):
            player.profession = 'Bandit'
            player.increase_attribute(2, 'dexterity')
            player.increase_attribute(2, 'charisma')
            player.increase_attribute(1, 'intimidationC')
            player.increase_attribute(1, 'stealthD')
            player.increase_attribute(1, 'survivalW')
        elif player.soclasse == 'Aristocrate':
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
            elif player.alignmentLC < 0 and (ancestre == 'Orc' or (reve == 'Pouvoir' or reve == 'Libre')):
                player.profession = 'Barbare'
                player.increase_attribute(2, 'strength')
                player.increase_attribute(2, 'constitution')
                player.increase_attribute(1, 'athleticsS')
                player.increase_attribute(1, 'survivalW')
                player.lores.append('plains')
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
                player.profession = 'Percepteur'
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
            elif player.alignmentLC < 0 and (reve == 'Renom' or reve == 'Libre'):
                player.profession = 'Artiste'
                player.increase_attribute(2, 'dexterity')
                player.increase_attribute(2, 'charisma')
                player.increase_attribute(1, 'craftingI')
                player.increase_attribute(1, 'performanceC')
                player.lores.append('art')
            elif player.alignmentGE >= 1:
                player.profession = 'Médecin'
                player.increase_attribute(2, 'dexterity')
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
            elif player.alignmentLC < 0 and (reve == 'Renom' or reve == 'Libre'):
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
                player.profession = 'Enfant des Rues'
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

def profession_description(prof):
    description = ''
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
    return description
def profession_picture(prof):
    picture_wh = [0,0]
    try :
        # width, height = Image.open('static\classes_images\\' + prof + '.webp').size
        width, height = Image.open("C:\\Users\g.bourgeon\Documents\GitHub\Estanaris\project\static\classes_images\\" + prof + ".webp").size
        picture_wh = [width * 0.6, height * 0.6]
    except Exception as e :
        print(e)
    return picture_wh