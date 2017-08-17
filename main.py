# -*- coding: UTF-8 -*-
import time
from gui import *
from parser import *
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from telepot.delegate import (
    per_chat_id, per_callback_query_origin, create_open, pave_event_space)

profesorRequest = False
profesorNombre = 'Fulanito'
claseRequest = False
mid = 0
gradoRequest = False
cursoRequest = False
grupoRequest = False

class Alumno:
    grado=''
    curso=1
    grupo=''
    def __init__(self):
        curso = 1
        grado = 'II'
        grupo = 'A'

    def parseGrado(self,g):
        if g == u'Informática':
            self.grado = 'II'
        elif g == 'Software':
            self.grado = 'IS'
        elif g == u'Máster':
            self.grado = 'MI'
        elif g == 'Computadores':
            self.grado = 'IC'
        elif g == 'Videojuegos':
            self.grado = 'DV'
        elif g == 'Optativas':
            self.grado = 'OP'

    def parseGrupo(g):
        grupo = g.upper()
    def setCurso(self,c):
        # type: (object) -> object
        self.curso = c
    def setGrupo (self,g):
        self.grupo = g
class Comando:
    grado= None
    curso= None
    grupo= None
    nombre = None
    apellido = None
    def __init__(self, c):

        if len(c) == 2:
            self.nombre = c[1]
        elif len(c) == 3:
            self.nombre = c[1]
            self.apellido = c[2]
        elif len(c) == 4:
            self.grado = c[1]
            self.curso = c[2]
            self.grupo = c [3]
        elif len(c) == 5:
            self.grado = c[1]
            self.curso = c[2]
            self.grupo = c [3]
            self.nombre = c[4]

al = Alumno
comando = Comando
class BotMentorStarter(telepot.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(BotMentorStarter, self).__init__(*args, **kwargs)
        global al
        al = Alumno()

    def on_chat_message(self, msg):
        if telepot.flavor(msg) == 'chat':
            content_type, chat_type, chat_id = telepot.glance(msg)
            command = msg['text'].split()
            global comando
            commando = Comando(command)
            if msg['text'] == '/start':
                global mid
                self.sender.sendMessage(
                    'Hola!!\nEste bot te sirve para consultar información sobre Tutorias, horarios, profesores y mucho más.\nPulsa "Consultar" para comenzar a utilizar el BotMentor de la Facultad de informática de la UCM')
                sent = self.sender.sendMessage('Pulse en empezar', reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Empezar', callback_data='menu'), ]]))
                menu(self)
            elif msg['text'] == '/menu':
                content_type, chat_type, chat_id = telepot.glance(msg)
                menu(self)
               # self.sender.sendMessage('Seleccione la opción deseada',)
            elif msg['text'] == '/horario':
                parse
            elif msg['text'] == 'Horarios' or msg['text'] == '/horarios':
                content_type, chat_type, chat_id = telepot.glance(msg)
                horarios(self)
            elif msg['text'] == 'Volver' or msg['text'] == '/volver':
                content_type, chat_type, chat_id = telepot.glance(msg)
                menu(self)
            elif msg['text'] == 'Fichas docentes' or msg['text'] == '/fichas':
                content_type, chat_type, chat_id = telepot.glance(msg)
                fichas(self)
            elif msg['text'] == '/ficha':
                fichas(self)
            elif msg['text'] == '/tutoria':
                fichas(self)
            elif msg['text'] == '/ayuda':
                fichas(self)
            elif msg['text'] == 'Profesores' or msg['text'] == '/profesor':
                content_type, chat_type, chat_id = telepot.glance(msg)
                profesores(self)
                global profesorRequest
                profesorRequest = True
            elif msg['text'] == 'Clases' or msg['text'] == '/clase':
                content_type, chat_type, chat_id = telepot.glance(msg)
                clases(self)
                global profesorRequest
                profesorRequest = True
            elif msg['text'] == 'Fichas de curso completo' or msg['text'] == '/fcurso':
                # self.sender.forceReply(force_reply= True)
                seleccionGrado(self)
                global cursoRequest
                cursoRequest = True
            elif profesorRequest:
                global profesorNombre
                profesorNombre = msg['text']
                print(profesorNombre)
                self.sender.sendMessage('Espera mientras busco a ' + profesorNombre + ' en mi base de datos')
                global profesorRequest
                profesorRequest = False
            elif claseRequest:
                global claseRequest
                claseRequest = False
                self.sender.sendMessage('Vamos a ver, que clase quieres ver')
            elif cursoRequest:
                content_type, chat_type, chat_id = telepot.glance(msg)
                global cursoRequest, grupoRequest
                cursoRequest = False
                grupoRequest = True
                global al
                al.parseGrado(msg['text'])
                seleccionCurso(self, al.grado)
                al.setCurso(msg['text'])
            elif grupoRequest:
                content_type, chat_type, chat_id = telepot.glance(msg)
                global grupoRequest, cursoRequest
                grupoRequest = False
                global al
                seleccionGrupo(self,al.grado)
                al.setGrupo(msg['text'])
            elif grupoRequest:
                content_type, chat_type, chat_id = telepot.glance(msg)
                global grupoRequest, cursoRequest
                cursoRequest = False
                grupoRequest = False
                global al
                seleccionGrupo(self,al.grupo)
                al.setGrupo(msg['text'])

class BotMentor(telepot.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(BotMentor, self).__init__(*args, **kwargs)

    def on_callback_query(self, msg):
        query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
        if query_data == 'menu':
            bot.deleteMessage(mid)
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='Horarios', callback_data='horarios'),
                 InlineKeyboardButton(text='Tutorias', callback_data='tutorias')],
                [InlineKeyboardButton(text='Profesores', callback_data='profesores')
                    , InlineKeyboardButton(text='Clases', callback_data='clases')],
                [InlineKeyboardButton(text='Fichas docentes', callback_data='fichas')],
            ])
            sent = bot.sendMessage(from_id, "Seleccione la opci├│n deseada:", reply_markup=keyboard)
            global mid
            mid = telepot.message_identifier(sent)
        elif query_data == 'horarios':
            mid = horarios(self)
        elif query_data == 'fichas':
            mid = fichas(self)
        elif query_data == 'profesores':
            global profesorRequest
            profesorRequest = True
            mid = profesores(self)
        elif query_data == 'clases':
            mid = clases(from_id, mid, bot)
        elif query_data == 'fCurso':
            global gradoRequest
            gradoRequest = True
            seleccionGrado(from_id,bot)

    def on_idle(self, event):
        self.editor.editMessageText('\n\nThis message will disappear in 5 seconds to test deleteMessage',
                                    reply_markup=None)
        time.sleep(5)
        self.editor.deleteMessage()
        self.close()

    """
        casos = {'hClase':hClase, 'hCurso':hCurso,'profesores':profesores, 'clases':clases, 'fichas':fichas}
        query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
        casos[query_data](int(from_id),msg)
        text = str(casos[query_data])
        bot.answerCallbackQuery(query_id, text)
"""


TOKEN = "423194965:AAFJtn4HcgYQmR0oN6WoSAEHZljARFlBSeI"

bot = telepot.DelegatorBot(TOKEN, [
    pave_event_space()(
        per_chat_id(), create_open, BotMentorStarter, timeout=60),
    pave_event_space()(
        per_callback_query_origin(), create_open, BotMentor, timeout=300),
])

MessageLoop(bot).run_as_thread()
print('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)