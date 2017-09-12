#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Charter Skill for Alexa.

TBC.

"""

import logging

from flask import Flask
from flask_ask import Ask, question, statement
import trio

app = Flask('Charter')
ask = Ask(app, "/")


def run(debug):
    """
    
    :return: 
    """

    if debug:
        logging.getLogger('flask_ask').setLevel(logging.DEBUG)

    app.run(debug=debug, host='0.0.0.0')


# Mandatory Intents.

@ask.launch
def launch_intent():
    """
    
    :return: 
    """

    speech_text = "Hi, I'm Charter. Would you like to chat?"

    reprompt_text = "Sorry, I didn't get that. Would you like to chat?"

    response = question(speech_text).reprompt(reprompt_text)

    return response


@ask.intent('AMAZON.HelpIntent')
def help_intent():
    """
    
    :return: 
    """

    speech_text = "I'm Charter, a conversational, machine learning " \
                  "infrastructure automation bot. I've sent a link to my " \
                  "documentation to your Alexa app."

    card_text = "As promised, here's my documentation: " \
                "https://petel.io/products/charter"

    response = statement(speech_text).simple_card('Charter', card_text)

    return response


@ask.session_ended
def end_intent():
    """
    
    :return: 
    """

    return statement('')


# Custom Intents.

@ask.intent('CapReport')
def capreport_intent():
    """
    
    :return: 
    """

    speech_text = "Okay! I'll create a new capacity report and send the link " \
                  "to your Alexa app once it's ready."

    response = statement(speech_text).simple_card('Charter', speech_text)

    return response


@ask.intent('Repeat')
def repeat_intent(name):
    """

    :return: 
    """

    speech_text = "You said {}!".format(name)

    response = statement(speech_text).simple_card('Charter', speech_text)

    return response
