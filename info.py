# Don't Remove Credit @VJ_Botz

# Subscribe YouTube Channel For Amazing Bot @Tech_VJ

# Ask Doubt on telegram @AV_King1

import re

from os import environ

from Script import script 

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'TechVJBot')

API_ID = int(environ.get('API_ID', '16402669'))

API_HASH = environ.get('API_HASH', 'e50b6c6e9dc8077ec3e9db0e565631e4')

BOT_TOKEN = environ.get('BOT_TOKEN', "")

# This Pictures Is For Start Message Picture, You Can Add Multiple By Giving One Space Between Each.

PICS = (environ.get('PICS', 'https://i.ibb.co/h9GBt42/file-6320.jpg https://i.ibb.co/n30XbDd/file-2317.jpg https://i.ibb.co/4fDd5BK/file-2317.jpg https://i.ibb.co/8dTrcPy/file-2319.jpg https://i.ibb.co/F41g7Hh/file-2320.jpg https://i.ibb.co/jh1HK8Q/file-2321.jpg https://i.ibb.co/CJ8XVjM/file-2322.jpg https://i.ibb.co/dcmyNnw/file-2323.jpg https://i.ibb.co/KLyrR0f/file-2324.jpg https://i.ibb.co/52gQ6g4/file-2325.jpg https://i.ibb.co/vZWTsCn/file-2326.jpg https://i.ibb.co/WHHkRgj/file-2327.jpg https://i.ibb.co/YBnjXZb/file-2328.jpg https://i.ibb.co/7YtFPC7/file-2329.jpg https://i.ibb.co/D1r9Dcc/file-2331.jpg https://i.ibb.co/jgF3LBq/file-2332.jpg')).split()

# Admins & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6570474744').split()] # For Multiple Id Use One Space Between Each.

auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]  # For Multiple Id Use One Space Between Each.

AUTH_USERS = (auth_users + ADMINS) if auth_users else []

# This Channel Is For When User Start Your Bot Then Bot Send That User Name And Id In This Log Channel, Same For Group Also.

LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002232668601'))

# This Is File Channel Where You Upload Your File Then Bot Automatically Save It In Database 

CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002046155403').split()]  # For Multiple Id Use One Space Between Each.

# auth_channel means force subscribe channel.

# if REQUEST_TO_JOIN_MODE is true then force subscribe work like request to join fsub, else if false then work like normal fsub.

REQUEST_TO_JOIN_MODE = bool(environ.get('REQUEST_TO_JOIN_MODE', False)) # Set True Or False

TRY_AGAIN_BTN = bool(environ.get('TRY_AGAIN_BTN', False)) # Set True Or False (This try again button is only for request to join fsub not for normal fsub)

# This Is Force Subscribe Channel, also known as Auth Channel 

auth_channel = environ.get('AUTH_CHANNEL', '-1002006400723') # give your force subscribe channel id here else leave it blank

AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None

# This Channel Is For When User Request File With command or hashtag like - /request or #request

reqst_channel = environ.get('REQST_CHANNEL_ID', '-1002421169275')

REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None

# This Is Your Bot Support Group Id , Here Bot Will Not Give File Because This Is Support Group.

support_chat_id = environ.get('SUPPORT_CHAT_ID', '-1002397537869')

SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None

# This Channel Is For Index Request 

INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))

# This Channel Is For /batch command file store.

FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1002338165303')).split()]  # For Multiple Id Use One Space Between Each.

# This Channel Is For Delete Index File, Forward Your File In This Channel Which You Want To Delete Then Bot Automatically Delete That File From Database.

DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '-1002445547306').split()]  # For Multiple Id Use One Space Between Each.

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://mrnoffice692:PsO4VGHI9heKd7WA@cluster0.o1vcj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")   # IF Multiple Database Is False Then Fill Only This Database Url.

DATABASE_NAME = environ.get('DATABASE_NAME', "mrnoffice692")

COLLECTION_NAME = environ.get('COLLECTION_NAME', 'vjcollection')

MULTIPLE_DATABASE = bool(environ.get('MULTIPLE_DATABASE', False)) # Set True or False

# If Multiple Database Is True Then Fill All Three Below Database Uri Else You Will Get Error.

O_DB_URI = environ.get('O_DB_URI', "")   # This Db Is For Other Data Store

F_DB_URI = environ.get('F_DB_URI', "")   # This Db Is For File Data Store

S_DB_URI = environ.get('S_DB_URI', "")   # This Db is for File Data Store When First Db Is Going To Be Full.

# Premium And Referal Settings
PREMIUM_AND_REFERAL_MODE = bool(environ.get('PREMIUM_AND_REFERAL_MODE', True)) # Set Ture Or False

# If PREMIUM_AND_REFERAL_MODE is True Then Fill Below Variable, If Flase Then No Need To Fill.

REFERAL_COUNT = int(environ.get('REFERAL_COUNT', '10')) # number of referal count

REFERAL_PREMEIUM_TIME = environ.get('REFERAL_PREMEIUM_TIME', '1month') # time in week, day, month.

PAYMENT_QR = environ.get('PAYMENT_QR', 'https://graph.org/file/47fed40f71a411a00e656-ac50cff8e8e973067d.jpg') # payment code picture url.

PAYMENT_TEXT = environ.get('PAYMENT_TEXT', '<b><blockquote>💰💳𝐇𝐞𝐲 𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𝐏𝐥𝐚𝐧𝐬 💲</blockquote>\n\n<blockquote>𝗣𝗿𝗲𝗺𝗶𝘂𝗺 𝗙𝗲𝗮𝘁𝘂𝗿𝗲</blockquote>\n\n<blockquote> ⭑⚝ 𝗪𝗶𝘁𝗵𝗼𝘂𝘁 𝗮𝗱𝘀\n    ๋࣭ ⭑⚝ 𝗡𝗼 𝘃𝗲𝗿𝗶𝗳𝗶𝗰𝗮𝘁𝗶𝗼𝗻\n    ๋࣭ ⭑⚝ 𝗗𝗶𝗿𝗲𝗰𝘁 𝗱𝗼𝘄𝗻𝗹𝗼𝗮𝗱 𝘁𝗼 𝗰𝗵𝗿𝗼𝗺𝗲\n    ๋࣭ ⭑⚝ 𝗗𝗶𝗿𝗲𝗰𝘁 𝗽𝗹𝗮𝘆 𝗶𝗻 𝘃𝗹𝗰/𝗺𝘅-𝗽𝗹𝗮𝘆𝗲𝗿 𝗮𝗻𝗱 𝗺𝗼𝗿𝗲 𝗽𝗹𝗮𝘆𝗲𝗿 𝗮𝘃𝗮𝗶𝗹𝗮𝗯𝗹𝗲\n    ๋࣭ ⭑⚝ 𝗙𝘂𝗹𝗹 𝗔𝗱𝗺𝗶𝗻 𝘀𝘂𝗽𝗽𝗼𝗿𝘁\n    ๋࣭ ⭑⚝ 𝗛𝗶𝗴𝗵 𝘀𝗽𝗲𝗲𝗱 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱\n    ๋࣭ ⭑⚝ 𝗧𝗩 𝗦𝗲𝗿𝗶𝗮𝗹𝘀\n    ๋࣭ ⭑⚝ 𝗡𝗲𝘄/𝗢𝗹𝗱 𝗠𝗼𝘃𝗶𝗲𝘀 𝗮𝗻𝗱 𝗦𝗲𝗿𝗶𝗲𝘀\n    ๋࣭ ⭑⚝ 𝗥𝗲𝗾𝘂𝗲𝘀𝘁 𝘄𝗶𝗹𝗹 𝗯𝗲 𝗰𝗼𝗺𝗽𝗹𝗲𝘁𝗲𝗱 𝗶𝗻 𝟭 𝗵𝗼𝘂𝗿 𝗶𝗳 𝗮𝘃𝗮𝗶𝗹𝗮𝗯𝗹𝗲｡</blockquote>\n\n<blockquote>   𝗔𝗹𝗹 𝗣𝗿𝗶𝗰𝗲 𝗟𝗶𝘀𝘁</blockquote>\n\n<blockquote>╭━━━━━━━━╮\n   • ₹10 - 1 Week\n   • ₹30 - 1 Month\n   • ₹60 - 2 Months\n   • ₹90 - 3 Months\n   • ₹120 - 7 months\n╰━━━━━━━━╯</blockquote>\n\n<blockquote>   ᴄᴏᴘʏ ᴛʜɪs ᴜᴘɪ ɪᴅ</blockquote>\n   ᴜᴘɪ ɪᴅ ➢ <code>abhishek.kumar6395@fam</code>\n\n<blockquote>⚠️𝗦𝗲𝗻𝗱 𝗦𝗦 𝗔𝗳𝘁𝗲𝗿 𝗣𝗮𝘆𝗺𝗲𝗻𝘁⚠️ 𝗔𝗳𝘁𝗲𝗿 𝘀𝗲𝗻𝗱𝗶𝗻𝗴 𝗮 𝗦𝗰𝗿𝗲𝗲𝗻𝘀𝗵𝗼𝘁 𝗽𝗹𝗲𝗮𝘀𝗲 𝗴𝗶𝘃𝗲 𝘂𝘀 𝘀𝗼𝗺𝗲 𝘁𝗶𝗺𝗲 𝘁𝗼 𝗮𝗱𝗱 𝘆𝗼𝘂 𝗶𝗻 𝘁𝗵𝗲 𝗽𝗿𝗲𝗺𝗶𝘂𝗺 𝘃𝗲𝗿𝘀𝗶𝗼𝗻｡｡</blockquote></b>')

# Clone Information : If Clone Mode Is True Then Bot Clone Other Bots.

CLONE_MODE = bool(environ.get('CLONE_MODE', False)) # Set True or False

CLONE_DATABASE_URI = environ.get('CLONE_DATABASE_URI', "") # Necessary If clone mode is true

PUBLIC_FILE_CHANNEL = environ.get('PUBLIC_FILE_CHANNEL', 'MZAUTOFILTER') # Public Channel Username Without @ or without https://t.me/ and Bot Is Admin With Full Right.

# Links
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/Movies_World_Request_Group_hdx')

CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/MOVIES_WORLDZS')

SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'Movies_World_Support_Group') # Support Chat Link Without https:// or @

OWNER_LNK = environ.get('OWNER_LNK', 'https://t.me/AV_King1')

# True Or False
AI_SPELL_CHECK = bool(environ.get('AI_SPELL_CHECK', True))

PM_SEARCH = bool(environ.get('PM_SEARCH', True))

BUTTON_MODE = bool(environ.get('BUTTON_MODE', False))

MAX_BTN = bool(environ.get('MAX_BTN', False))

IS_TUTORIAL = bool(environ.get('IS_TUTORIAL', False))

IMDB = bool(environ.get('IMDB', False))

AUTO_FFILTER = bool(environ.get('AUTO_FFILTER', True))

AUTO_DELETE = bool(environ.get('AUTO_DELETE', True))

LONG_IMDB_DESCRIPTION = bool(environ.get("LONG_IMDB_DESCRIPTION", False))

SPELL_CHECK_REPLY = bool(environ.get("SPELL_CHECK_REPLY", True))

MELCOW_NEW_USERS = bool(environ.get('MELCOW_NEW_USERS', True))

PROTECT_CONTENT = bool(environ.get('PROTECT_CONTENT', False))

PUBLIC_FILE_STORE = bool(environ.get('PUBLIC_FILE_STORE', True))

NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", False))

USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

# Token Verification Info :

VERIFY = bool(environ.get('VERIFY', False))

VERIFY_SHORTLINK_URL = environ.get('VERIFY_SHORTLINK_URL', '')

VERIFY_SHORTLINK_API = environ.get('VERIFY_SHORTLINK_API', '')

VERIFY_TUTORIAL = environ.get('VERIFY_TUTORIAL', '')

# If You Fill Second Shortner Then Bot Attach Both First And Second Shortner And Use It For Verify.

VERIFY_SECOND_SHORTNER = bool(environ.get('VERIFY_SECOND_SHORTNER', False))

# if verify second shortner is True then fill below url and api

VERIFY_SND_SHORTLINK_URL = environ.get('VERIFY_SND_SHORTLINK_URL', '')

VERIFY_SND_SHORTLINK_API = environ.get('VERIFY_SND_SHORTLINK_API', '')

# Shortlink Info

SHORTLINK_MODE = bool(environ.get('SHORTLINK_MODE', False)) # Set True Or False

SHORTLINK_URL = environ.get('SHORTLINK_URL', '')

SHORTLINK_API = environ.get('SHORTLINK_API', '')

TUTORIAL = environ.get('TUTORIAL', '') # How Open Shortner Link Video Link , Channel Link Where You Upload Your Video.

# Others
CACHE_TIME = int(environ.get('CACHE_TIME', 1800))

MAX_B_TN = environ.get("MAX_B_TN", "10")

PORT = environ.get("PORT", "8080")

MSG_ALRT = environ.get('MSG_ALRT', 'Hello My Dear Friends ❤️')

CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")

BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)

IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")

MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)

# Choose Option Settings 
LANGUAGES = ["malayalam", "mal", "tamil", "tam" ,"english", "eng", "hindi", "hin", "telugu", "tel", "kannada", "kan"]

SEASONS = ["season 1", "season 2", "season 3", "season 4", "season 5", "season 6", "season 7", "season 8", "season 9", "season 10"]

EPISODES = ["E01", "E02", "E03", "E04", "E05", "E06", "E07", "E08", "E09", "E10", "E11", "E12", "E13", "E14", "E15", "E16", "E17", "E18", "E19", "E20", "E21", "E22", "E23", "E24", "E25", "E26", "E27", "E28", "E29", "E30", "E31", "E32", "E33", "E34", "E35", "E36", "E37", "E38", "E39", "E40"]

QUALITIES = ["360p", "480p", "720p", "1080p", "1440p", "2160p"]

YEARS = ["1900", "1991", "1992", "1993", "1994", "1995", "1996", "1997", "1998", "1999", "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025"]


                           # Don't Remove Credit @VJ_Botz

                           # Subscribe YouTube Channel For Amazing Bot @Tech_VJ

                           # Ask Doubt on telegram @AV_King1


# Online Stream and Download
STREAM_MODE = bool(environ.get('STREAM_MODE', True)) # Set True or False

# If Stream Mode Is True Then Fill All Required Variable, If False Then Don't Fill.

MULTI_CLIENT = False

SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))

PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes

if 'DYNO' in environ:

    ON_HEROKU = True

else:

    ON_HEROKU = False

URL = environ.get("URL", "https://ultimate-kally-123456789123456789123456789123456789pro-18b66409.koyeb.app/")

# Rename Info : If True Then Bot Rename File Else Not

RENAME_MODE = bool(environ.get('RENAME_MODE', True)) # Set True or False

# Auto Approve Info : If True Then Bot Approve New Upcoming Join Request Else Not

AUTO_APPROVE_MODE = bool(environ.get('AUTO_APPROVE_MODE', False)) # Set True or False

# Start Command Reactions
REACTIONS = ["🤝", "😇", "🤗", "😍", "👍", "🎅", "😐", "🥰", "🤩", "😱", "🤣", "😘", "👏", "😛", "😈", "🎉", "⚡️", "🫡", "🤓", "😎", "🏆", "🔥", "🤭", "🌚", "🆒", "👻", "😁"] #don't add any emoji because tg not support all emoji reactions

if MULTIPLE_DATABASE == False:

    USER_DB_URI = DATABASE_URI

    OTHER_DB_URI = DATABASE_URI

    FILE_DB_URI = DATABASE_URI

    SEC_FILE_DB_URI = DATABASE_URI

else:

    USER_DB_URI = DATABASE_URI    # This Db is for User Data Store

    OTHER_DB_URI = O_DB_URI       # This Db Is For Other Data Store

    FILE_DB_URI = F_DB_URI        # This Db Is For File Data Store

    SEC_FILE_DB_URI = S_DB_URI    # This Db is for File Data Store When First Db Is Going To Be Full.

# Don't Remove Credit @AV_King1

# Subscribe YouTube Channel For Amazing Bot @AV_King1

# Ask Doubt on telegram @AV_King1
