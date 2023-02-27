from os import environ

class Config(object):
  MAX_RESULT = 50 
  SORTING = 'lastUpdatedDate'
  CATEGORY = 'cs.AI'
  PREFIX = 'cat'
  GPT3_ACTIVATED = False
    
class DevConfig(Config):
  DEV_INDEX = environ.get('DEV_OSEARCH_INDEX')
  DEV_OSEARCH_HOST = environ.get('DEV_OSEARCH_HOST')
  DEV_OSEARCH_PORT = environ.get('DEV_OSEARCH_PORT')
  DEV_OSEARCH_AUTH = (environ.get('DEV_OSEARCH_USERNAME'), environ.get('DEV_OSEARCH_PASSWORD')) 
  DEV_CA_CERTS_PATH = environ.get('CA_CERTS_PATH') 
    