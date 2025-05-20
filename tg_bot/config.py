import os
from tg_bot.sample_config import Config

class Development(Config):
    OWNER_ID = int(os.environ.get('OWNER_ID'))  # Your Telegram ID
    OWNER_USERNAME = os.environ.get('OWNER_USERNAME')  # Your Telegram username
    API_KEY = os.environ.get('TOKEN')  # Bot token from @BotFather
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')  # Database URL from Railway
    MESSAGE_DUMP = os.environ.get('MESSAGE_DUMP', None)  # Channel/Group ID for logging
    LOAD = []
    NO_LOAD = ['translation']
    WEBHOOK = bool(os.environ.get('WEBHOOK', False))
    URL = os.environ.get('URL', "")

    # Optional
    SUDO_USERS = []  # List of ID's - (not usernames)
    SUPPORT_USERS = []  # List of ID's - (not usernames)
    WHITELIST_USERS = []  # List of ID's - (not usernames)
    CERT_PATH = None
    PORT = int(os.environ.get('PORT', 5000))
    DEL_CMDS = bool(os.environ.get('DEL_CMDS', True))
    STRICT_GBAN = bool(os.environ.get('STRICT_GBAN', True))
    WORKERS = int(os.environ.get('WORKERS', 8))
    ALLOW_EXCL = bool(os.environ.get('ALLOW_EXCL', True))
