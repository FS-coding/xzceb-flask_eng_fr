"""
My final project
"""
#import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

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
    """
    Translates English text to French
    """
    try:
        french_text = language_translator.translate(
            text=english_text, model_id='en-fr').get_result()
    except Exception:
        return ''
    french_text = french_text['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """
    Translates French text to English
    """
    try:
        english_text = language_translator.translate(
            text=french_text, model_id='fr-en').get_result()
    except Exception:
        return ''
    english_text = english_text['translations'][0]['translation']
    return english_text

# TEXT='Hello'
# french=english_to_french(text)
# print(french)
# english=french_to_english(french)
# print(english)
