import os

class Config(object):
    LOGGER = True
    
    # REQUIRED
    API_KEY = os.environ.get('TOKEN', None)
    OWNER_ID = int(os.environ.get('OWNER_ID', None))  # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = os.environ.get('OWNER_USERNAME', None)

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', None)
    MESSAGE_DUMP = os.environ.get('MESSAGE_DUMP', None)  # needed to make sure 'save from' messages persist
    LOAD = []
    NO_LOAD = ['translation']
    WEBHOOK = bool(os.environ.get('WEBHOOK', False))
    URL = os.environ.get('URL', "")  # Does not contain token

    # OPTIONAL
    SUDO_USERS = []  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = []  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = []  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    DONATION_LINK = None
    CERT_PATH = None
    PORT = int(os.environ.get('PORT', 5000))
    DEL_CMDS = bool(os.environ.get('DEL_CMDS', False))
    STRICT_GBAN = bool(os.environ.get('STRICT_GBAN', False))
    WORKERS = int(os.environ.get('WORKERS', 8))
    BAN_STICKER = 'CAADAgADOwADPPEcAXkko5EB3YGYAg'  # banhammer marie sticker
    ALLOW_EXCL = bool(os.environ.get('ALLOW_EXCL', False))
    CUSTOM_CMD = bool(os.environ.get('CUSTOM_CMD', True))
    API_WEATHER = None
    WALL_API = None
    STRICT_GMUTE = bool(os.environ.get('STRICT_GMUTE', False))

class Development(Config):
    LOGGER = True
