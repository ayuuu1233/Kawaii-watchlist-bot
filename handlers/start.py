from telegram import Update
from telegram.ext import ContextTypes
from database.db import upsert_user, get_user_stats
from utils.keyboards import main_menu_kb, watchlist_filter_kb
import database.db as db

WELCOME = (
    "👋 <b>Konnichiwa, {name}!</b>\n\n"
    "🎌 <b>Anime Watchlist Bot</b> — tumhara personal anime tracker!\n\n"
    "✨ <b>Kya kar sakte ho:</b>\n"
    "• Anime search karo (AniList se)\n"
    "• Watchlist mein add/remove karo\n"
    "• Status track karo (Watching, Completed...)\n"
    "• Episode progress update karo\n"
    "• Rating do aur top list dekho\n"
    "• Reminders set karo\n\n"
    "👇 Neeche buttons se shuru karo!"
)

HELP_TEXT = (
    "📖 <b>Commands List</b>\n\n"
    "🔍 <b>Search</b>\n"
    "/search &lt;name&gt; — Anime search karo\n\n"
    "📋 <b>Watchlist</b>\n"
    "/list — Puri list dekho\n"
    "/add &lt;name&gt; — Quick add\n"
    "/remove &lt;id&gt; — Remove karo\n"
    "/status &lt;id&gt; — Status change karo\n"
    "/progress &lt;id&gt; &lt;ep&gt; — Episode update\n\n"
    "📊 <b>Stats & Info</b>\n"
    "/stats — Tumhari stats\n"
    "/top — Top rated anime\n\n"
    "⏰ <b>Reminder</b>\n"
    "/remind — Reminders manage karo\n\n"
    "💡 <b>Tip:</b> Seedha koi bhi anime name type karo — main search kar dunga!"
)

async def cmd_start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    upsert_user(user.id, user.username or "", user.first_name or "")
    await update.message.reply_text(
        WELCOME.format(name=user.first_name or "Otaku"),
        parse_mode="HTML",
        reply_markup=main_menu_kb()
    )

async def cmd_help(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(HELP_TEXT, parse_mode="HTML", reply_markup=main_menu_kb())

# ── Callback: menu_ buttons ────────────────────────────────────────
async def cb_menu(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q    = update.callback_query
    data = q.data
    await q.answer()
    user = update.effective_user

    if data == "menu_main":
        await q.edit_message_text(
            WELCOME.format(name=user.first_name or "Otaku"),
            parse_mode="HTML",
            reply_markup=main_menu_kb()
        )

    elif data == "menu_watchlist":
        await q.edit_message_text(
            "📋 <b>My Watchlist</b>\n\nKaun si list dekhni hai?",
            parse_mode="HTML",
            reply_markup=watchlist_filter_kb()
        )

    elif data == "menu_search":
        db.set_state(user.id, "searching")
        await q.edit_message_text(
            "🔍 <b>Anime Search</b>\n\nAnime ka naam type karo — main AniList se dhundh dunga!",
            parse_mode="HTML"
        )

    elif data == "menu_stats":
        stats = get_user_stats(user.id)
        text = (
            f"📊 <b>{user.first_name}'s Anime Stats</b>\n\n"
            f"👁️ Watching    : <b>{stats['watching']}</b>\n"
            f"✅ Completed   : <b>{stats['completed']}</b>\n"
            f"⏸️ On Hold     : <b>{stats['on_hold']}</b>\n"
            f"❌ Dropped     : <b>{stats['dropped']}</b>\n"
            f"📋 Plan        : <b>{stats['plan']}</b>\n"
            f"━━━━━━━━━━━━━━━\n"
            f"🎌 Total Anime : <b>{stats['total_anime']}</b>\n"
            f"📺 Episodes    : <b>{stats['total_episodes']}</b> watched"
        )
        await q.edit_message_text(text, parse_mode="HTML", reply_markup=main_menu_kb())

    elif data == "menu_reminders":
        reminders = db.get_user_reminders(user.id)
        if not reminders:
            text = "⏰ <b>Reminders</b>\n\nKoi reminder set nahi hai.\nAnime search karo aur reminder add karo!"
        else:
            text = "⏰ <b>Active Reminders</b>\n\n"
            for r in reminders:
                text += f"🔔 <b>{r['title']}</b>\n   📅 {r['remind_at']}\n\n"
        await q.edit_message_text(text, parse_mode="HTML", reply_markup=main_menu_kb())

    elif data == "menu_top":
        from handlers.watchlist import show_top_rated
        await show_top_rated(q, user.id)

    elif data == "menu_help":
        await q.edit_message_text(HELP_TEXT, parse_mode="HTML", reply_markup=main_menu_kb())
