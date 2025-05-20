import os

def fix_postgres_url(url):
    """Fix postgres URL for SQLAlchemy"""
    if not url:
        return None
    # Replace 'postgres://' with 'postgresql://' for SQLAlchemy
    if url.startswith('postgres://'):
        url = url.replace('postgres://', 'postgresql://', 1)
    return url

from tg_bot.sample_config import Config

class Development(Config):
    OWNER_ID = int(os.environ.get('OWNER_ID'))  # Your Telegram ID
    OWNER_USERNAME = os.environ.get('OWNER_USERNAME')  # Your Telegram username
    API_KEY = os.environ.get('TOKEN')  # Bot token from @BotFather
    
    # Fix the DATABASE_URL format for SQLAlchemy
    SQLALCHEMY_DATABASE_URI = fix_postgres_url(os.environ.get('DATABASE_URL'))
    
    MESSAGE_DUMP = os.environ.get('MESSAGE_DUMP', None)
    LOAD = []
    NO_LOAD = ['translation']
    WEBHOOK = bool(os.environ.get('WEBHOOK', False))
    URL = os.environ.get('URL', "")

    # Optional
    SUDO_USERS = []
    SUPPORT_USERS = []
    WHITELIST_USERS = []
    CERT_PATH = None
    PORT = int(os.environ.get('PORT', 5000))
    DEL_CMDS = bool(os.environ.get('DEL_CMDS', True))
    STRICT_GBAN = bool(os.environ.get('STRICT_GBAN', True))
    WORKERS = int(os.environ.get('WORKERS', 8))
    ALLOW_EXCL = bool(os.environ.get('ALLOW_EXCL', True))
