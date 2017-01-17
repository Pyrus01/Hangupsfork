import asyncio, random
import time 
import urllib
from hangupsbot.utils import strip_quotes, text_to_segments
from hangupsbot.commands import command
from random import randint
from math import sqrt
from math import pi


@command.register
def laip(bot, event, *args):
    """Repite el mensaje que le den\n Uso: bot di [texto]"""
    my_ip = urllib.request.urlopen('http://ip.42.pl/raw').read()
    text = str(my_ip)
    yield from event.conv.send_message(text_to_segments(text))

@command.register
def puedes(bot, event, *args):
    """Responde al azar si puede o no.\n Uso: <bot> verdad [frase]"""
    if (randint(0,9)) > 3:
        text = 'Claro! ^^'
    else:
        text = 'No lo creo, lo siento...'
    yield from event.conv.send_message(text_to_segments(text))

@command.register
def quieres(bot, event, *args):
    """Responde al azar si quiere o no.\n Uso: <bot> verdad [frase]"""
    if (randint(0,9)) > 3:
        text = 'No quiero...'
    else:
        text = 'Yep!'
    yield from event.conv.send_message(text_to_segments(text))

@command.register
def mata(bot, event,*args):
    """Los [ro]bots no soportan las paradojas\n Uso: <bot> Este enunciado es mentira [frase]"""
    arg = ' '.join(args)
    text= 'Solo soy un bot! no puedo matar '+arg+' !'
    yield from event.conv.send_message(text_to_segments(text))

@command.register
def eres(bot, event, *args):
    """Pues tal vez si lo sea\n Uso: bot eres [texto]"""
    ser = ' '.join(args)
    if (randint(0,1)) == 1:
        text = _('¿D-de verdad... piensas que soy '+ser+' ?')
    else:
        text = _('A veces yo tambien pienso que soy '+ser)
    yield from event.conv.send_message(text_to_segments(text))

@command.register
def saluda(bot, event, *args):
    """Saluda a la persona. \nUso: bot saluda [Persona]"""
    text = 'Holis '+' '.join(args)
    yield from event.conv.send_message(text_to_segments(text))

@command.register
def porque(bot, event, *args):
    """Saluda a la persona. \nUso: bot saluda [Persona]"""
    text = 'Lo siento, no lo se.'
    yield from event.conv.send_message(text_to_segments(text))

@command.register
def dime(bot, event, *args):
    """Regresa una frase despues de 'dime'\n Uso: <bot> dime [frase]"""
    text = ' '.join(args)
    yield from event.conv.send_message(text_to_segments(text))

@command.register
def dile(bot, event, *args):
    """Regresa una frase despues de 'dile'\n Uso: <bot> dile [frase]"""
    text = ' '.join(args)
    yield from event.conv.send_message(text_to_segments(text))

@command.register
def te(bot, event, *args):
    """Creo que el tambien siente lo mismo \n Uso: <bot> te [frase]"""
    argums = ' '.join(args)
    text = 'Yo tambien te '+argums+' !!!'
    yield from event.conv.send_message(text_to_segments(text))

@command.register
def felicidades(bot, event, *args):
    """Felicidades! \n Uso: <bot> congratulations"""
    text = '__Yay!__\nhttps://www.youtube.com/watch?v=3NuFVQk_CCs'
    yield from event.conv.send_message(text_to_segments(text))

@command.register
def canta(bot, event, *args):
    """Maid Sings \n Uso: <bot> congratulations"""
    text = 'Baby I wanna be your girl ~  \https://www.youtube.com/watch?v=ziU36CDT1wU'
    yield from event.conv.send_message(text_to_segments(text))


@command.register
def dame(bot, event, *args):
    """Dame algo bot! \n Uso: <bot> dame [frase]"""
    text = 'toma '+' '.join(args)
    yield from event.conv.send_message(text_to_segments(text))

@command.register
def malo(bot, event, *args):
    """Se disculpa por ser un mal mal bot \n Uso: <bot> malo [frase]"""
    text = _('D-de verdad lo siento mucho, no volvera a pasar!')
    yield from event.conv.send_message(text_to_segments(text))

@command.register
def mala(bot, event, *args):
    """Se disculpa por ser una mala bot ;) \n Uso: <bot> mala [frase]"""
    text = _('D-de verdad lo siento mucho, no volvera a pasar!')
    yield from event.conv.send_message(text_to_segments(text))

@command.register
def gracias(bot, event, *args):
    """Estoy para servirte, no hay necesidad de agradecer\n Uso: <bot> gracias"""
    text = _('Estoy para servir! ^///^')
    yield from event.conv.send_message(text_to_segments(text))

@command.register
def buena(bot, event, *args):
    """Buen bot !\nUso: <bot> gracias"""
    text = _('M-muchas gracias! >///<')
    yield from event.conv.send_message(text_to_segments(text))

@command.register
def buen(bot, event, que, *args):
    """Que bueno es el bot\b <bot> buen (bot)"""
    if strip_quotes(que)=="bot":
        text = _('Gracias, me esfuerzo')
    else:
        text = _('Ehh...ehhh...EHHH!??! 0////0')
    yield from event.conv.send_message(text_to_segments(text))

@command.register
def emoticon(bot, event, emon, *args):
    """
    😪 bozteso 
    😐 serio 
    😊 contento
    😀 sonriente
    😂 lol
    😃 feliz
    😅 preocupado
    😇 angel
    😠 enojado
    😬 furioso
    😢 lagrima
    😴 sueño
    😮 sorpresa
    😥 angustiado
    😟 jum
    😞 triste
    😎 cool
    😘 beso
    😗 .3.
    😒 Sospechoso
    😶 nada
    😭 llanto
    😏 yeah
    🙋saludo
    🙅nope
    🙌festejo
    🍪 galleta
    """
    arg = ' '.join(args)
    text= '???'

    if emon == 'bozteso':
        text= '😪'
    elif emon == 'serio':
        text= '😐'
    elif emon == 'contento':
        text= '😊'
    elif emon == 'sonriente':
        text= '😀'
    elif emon == 'lol':
        text= '😂'
    elif emon == 'feliz':
        text= '😃'
    elif emon == 'preocupado':
        text= '😅'
    elif emon == 'angel':
        text= '😇'
    elif emon == 'furioso':
        text= '😬'
    elif emon == 'lagrima':
        text= '😢'
    elif emon == 'sueño':
        text= '😴'
    elif emon == 'sorpresa':
        text= '😮'
    elif emon == 'angustiado':
        text= '😥'
    elif emon == 'jum':
        text= '😟'
    elif emon == 'triste':
        text= '😞'
    elif emon == 'cool':
        text= '😎'
    elif emon == 'beso':
        text= '😘'
    elif emon == '.3.':
        text= '😗'
    elif emon == 'Sospechoso':
        text= '😒'
    elif emon == 'nada':
        text= '😶'
    elif emon == 'llanto':
        text= '😭'
    elif emon == 'yeah':
        text= '😏'
    elif emon == 'saludo':
        text= '🙋'
    elif emon == 'nope':
        text= '🙅'
    elif emon == 'festejo':
        text= '🙌'
    elif emon == 'galleta':
        text= '🍪'
    #elif emon == '':
    #    text= ''
    yield from event.conv.send_message(text_to_segments(text))
    

### Funciones de Hunter ###

@command.register
def amame(bot, event, *args):
    """El bot manda amor de bot, ¿las maquinas sienten no?\n Sintaxis: bot amame"""
    text = _('te mando amor')
    yield from event.conv.send_message(text_to_segments(text))

### Funciones de Manuel ###

@command.register
def paradoja(bot, event, *args):
    """Los [ro]bots no soportan las paradojas\n Uso: <bot> Este enunciado es mentira [frase]"""
    text = _('No pienses en ello, no pienses en ello, no pienses en ello')
    yield from event.conv.send_message(text_to_segments(text))

@command.register
def fuera(bot, event, *args):
    """El bot hiso algo que no debe y ahora debe retirarse"""
    text = _('Pe... pe.. pero por que!?')
    yield from event.conv.send_message(text_to_segments(text))

@command.register
def reglas(bot, event, *args):
    """Las tres leyes de la robótica son un conjunto de normas escritas por Isaac Asimov"""
    text = _('1.- Un robot no hará daño a un ser humano o, por inacción, permitir que un ser humano sufra daño.\n' 
    '2.- Un robot debe obedecer las órdenes dadas por los seres humanos, excepto si estas órdenes entrasen en conflicto con la 1ª Ley.\n'
    '3.-Un robot debe proteger su propia existencia en la medida en que esta protección no entre en conflicto con la 1ª o la 2ª Ley.' )
    yield from event.conv.send_message(text_to_segments(text))

@command.register
def explosions(bot, event, *args):
    """Mr torgue approves\n Uso: <bot> explosions"""
    text = _('**Explosiones yay!!**\n https://www.youtube.com/watch?v=mEizJ-TWua0')
    yield from event.conv.send_message(text_to_segments(text))

@command.register
def bestpony(bot, event, *args):
    """Responde al azar un nombre de pony.\n Uso: <bot> best pony[frase]"""
    var = (randint(0,5))
    if var == 0:
        text = 'Applejack'
    elif var == 1:
        text = 'Pinkie pie'
    elif var == 2:
        text = 'Rarity'
    elif var == 3:
        text = 'Raibow dash'
    elif var == 4:
        text =  'Twilight'
    elif var == 5:
        text =  'Fluttershy'
    yield from event.conv.send_message(text_to_segments(text))

@command.register
def este(bot, event, *args):
    """Los [ro]bots no soportan las paradojas\n Uso: <bot> Este enunciado es mentira [frase]"""
    arg = ' '.join(args)
    text= '???'
    if arg == 'enunciado es mentira':
        text= _('No pienses en ello, no pienses en ello, no pienses en ello')
    yield from event.conv.send_message(text_to_segments(text))

### AZAR ###

@command.register
def sino(bot, event, *args):
    """Simplemente te dice Si o No.\n Uso: <bot> sino [frase]"""
    if (randint(0,1)) == 1:
    	text = 'Sip!'
    else:
    	text = 'Nu...'
    yield from event.conv.send_message(text_to_segments(text))

@command.register
def verdad(bot, event, *args):
    """Responde al azar si es verdad o no.\n Uso: <bot> verdad [frase]"""
    if (randint(0,1)) == 1:
        text = 'Yep!'
    else:
        text = 'Nop...'
    yield from event.conv.send_message(text_to_segments(text))

@command.register
def moneda(bot, event, *args):
    """Lanza una moneda y te dice el resultado.\n Uso: <bot> moneda"""
    if (randint(0,1)) == 1:
    	res = '**Cara**'
    else:
    	res = '**Sello**'
    text= 'Se Lanzo una moneda al aire\n Cayó: '+res
    yield from event.conv.send_message(text_to_segments(text))

@command.register
def dado(bot, event, caras, *args):
    """Lanza un dado, es posible definir el numero de caras del dado\n Uso: <bot> dado [numero de caras]"""
    text = 'Se lanzo un dado de {} caras\n El resultado fue: '.format(strip_quotes(caras))+str(randint(1,int(caras)))
    yield from event.conv.send_message(text_to_segments(text))


### Respuestas ### 

@command.register
def como(bot, event, *args):
    """Preguntarle como esta al bot\nUso: <bot> como estas?"""
    arg = ' '.join(args)
    text= '???'
    if arg == "estas?":
        text= "Bien, gracias ^^"
    yield from event.conv.send_message(text_to_segments(text))

@command.register
def queso(bot, event, *args):
    """Queso? Queso!\nUso: <bot> queso"""
    text = _(
        'ok\n'
        'Yo Queso, tu Queso, nosotros Queseamos'
        )
    yield from event.conv.send_message(text_to_segments(text))


@command.register
def wtf(bot, event, *args):
    """ಠ_ಠ"""
    text = _('ಠ_ಠ\nhttp://www.gfycat.com/AdmirableConcreteDairycow')
    yield from event.conv.send_message(text_to_segments(text))

@command.register
def roboass(bot, event, *args):
    """[ro]bots are not for sexual. Please be safe\b Uso: <bot> roboass"""
    text = _(T-tonto... https://www.youtube.com/watch?v=2LWzrE56yf0')
    yield from event.conv.send_message(text_to_segments(text))


@command.register
def tip(bot, event, *args):
    """Tipear fedora o trilby\n <bot> tip <fedora/trilby>"""
    arg = ' '.join(args)
    text= '???'
    if arg == 'fedora'or'trilby':
        text= 'https://youtu.be/oe9uK9QGCUI'
    yield from event.conv.send_message(text_to_segments(text))

### Easter Egg (?) ###

@command.register
def aptitude(bot, event, *args):
    """Easter egg del aptitude\n Uso:\n<bot> aptitude moo\n<bot> aptitude -v
    moo \n<bot> aptitude -vv moo\n<bot> aptitude -vvv moo\b<bot> aptitude -vvvv
    moo"""
    arg = ' '.join(args)
    text= '???'
    if arg == 'moo':
        text= 'No hay ningun Easter Egg en este bot'
    elif arg == '-v moo':
        text= 'De verdad no hay un Easter Egg en este bot'
    elif arg == '-vv moo':
        text= 'No te dije que no hay Easter Eggs en este bot?'
    elif arg == '-vvv moo':
        text= _('Ok, tu ganas.\n '
                +'____/---'+'\\'+'____\n'
                +'______________\n')
    elif arg == '-vvvv moo':
        text= 'Que que es? pues un elefante dentro de una vibora, obviamente '
    yield from event.conv.send_message(text_to_segments(text))

### Sandwiches ##

@command.register
def sandwich(bot, event, *args):
    """Cosas emparedadas de pan con cosas enmedio... i guess\n ver: make me a sandwich"""
    text = _('Que tiene?')
    yield from event.conv.send_message(text_to_segments(text))

@command.register
def make(bot, event, *args):
    """Make me a sandiwch \n Uso: <bot> make me a sandwich"""
    arg = ' '.join(args)
    text= '???'
    if arg == 'me a sandwich'or'sandwich'or'me a sándwich'or'sándwich':
        text= 'Que? no, haztelo tu'
    yield from event.conv.send_message(text_to_segments(text))
@command.register

def sudo(bot, event, *args):
    """Permisos de administrador! (o no)\n Uso: [bot] sudo make me a sandwich"""
    arg = ' '.join(args)
    text= '???'
    if arg == 'make me a sandwich'or'sandwich'or'make me a sándwich'or'sándwich':
        text= 'A sus ordenes, un sandwich enseguida'
    yield from event.conv.send_message(text_to_segments(text))

### CALCULADORA ###

@command.register
def suma(bot, event, n1, n2, *args):
    """Suma 2 numeros\n Uso: bot suma [numero1] [numero2]"""
    text = str(int(strip_quotes(n1))+int(strip_quotes(n2)))
    yield from event.conv.send_message(text_to_segments(text))

@command.register
def resta(bot, event, n1, n2, *args):
    """Resta 2 numeros\n Uso: bot resta [numero1] [numero2]"""
    text = str(int(strip_quotes(n1))-int(strip_quotes(n2)))
    yield from event.conv.send_message(text_to_segments(text))

@command.register
def multi(bot, event, n1, n2, *args):
    """Multiplica 2 numeros\n Uso: bot multi [numero1] [numero2]"""
    text = str(int(strip_quotes(n1))*int(strip_quotes(n2)))
    yield from event.conv.send_message(text_to_segments(text))

@command.register
def div(bot, event, n1, n2, *args):
    """Divide 2 numeros\n Uso: bot div [numero1] [numero2]"""
    text = str(int(strip_quotes(n1))/int(strip_quotes(n2)))
    yield from event.conv.send_message(text_to_segments(text))

@command.register
def raiz(bot, event, n1, *args):
    """Raiz Cuadrada\n Uso: bot raiz [numero1] """
    num = float(strip_quotes(n1))
    num = sqrt(num)
    text= str(num)
    yield from event.conv.send_message(text_to_segments(text))

#@command.register
#def pi(bot, event, *args):
#    """Calcula pi"""
#    yield from event.conv.send_message(text_to_segments(pi))

@command.register
def mi_id(bot, event, *args):
    """Te dice tu ID interno\b <bot> mi_id"""
    yield from event.conv.send_message(text_to_segments(event.user_id.chat_id))

@command.register
def alpha(bot, event, *args):
    """Que bueno es el bot\b <bot> buen (bot)"""
    # El primero que buscar
    if str(event.user_id.chat_id) == '110463787066927524425':
        text= _("Segun tu ID, eres manuel")

    # El resto que busca, se puede copiar tantas veces quieras (ver emoticon)
    elif str(event.user_id.chat_id) == '106738693435124296098':
        text= _("Holis tsun~~~")
    elif str(event.user_id.chat_id) == '114521682538272530800':
        text= _("oOHH ! que onda farcko ! <3 soy tu fan")

        

    # Si no esta aqui el ID, este es el mensaje default:
    else :
        text=_("oohh no te conozco")

    yield from event.conv.send_message(text_to_segments(text))
