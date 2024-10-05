import os

# Required Variables Config
API_ID = int(os.environ.get("API_ID", "24817837"))
API_HASH = os.environ.get("API_HASH", "acd9f0cc6beb08ce59383cf250052686")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7433809622:AAGc38HRdxVBKOnNB_Icthe-LE54KYL05Yc")
ADMIN = int(os.environ.get("ADMIN", "1740287480"))


# Premium 4GB Renaming Client Config
STRING_SESSION = os.environ.get("STRING_SESSION", "BAF6sK0ANhri1hJxsLan3dILfANjI3vQM3mRA0BAmxXOAxOuIF3JgW1XM6SWH-H-r2jYBwlFJyC1IRp7qFJ6s2MpBxN804-HDuQml6GsQOCjz9TRzTrMnEkvCWBSUwpK9UZOjOYkyMVOUo5ZQqcNhOYjMcWcuURajhHBDO-NRwq5JCu1b-QN9gFklgo9g08dtXMGXSuvrBWYmTrg1PiJKsGqu8ZtvdPWEVAGWFBRXAKA08gHWs3TRUC9EZtCm9sFr7u0x07AGeCAcaieaPKwMJJzg4JI-SVSYikAeb7yvOriJjdUTXJv-xbloMX9l2ic8IFZF4jbfLC0YSn21gsJPMlgvHAi1gAAAAG6xrWUAA")


# Log & Force Channel Config
FORCE_SUBS = os.environ.get("FORCE_SUBS", "Aniflix_Network")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002151954601"))


# Mongo DB Database Config
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://mhsm:mhsm@cluster0.j9figvh.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "majority")


# Other Variables Config
START_PIC = os.environ.get("START_PIC", "https://envs.sh/08i.jpg")
