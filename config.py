# ═══════════════════════════════════════════════
#   config.py  –  Bot Configuration
# ═══════════════════════════════════════════════

BOT_TOKEN = "8778724587:AAHxkwzLU1Zpc7OssHAPbfKTIivfGYa6tX0"   # 👈 got from @BotFather 

DB_PATH   = "watchlist.db"

ADMIN_IDS = [5158013355]             # 👈  Telegram user ID 

# AniList GraphQL API (free, no key needed)
ANILIST_URL = "https://graphql.anilist.co"

# Status labels shown in UI
STATUS_LABELS = {
    "watching":   "👁️ Watching",
    "completed":  "✅ Completed",
    "on_hold":    "⏸️ On Hold",
    "dropped":    "❌ Dropped",
    "plan":       "📋 Plan to Watch",
}

# Max watchlist per user
MAX_WATCHLIST = 200
