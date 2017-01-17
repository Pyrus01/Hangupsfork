import asyncio, random
import os, io, gettext
import time 
from hangupsbot.utils import strip_quotes, text_to_segments
from hangupsbot.commands import command
import appdirs

### NOTAS ###

@command.register
def recuerda(bot, event, *args):
    """Guarda un mensaje en la libreta de notas\nUso: <bot> recuerda [nota]"""
    arg = ' '.join(args)
    dirs = appdirs.AppDirs('hangupsbot', 'hangupsbot')
    nota= str(os.path.join(dirs.user_data_dir))+"/"+str(event.user_id.chat_id)+".txt"
    if os.path.isfile(nota):
        text='queso'
    else: 
        os.mknod(nota)

    f = open(nota,'r+')
    s=time.ctime()
    msg= str((s+'\n[{}]\n'+'{}'+'\n\n').format(event.user.full_name,arg))
    f.write(msg)
    f.readlines()
    f.close()
        
    yield from event.conv.send_message(text_to_segments('Guardado'))

@command.register
def notas(bot, event, *args):
    """Muestra las notas guardadas \n Uso: <bot> notas"""
    dirs = appdirs.AppDirs('hangupsbot', 'hangupsbot')
    nota= str(os.path.join(dirs.user_data_dir))+"/"+str(event.user_id.chat_id)+".txt"
    if os.path.isfile(nota):
        text='queso'
    else: 
        os.mknod(nota)
    f = open(nota,'r+')
    text= 'Notas:\n'
    r=f.readlines()
    for line in r:
        text= _(text+line)
    f.close()
    yield from event.conv.send_message(text_to_segments(text))

@command.register(admin=True)
def deletenotas(bot, event, *args):
    """Borra la libreta de notas (Solo admins)\n Uso: <bot> deletenotas"""
    dirs = appdirs.AppDirs('hangupsbot', 'hangupsbot')
    nota= str(os.path.join(dirs.user_data_dir))+"/"+str(event.user_id.chat_id)+".txt"
    arg = ' '.join(args)
    if os.path.isfile(nota):
        text='queso'
    else: 
        os.mknod(nota)
    f = open(nota,'w')
    f.write(' ')
    f.close()
    yield from event.conv.send_message(text_to_segments('Borradas todas las notas'))
