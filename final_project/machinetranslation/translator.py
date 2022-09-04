import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
version = os.environ['version']
url = os.environ['url']

authenticator = IAMAuthenticator(f'{apikey}')
language_translator = LanguageTranslatorV3(
    version=f'{version}',
    authenticator=authenticator
)

language_translator.set_service_url(f'{url}')
language_translator.set_disable_ssl_verification(True)


def english_to_french(eng_text):
    translation_dict = language_translator.translate(
        text=eng_text, model_id='en-fr').get_result()
    return translation_dict.get('translations')[0].get('translation')


def french_to_english(fr_text):
    translation_dict = language_translator.translate(
        text=fr_text, model_id='fr-en').get_result()
    return translation_dict.get('translations')[0].get('translation')
