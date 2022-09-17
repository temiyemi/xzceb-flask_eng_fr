"""Translator service utilising IBM Language Translator APIs to
translate texts from English to French, or vice versa"""

import json
import os
from dotenv import load_dotenv
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import LanguageTranslatorV3

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)

language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """Returns the French translation of english_text"""
    french_text = None
    if english_text:
        response = language_translator.translate(
                    text=english_text,
                    model_id='en-fr'
                    ).get_result()
        french_text = response['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """Returns the English translation of french_text"""
    english_text = None
    if french_text:
        response = language_translator.translate(
                    text=french_text,
                    model_id='fr-en'
                    ).get_result()
        english_text = response['translations'][0]['translation']
    return english_text
