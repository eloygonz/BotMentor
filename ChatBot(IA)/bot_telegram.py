# -*- coding: UTF-8 -*-
import time
import telepot
from chatterbot import ChatBot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from telepot.delegate import (
    per_chat_id, per_callback_query_origin, create_open, pave_event_space)

chatbot = ChatBot(
    "Terminal",
    
    logic_adapters=[
        #"chatterbot.logic.MathematicalEvaluation",
        "chatterbot.logic.TimeLogicAdapter",
        "chatterbot.logic.BestMatch"
    ],
    #input_adapter="chatterbot.input.TerminalAdapter",
    #output_adapter="chatterbot.output.TerminalAdapter",
)

class bot_telegram_starter(telepot.helper.ChatHandler):
	
    def __init__(self, *args, **kwargs):
        super(bot_telegram_starter, self).__init__(*args, **kwargs)
        

    def on_chat_message(self, msg):
        
        if telepot.flavor(msg) == 'chat':
            content_type, chat_type, chat_id = telepot.glance(msg)
            
            response = chatbot.get_response(msg['text'])

            if (len(response.text) > 1500):
                aux = response.text.split("\n")
                
                for tex in aux:
                   self.sender.sendMessage(tex)
                
            else:

                self.sender.sendMessage(response.text)         


TOKEN = "423194965:AAFJtn4HcgYQmR0oN6WoSAEHZljARFlBSeI"

bot = telepot.DelegatorBot(TOKEN, [
    pave_event_space()(
    per_chat_id(), create_open, bot_telegram_starter, timeout=60),
])

MessageLoop(bot).run_as_thread()
print('Ejecutando BotMentor...')


# Keep the program running.
while 1:
    time.sleep(10)

                   
"""
class bot_telegram(telepot.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(BotMentor, self).__init__(*args, **kwargs)

    def on_callback_query(self, msg):
        query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
        if query_data == 'menu':
            bot.deleteMessage(mid)
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='Horarios', callback_data='horarios'),
                 InlineKeyboardButton(text='Tutorias', callback_data='tutorias')],
                [InlineKeyboardButton(text='Profesores', callback_data='profesores'),
                 InlineKeyboardButton(text='Clases', callback_data='clases')],
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


