from os import environ

class Config(object):
  MAX_RESULT = 50 
  SORTING = 'lastUpdatedDate'
  CATEGORY = 'cs.AI'
  PREFIX = 'cat'
  GPT3_ACTIVATED = False
  OPENAI_API_KEY = environ.get('OPENAI_API_KEY')
    
class DevConfig(Config):
  INDEX = environ.get('DEV_OSEARCH_INDEX')
  OSEARCH_HOST = environ.get('DEV_OSEARCH_HOST')
  OSEARCH_PORT = environ.get('DEV_OSEARCH_PORT')
  OSEARCH_AUTH = (environ.get('DEV_OSEARCH_USERNAME'), environ.get('DEV_OSEARCH_PASSWORD')) 
  CA_CERTS_PATH = environ.get('CA_CERTS_PATH') 
    