import os

# Required Variables Config
API_ID = int(os.environ.get("API_ID", "24817837"))
API_HASH = os.environ.get("API_HASH", "acd9f0cc6beb08ce59383cf250052686")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7433809622:AAGc38HRdxVBKOnNB_Icthe-LE54KYL05Yc")
ADMIN = int(os.environ.get("ADMIN", "1740287480"))


# Premium 4GB Renaming Client Config
STRING_SESSION = os.environ.get("STRING_SESSION", "BQAAxJIAwxT4xmF7CEWq7wdHCBSZSomUQLOaOgzjZWV9HS0l6EiqOmBFYHjLMQRoFJRTMKdafxHJ3uwaRoUqBIQHGfqt6Jf93xvdNlKq-Lm1k1M3xxHElpg4sdfny0FOvbWgmnd5oOMiWSsSXllTNkXJYwIrdVgkgtzyKYP14WrNBWwGo2DmJde5WAF2ttniWDmEZp9h4hj0Y1_6ADOoMfdFczxrbeTNyFv6I0_J60qvDspwdHA1LG7slMau6CMNn7XiWJfb_gtI_ALlgdykOEIoaJdgXj-ZMq68GGPa7NSXhieflZ80dHs--sBnN2Ie5iVKxcywJBIVc7xVOgZq6vcTxMGrswAAAABnuq34AA")


# Log & Force Channel Config
FORCE_SUBS = os.environ.get("FORCE_SUBS", "Aniflix_Network")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002151954601"))


# Mongo DB Database Config
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://mhsm:mhsm@cluster0.j9figvh.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "majority")


# Other Variables Config
START_PIC = os.environ.get("START_PIC", "https://envs.sh/08i.jpg")
