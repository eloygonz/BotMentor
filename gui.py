# -*- coding: UTF-8 -*-
import sys
import time
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


def horarios(id, mid, bot):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Horarios curso', callback_data='hCurso'),
         InlineKeyboardButton(text='Horarios clase', callback_data='hClase'),
         InlineKeyboardButton(text='Volver', callback_data='menu')]])
    bot.deleteMessage(mid)
    mid = telepot.message_identifier(bot.sendMessage(id, "┬┐Qu├® horarios quiere ver?:", reply_markup=keyboard))
    return mid

def fichas(id, mid, bot):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Fichas docentes de curso', callback_data='fCurso'),
         InlineKeyboardButton(text='Ficha docente de asignatura', callback_data='fAsignatura'),
         InlineKeyboardButton(text='Volver', callback_data='menu')]])
    bot.deleteMessage(mid)
    mid = telepot.message_identifier(bot.sendMessage(id, "┬┐Qu├® Fichas docentes quiere ver?:", reply_markup=keyboard))
    return mid

def profesores(id, mid, bot):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Volver', callback_data='menu')]])
    bot.deleteMessage(mid)
    mid = telepot.message_identifier(bot.sendMessage(id,"┬┐De qu├® profesor quieres saber?:", reply_markup=keyboard))
    # bot.editMessageText(mid, "┬┐De qu├® profesor quieres saber?:", reply_markup=keyboard)
    return mid
def clases(id, mid, bot):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Volver', callback_data='menu')]])
    bot.editMessageText(mid, text='┬┐C├║al es la clase sobre la que quieres informaci├│n?:', reply_markup=keyboard)


def seleccionGrado(id, bot):

    bot.sendMessage(id, 'Selecciona la titulaci├│n:', reply_markup=ReplyKeyboardMarkup( keyboard = [
        [KeyboardButton(text='Inform├ítica'), KeyboardButton(text='Software'), KeyboardButton(text='Computadores')],
        [KeyboardButton(text='Videojuegos'), KeyboardButton(text='M├íster'), KeyboardButton(text='Optativas')]]))


def seleccionCurso(id, msg, bot, grado):
    if grado == 'M├íster':
        cursos = [[KeyboardButton(text='1')]]
        max = 1
    elif grado == 'Videojuegos':
        cursos = [[KeyboardButton(text='1'),KeyboardButton(text='2'),KeyboardButton(text='3')]]
        max = 3
    elif grado == 'Optativas':
        cursos = [[KeyboardButton(text='1')]]
        max = 1
    else:
        cursos = [[KeyboardButton(text='1'),KeyboardButton(text='2'),KeyboardButton(text='3'),KeyboardButton(text='4')]]
        max = 4

    bot.sendMessage(id, "Selecciona el curso:", reply_markup=ReplyKeyboardMarkup(keyboard = cursos))


def seleccionGrupo(id, msg, bot):
    keyboard = [
        [KeyboardButton(text='Inform├ítica'), KeyboardButton(text='Software'), KeyboardButton(text='Computadores')],
        [KeyboardButton(text='Videojuegos'), KeyboardButton(text='Master'), KeyboardButton(text='Optativas')]]
    bot.editMessageText(id, "Selecciona la titulaci├│n:", reply_markup=keyboard)
    content_type, chat_type, chat_id = telepot.glance(msg)

    """
    keyboard2 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Inform├ítica', callback_data='II'),InlineKeyboardButton(text='Software', callback_data='IS'),InlineKeyboardButton(text='Computadores', callback_data='IC')],[InlineKeyboardButton(text='Videojuegos', callback_data='DV'),InlineKeyboardButton(text='Master', callback_data='MII'),InlineKeyboardButton(text='Optativas', callback_data='OP')]])
    bot.sendMessage(id, "Selecciona la titulaci├│n:", reply_markup=keyboard2)
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
"""


