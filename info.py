import re, logging
from os import environ
from Script import script
from dotenv import load_dotenv
load_dotenv()


id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID'))
API_HASH = environ.get('API_HASH')
BOT_TOKEN = environ.get('BOT_TOKEN')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

PICS = (environ.get('PICS', 'https://telegra.ph/file/078fe6cc7020a1a65ef32.jpg')).split()
NOR_IMG = environ.get("NOR_IMG", "https://telegra.ph/file/c6f580f8acff147dbb670.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://telegra.ph/file/9485c9f7ddb31b30a44d1.mp4")
SPELL_IMG = environ.get("SPELL_IMG", "https://telegra.ph/file/5f76bef8f118ac406e40c.jpg")

# Admins, Channels & User
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_grp = environ.get('AUTH_GROUP')
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID')
reqst_channel = environ.get('REQST_CHANNEL_ID')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None

#Downloader
DOWNLOAD_LOCATION = environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/AudioBoT/")

# This is required for the plugins involving the file system.
TMP_DOWNLOAD_DIRECTORY = environ.get("TMP_DOWNLOAD_DIRECTORY", "./DOWNLOADS/")

# Open AI
OPENAI_API = environ.get('OPENAI_API', '0')
if len(OPENAI_API) == 0:
    logging.warning('OPENAI_API is empty')
    exit()

# Command
COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "/")

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Nobideveloper")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# stickers
STICKERS = (environ.get('STICKERS', 'CAACAgUAAxkBAAPwZWxKvJUQjpvQlTEz_D4djAThehUAAhMAA8r5GjSPvfvuL-YcEB4E')).split()

# FSUB
auth_channel = environ.get('AUTH_CHANNEL')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
# Set to False inside the bracket if you don't want to use Request Channel else set it to Channel ID
REQ_CHANNEL = environ.get("REQ_CHANNEL", "")
REQ_CHANNEL = int(REQ_CHANNEL) if REQ_CHANNEL and id_pattern.search(REQ_CHANNEL) else False
JOIN_REQS_DB = environ.get("JOIN_REQS_DB", DATABASE_URI)

#Auto approve 
CHAT_ID = [int(app_chat_id) if id_pattern.search(app_chat_id) else app_chat_id for app_chat_id in environ.get('CHAT_ID', '').split()]
TEXT = environ.get("APPROVED_WELCOME_TEXT", "<b>{mention},\n\nʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ᴛᴏ ᴊᴏɪɴ {title} ɪs ᴀᴘᴘʀᴏᴠᴇᴅ.</b>")
APPROVED = environ.get("APPROVED_WELCOME", "on").lower()

# Others
IS_VERIFY = bool(environ.get('IS_VERIFY', False))
VERIFY2_URL = environ.get('VERIFY2_URL', "tnshort.net")
VERIFY2_API = environ.get('VERIFY2_API', "f7dc286d04be9c25b6f42433609019512043af08")
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'onepagelink.in')
SHORTLINK_API = environ.get('SHORTLINK_API', 'a192c594a6c1f799ceea2539fe833c8dd07cdda7')
IS_SHORTLINK = bool(environ.get('IS_SHORTLINK', True))
NO_RESULTS_MSG = bool(environ.get('NO_RESULTS_MSG', True))
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
MAX_B_TN = environ.get("MAX_B_TN", "8")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
PORT = environ.get("PORT", "8080")
S_GROUP = environ.get('S_GROUP',"https://telegram.me/SHProSearchbot")
RUL_LNK = environ.get('RUL_LNK',"https://graph.org/%F0%9D%97%A0%F0%9D%9E%93%F0%9D%97%A6%F0%9D%97%A7%F0%9D%9E%9D%F0%9D%97%A5-02-15")
MAIN_CHANNEL = environ.get('MAIN_CHANNEL',"https://telegram.me/SHProSearchbot")
GRP_LNK = environ.get('GRP_LNK', 'https://telegram.me/SHProSearchbot')
CHNL_LNK = environ.get('CHNL_LNK', 'https://telegram.me/SH_OTT')
OWN_LNK = environ.get('S_GROUP',"https://telegram.me/SHProSearchbot")
MVG_LNK = environ.get('S_GROUP',"https://telegram.me/SHProSearchbot")
MSG_ALRT = environ.get('MSG_ALRT', 'ꜱʜᴀʀᴇ  ᴀɴᴅ  ꜱᴜᴘᴘᴏʀᴛ  ᴜꜱ')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', ''))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'SHprosearchbot')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "False")), False)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", None)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

LANGUAGES = ["hindi", "hin", "tamil", "tam", "telugu", "tel", "english", "eng", "kannada", "kan", "malayalam", "mal"]
TUTORIAL = environ.get('TUTORIAL', 'https://t.me/Howto_openthislink/4')
IS_TUTORIAL = bool(environ.get('IS_TUTORIAL', True))

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
