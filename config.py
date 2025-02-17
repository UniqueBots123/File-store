import os

class Config:
    API_ID = int(os.getenv("API_ID", "123456"))  
    API_HASH = os.getenv("API_HASH", "your_api_hash")  
    BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token")  
    MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://your_mongodb_uri")  
    DATABASE_NAME = os.getenv("DATABASE_NAME", "FileStoreBot")  
    LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "-1001234567890"))  
    FORCE_SUB_CHANNEL = os.getenv("FORCE_SUB_CHANNEL", "your_channel_username")  
    ADMINS = [int(x) for x in os.getenv("ADMINS", "").split()]  

    AUTO_DELETE_DURATION = int(os.getenv("AUTO_DELETE_DURATION", "180"))  # Default 3 hours
    AUTO_DELETE_ENABLED = os.getenv("AUTO_DELETE_ENABLED", "True").lower() == "true"

    SHORTENER_API = os.getenv("SHORTENER_API", "your_shortener_api_key")
    AD_TOKEN_SYSTEM = os.getenv("AD_TOKEN_SYSTEM", "True").lower() == "true"

    PREMIUM_USERS = []
