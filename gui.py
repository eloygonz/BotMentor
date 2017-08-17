# -*- coding: UTF-8 -*-
import telepot
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton

def menu(self):
    self.sender.sendMessage(
        'Selecciona la opción deseada:'
        , reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Horarios'), KeyboardButton(text='Tutorías')],
                                                     [KeyboardButton(text='Clases'), KeyboardButton(text='Profesores')],
                                                     [KeyboardButton(text='Fichas docentes')]],resize_keyboard = True))
def horarios(self):
    self.sender.sendMessage('¿Qué horarios quiere ver?:', reply_markup=ReplyKeyboardMarkup(keyboard =
                [[KeyboardButton(text='Horarios curso'), KeyboardButton(text='Horarios clase'),
                 KeyboardButton(text='Volver')]],resize_keyboard = True))

def fichas(self):
    keyboard = [
        [KeyboardButton(text='Fichas de curso completo'),
         KeyboardButton(text='Ficha docente de asignatura'),
         KeyboardButton(text='Volver')]]
    self.sender.sendMessage("¿Qué Fichas docentes quiere ver?:", reply_markup=ReplyKeyboardMarkup(keyboard = keyboard, resize_keyboard = True))

def profesores(self):
    keyboard=[[KeyboardButton(text='Volver')]]
    self.sender.sendMessage("¿De qué profesor quieres saber?:", reply_markup=ReplyKeyboardMarkup(keyboard = keyboard, resize_keyboard = True))

def clases(self):
    keyboard = [[KeyboardButton(text='Volver')]]
    self.sender.sendMessage(text='¿Cuál es la clase sobre la que quieres información?:', reply_markup=ReplyKeyboardMarkup(keyboard = keyboard, resize_keyboard = True))

def seleccionGrado(self):

    self.sender.sendMessage('Selecciona la titulación:', reply_markup=ReplyKeyboardMarkup( keyboard = [
        [KeyboardButton(text='Informática'), KeyboardButton(text='Software'), KeyboardButton(text='Computadores')],
        [KeyboardButton(text='Videojuegos'), KeyboardButton(text='Máster'), KeyboardButton(text='Optativas')]], resize_keyboard = True))


def seleccionCurso(self,grado):
    if grado == 'MI':
        cursos = [[KeyboardButton(text='1'),KeyboardButton(text='2')]]
    elif grado == 'DV':
        cursos = [[KeyboardButton(text='1'),KeyboardButton(text='2'),KeyboardButton(text='3')]]
    elif grado == 'OP':
        cursos = [[KeyboardButton(text='Generales'), KeyboardButton(text='Itinerario A Informática'), KeyboardButton(text='Itinerario B Informática')]]
    else:
        cursos = [[KeyboardButton(text='1'),KeyboardButton(text='2'),KeyboardButton(text='3'),KeyboardButton(text='4')]]

    self.sender.sendMessage("Selecciona el curso:", reply_markup=ReplyKeyboardMarkup(keyboard = cursos, resize_keyboard = True))


def seleccionGrupo(self,grupo):
    keyboard = [
        [KeyboardButton(text='A'), KeyboardButton(text='B'), KeyboardButton(text='C')],
        [KeyboardButton(text='D'), KeyboardButton(text='E'), KeyboardButton(text='F')]]
    self.sender.sendMessage("Selecciona la titulación:", reply_markup=keyboard)


