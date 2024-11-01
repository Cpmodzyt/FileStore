#(©)t.me/CodeFlix_Bots




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7616240279:AAEvAzlR7u3pBjYClKtdX1KiOy9bPNpUSOc")
#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "23023343"))
#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "2b79fd2d2c83173807a039325e7e166f")
#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002324232643"))
# NAMA OWNER
OWNER = os.environ.get("OWNER", "Itzmecp")
#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "7717701360"))
#Port
PORT = os.environ.get("PORT", "8030")
#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://interworld:itzmecp@cluster0.jfui5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", ""))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", ""))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

START_PIC = os.environ.get("START_PIC", "https://i.ibb.co/M7X19Qr/file-949.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://i.ibb.co/M7X19Qr/file-949.jpg")

HELP_TXT = "<b>This is a file to link bot work for @Itzmecp \n\n❏ Bot Commands\n├ /start : Start the bot\n├├ /about : Our Information\n /help : Help related to bot\n\n Simply click on the link and start the bot. Join both channels and try again, that’s it!\n\n Developed by <a href=https://t.me/itzmecp>itzmecp</a></b>"
ABOUT_TXT = "<b>◈ ᴄʀᴇᴀᴛᴏʀ: <a href=https://t.me/Itzmecp>Itzmecp</a>\n◈ ꜰᴏᴜɴᴅᴇʀ ᴏꜰ : <a href=https://t.me/otakuflix_network>I n t e r W o r l d</a></b>"
START_MSG = os.environ.get("START_MESSAGE", "<b>Kon'nichiwa ! {first}\n\n I am File Store Bot. I can store private files in a specified channel, and other users can access it from a special link.</b>")
try:
    ADMINS=[6376328008]
    for x in (os.environ.get("ADMINS", "5115691197 6273945163 6103092779 5231212075").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {first}\n\n<b>ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ʀᴇʟᴏᴀᴅ button ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛᴇᴅ ꜰɪʟᴇ.</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>• ʙʏ @CloudXcpbot</b>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "Bakka! You are not my senpai!!"

ADMINS.append(OWNER_ID)
ADMINS.append(6497757690)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
