# -*- coding: utf-8 -*-
import telepot
from chatterbot import ChatBot
from trainers import training_profesores as t_p
from trainers import training_asignaturas as t_a
from telegram import bot_telegram as bots
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from telepot.delegate import (
    per_chat_id, per_callback_query_origin, create_open, pave_event_space)
#from alexa import run as RunAlexaService

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


def main():
	
	print("Type something to begin...")
	
	#t = t_p.training_profesores(chatbot)

	#a = t_a.training_asignaturas(chatbot)
	 
	#a.trainingAsignaturaInfo()
	#a.trainingAsignaturaProfesores()
	#a.trainingAsignaturaClases()
	#a.trainingAsignaturaFichaDocente()
	# The following loop will execute each time the user enters input
	

	"""
	while True:
	    try:
	        # We pass None to this method because the parameter
	        # is not used by the TerminalAdapter
	        bot_input = chatbot.get_response(None)
	    # Press ctrl-c or ctrl-d on the keyboard to exit
	    except (KeyboardInterrupt, EOFError, SystemExit):
	        break
	
	# Get a response for some unexpected input
	
	print("has")
	response = chatbot.get_response('lista de profesores')
	print(response)
	"""


if __name__ == "__main__":
    main()

