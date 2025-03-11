# === DATABASE SETTINGS ===
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///default.db")  # Use ENV or default


# === FLASK SETTINGS ===
FLASK_ENV=development
DEBUG=True
SECRET_KEY=

# === BOT SETTINGS ===
BOT_API_KEY=  # Your API key for bot authentication
SCRAPER_USER_AGENT=from fake_useragent import UserAgent

ua = UserAgent()
SCRAPER_USER_AGENT = ua.random  # Generates a new user agent every run

print(f"Using User-Agent: {SCRAPER_USER_AGENT}")  # Debugging output

SCRAPER_TIMEOUT=10

# === CLOUD & DEPLOYMENT ===
GITHUB_CLIENT_ID=
GITHUB_CLIENT_SECRET=
VERCEL_PROJECT_ID=
VERCEL_ORG_ID=
VERCEL_TOKEN=

# === WEBSITE CONFIG ===
FRONTEND_URL=http://127.0.0.1:3000
BACKEND_URL=http://127.0.0.1:5000

# === AUTH ===
JWT_SECRET=
JWT_ALGORITHM=HS256
