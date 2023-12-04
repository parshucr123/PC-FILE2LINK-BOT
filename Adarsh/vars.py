# (c) adarsh-goel
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', '20268838'))
    API_HASH = str(getenv('API_HASH', '908e732e523a2fa88cb2599873c98eb1'))
    BOT_TOKEN = str(getenv('BOT_TOKEN', "6638886131:AAE2gB4ZC6649RpNIJmRO0GoqhMNhOXawF0"))
    name = str(getenv('name', 'filetolinkbot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1001936136684'))
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "1474382506").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = str(getenv('APP_NAME', 'pcfile2link'))
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', 'parshucr'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME', 'pcfile2link'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', "mongodb+srv://ladykiller2:ladykiller2@cluster0.eezeovn.mongodb.net/?retryWrites=true&w=majority"))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', 'pcnewmoviez'))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001362659779")).split())) 
