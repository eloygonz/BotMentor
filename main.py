# -*- coding: UTF-8 -*-
import sys
import time
import telepot
from gui import *
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

    def parseGrupo(g):
        grupo = g.upper()
    def setCurso(self,c):
        # type: (object) -> object
        self.curso = c

al = Alumno
class BotMentorStarter(telepot.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(BotMentorStarter, self).__init__(*args, **kwargs)
        global al
        al = Alumno()

    def on_chat_message(self, msg):
        if msg['text'] == '/start':
            content_type, chat_type, chat_id = telepot.glance(msg)
            global mid
            self.sender.sendMessage(
                'Hola!!\nEste bot te sirve para consultar informaci├│n sobre Tutorias, horarios, profesores y mucho m├ís.\nPulsa "Consultar" para comenzar a utilizar el BotMentor de la Facultad de inform├ítica de la UCM')
            sent = self.sender.sendMessage('Pulse en empezar', reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Empezar', callback_data='menu'), ]]))
            mid = telepot.message_identifier(sent)
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
        elif gradoRequest:
            content_type, chat_type, chat_id = telepot.glance(msg)
            global gradoRequest, cursoRequest
            gradoRequest = False
            cursoRequest = True
            global al
            al.parseGrado(msg['text'])
            seleccionCurso(chat_id, msg, bot, al.grado)
            al.setCurso(msg['text'])
        elif cursoRequest:
            content_type, chat_type, chat_id = telepot.glance(msg)
            global grupoRequest, cursoRequest
            cursoRequest = False
            grupoRequest = True
            global al
            seleccionCurso(chat_id,msg,bot,al.grado)


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
            mid = horarios(from_id, mid, bot)
        elif query_data == 'fichas':
            mid = fichas(from_id, mid, bot)
        elif query_data == 'profesores':
            global profesorRequest
            profesorRequest = True
            mid = profesores(from_id, mid, bot)
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