# Kawaii-watchlist-bot
# 🎌 Anime Watchlist Bot — Setup Guide

## 📦 Installation

```bash
# 1. Python install karo (3.10+)
# 2. Dependencies install karo
pip install -r requirements.txt
```

## ⚙️ Configuration

`config.py` file kholo aur yeh 2 cheezein change karo:

```python
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"   # ← @BotFather se lo
ADMIN_IDS = [YOUR_TELEGRAM_USER_ID] # ← apna ID dalo
```

### Bot Token kaise milega?
1. Telegram mein **@BotFather** ko open karo
2. `/newbot` type karo
3. Bot ka naam do (e.g. "My Anime Bot")
4. Username do (e.g. "myAnimeTrackerBot")
5. Token copy karo → `config.py` mein paste karo

### Apna User ID kaise milega?
1. **@userinfobot** ko message karo
2. ID copy karo → `ADMIN_IDS` mein dalo

## 🚀 Run Karo

```bash
python bot.py
```

Terminal mein `🚀 Anime Watchlist Bot started!` dikhega.

---

## 🌐 Hosting Options (baad mein)

### Railway.app (Free, Recommended)
1. railway.app pe account banao
2. New Project → Deploy from GitHub
3. Environment variable mein `BOT_TOKEN` add karo
4. Done!

### Replit
1. replit.com pe import karo
2. Secrets mein `BOT_TOKEN` add karo
3. Run!

---

## 📋 Bot Commands

| Command | Description |
|---------|-------------|
| `/start` | Bot shuru karo |
| `/search <name>` | Anime search karo |
| `/list` | Watchlist dekho |
| `/add <name>` | Anime add karo |
| `/remove <id>` | Anime remove karo |
| `/status <id>` | Status change karo |
| `/progress <id> <ep>` | Progress update |
| `/stats` | Tumhari stats |
| `/top` | Top rated anime |
| `/remind` | Reminders dekho |
| `/admin` | Admin panel |

---

## ✨ Features

- 🎌 **AniList Integration** — 15,000+ anime database (free, no API key needed)
- 📋 **5 Status Types** — Watching, Completed, On Hold, Dropped, Plan to Watch
- 🔢 **Episode Tracking** — Auto-complete jab sab episodes dekh lo
- ⭐ **Rating System** — 1-10 score do
- ⏰ **Reminders** — 1h, 3h, 1 day, 1 week options
- 🏆 **Top Rated** — Tumhari personal best anime list
- 📊 **Stats** — Full analytics
- 🔧 **Admin Panel** — User count, DB stats, broadcast
- 🗄️ **SQLite** — Local database, no setup needed

---

Made with ❤️ by Ayush
