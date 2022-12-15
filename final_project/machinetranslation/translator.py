import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('zm0SsoHKtWJOTWaFL-lv2ogQknuFAg0Njs7azE0DT9qV')
language_translator = LanguageTranslatorV3(
    version = '2018-05-01',
    authenticator = authenticator
)

language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/5abaec3f-3c30-4106-a76b-08e3ebb90587')

def englishToFrench(english_text):
    ''' Translate English to French '''
    french_text = language_translator.translate(
    text = english_text,
    model_id = 'en-fr').get_result()
    french_text = french_text['translations'][0]['translation']
    return english_text['translations'][0]['translation']    

def frenchToEnglish(french_text):
    ''' Translate French to English '''
    english_text = language_translator.translate(
    text = french_text,
    model_id = 'fr-en').get_result()
    english_text = english_text['translations'][0]['translation']
    return english_text['translations'][0]['translation']    
