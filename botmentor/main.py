# -*- coding: UTF-8 -*-
import time
from gui import *
from CommandParser import *
from Consultor import *
from Commands import *
from FactoriaCommand import FactoriaCommand
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

    def parseGrado(self, g):
        if g == u'Informática':
            self.grado = 'GII'
        elif g == 'Software':
            self.grado = 'GIS'
        elif g == u'Máster':
            self.grado = 'MII'
        elif g == 'Computadores':
            self.grado = 'GIC'
        elif g == 'Videojuegos':
            self.grado = 'GDV'

    def parseGrupo(g):
        grupo = g.upper()
    def setCurso(self,c):
        # type: (object) -> object
        self.curso = c
    def setGrupo (self,g):
        self.grupo = g

comando = Command
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
            comando = Command(command)
            if parseCommand(self,comando):
                f = FactoriaCommand
                com = f.creaComando(command)
                if comando.com == '/start':
                    global mid
                    self.sender.sendMessage(
                        'Hola!!\nEste bot te sirve para consultar información sobre Tutorias, horarios, profesores y mucho más.\nPulsa "Consultar" para comenzar a utilizar el BotMentor de la Facultad de informática de la UCM')
                    sent = self.sender.sendMessage('Pulse en empezar', reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Empezar', callback_data='menu'), ]]))
                    menu(self)
                    prueba()
                elif comando.com == '/menu':
                    menu(self)
                elif comando.com == '/horario':
                    self.sender.sendMessage('comando horario parseado bien!')
                    if com.estaListo():
                        com.ejecutar()
                elif comando.com == 'Horarios' or comando.com == '/horarios':
                    self.sender.sendMessage('comando horarios parseado bien!')
                    if com.estaListo():
                        com.ejecutar()
                elif comando.com == 'Volver' or comando.com == '/volver':
                    self.sender.sendMessage('comando volver parseado bien!')

                    menu(self)
                elif comando.com == 'Fichas docentes' or comando.com == '/fichas':
                    self.sender.sendMessage('comando fichas parseado bien!')
                    if com.estaListo():
                        com.ejecutar()
                elif comando.com == '/ficha':
                    self.sender.sendMessage('comando ficha parseado bien!')
                    if com.estaListo():
                        com.ejecutar()
                elif comando.com == '/tutoria':
                    self.sender.sendMessage('comando tutoria parseado bien!')
                    if com.estaListo():
                        com.ejecutar()
                elif comando.com == '/ayuda':
                    self.sender.sendMessage('comando ayuda parseado bien!')
                elif comando.com == 'Profesores' or comando.com == '/profesor':
                    self.sender.sendMessage('comando profesor parseado bien!')
                    if com.estaListo():
                        profesor = com.ejecutar()
                        self.sender.sendMessage('El profesor que buscas es: ' + profesor.nombre + ':\n'
                            + 'Despacho: ' + profesor.despacho + '\nCorreo: ' + profesor.correo + '\nTlf: '+ profesor.tlf)
                elif comando.com == 'Clases' or comando.com == '/clase':
                    self.sender.sendMessage('comando clase parseado bien!')
                    if com.estaListo():
                        com.ejecutar()
                elif comando.com == 'Fichas de curso completo' or comando.com == '/fcurso':
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
print('Ejecutando BotMentor...')

# Keep the program running.
while 1:
    time.sleep(10)