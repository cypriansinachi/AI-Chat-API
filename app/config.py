from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///.ai-chat-app.db")
XAI_API_KEY = os.getenv("XAI_API_KEY") 