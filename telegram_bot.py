"""
╔══════════════════════════════════════════════════════════╗
║   UMESH KAMBLE — TELEGRAM BOT                           ║
║   Courses · Mentorship · Portfolio · Lead Collection    ║
╚══════════════════════════════════════════════════════════╝

SETUP:
1. pip install python-telegram-bot
2. Create bot via @BotFather on Telegram → get TOKEN
3. Replace YOUR_BOT_TOKEN below
4. Run: python telegram_bot.py
"""

import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application, CommandHandler, CallbackQueryHandler,
    MessageHandler, filters, ContextTypes, ConversationHandler
)

# ── CONFIG ────────────────────────────────────────────────
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"   # From @BotFather
YOUR_EMAIL = "umeshkamble036@gmail.com"
YOUR_WHATSAPP = "+917083903479"
YOUR_LINKEDIN = "https://www.linkedin.com/in/umesh-kamble-a21704134/"
YOUR_ARTICLE = "https://www.linkedin.com/pulse/learners-perspective-what-i-built-when-connected-mainframe-kamble-pevkc"
YOUR_PORTFOLIO = "https://umeshkamble036.github.io/resume"
YOUR_GITHUB = "https://github.com/Umeshkamble036"
YOUR_SERVICES = "https://umeshkamble036.github.io/resume/services"

# Conversation states
ASK_NAME, ASK_EMAIL, ASK_GOAL = range(3)

# Leads storage (in production use a database or Google Sheets)
leads = []

logging.basicConfig(level=logging.INFO)

# ── MAIN MENU ─────────────────────────────────────────────
def main_menu_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📚 Courses & Mentorship", callback_data="courses")],
        [InlineKeyboardButton("💰 Pricing & Plans", callback_data="pricing")],
        [InlineKeyboardButton("📖 Read My Article", callback_data="article")],
        [InlineKeyboardButton("🌐 Portfolio & GitHub", callback_data="portfolio")],
        [InlineKeyboardButton("📅 Book a Session", callback_data="book")],
        [InlineKeyboardButton("📩 Contact Umesh", callback_data="contact")],
    ])

# ── /START ────────────────────────────────────────────────
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(
        f"👋 *Hello {user.first_name}!*\n\n"
        "I'm the assistant bot for *Umesh Kamble* — Senior Mainframe Lead, "
        "AI Agent Builder & AWS Modernization Expert.\n\n"
        "I can help you with:\n"
        "• 📚 Course & mentorship details\n"
        "• 💰 Pricing & packages\n"
        "• 📅 Booking a 1:1 session\n"
        "• 📖 Articles & portfolio\n\n"
        "What would you like to know? 👇",
        parse_mode="Markdown",
        reply_markup=main_menu_keyboard()
    )

# ── BUTTON HANDLER ────────────────────────────────────────
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    # ── COURSES
    if data == "courses":
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("☁️ AWS Modernization", callback_data="course_aws")],
            [InlineKeyboardButton("🖥️ Mainframe Engineering", callback_data="course_mainframe")],
            [InlineKeyboardButton("🤖 Custom AI Agents", callback_data="course_agents")],
            [InlineKeyboardButton("🌱 Free Learning", callback_data="course_free")],
            [InlineKeyboardButton("⬅️ Back to Menu", callback_data="menu")],
        ])
        await query.edit_message_text(
            "📚 *Courses & Mentorship*\n\n"
            "I offer part-time mentorship in 3 specialist areas.\n"
            "All sessions are 1:1, personalised, and practical.\n\n"
            "Choose a topic to learn more 👇",
            parse_mode="Markdown",
            reply_markup=keyboard
        )

    # ── COURSE: AWS
    elif data == "course_aws":
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("💰 See Pricing", callback_data="pricing")],
            [InlineKeyboardButton("📅 Book a Session", callback_data="book")],
            [InlineKeyboardButton("⬅️ Back", callback_data="courses")],
        ])
        await query.edit_message_text(
            "☁️ *AWS Mainframe Modernization*\n\n"
            "What you'll learn:\n"
            "→ AWS Blu Age — COBOL to Java refactoring\n"
            "→ AWS Mainframe Modernization Service\n"
            "→ AWS Transform — AI-assisted migration\n"
            "→ 8R Framework — right strategy per system\n"
            "→ Replatforming vs Refactoring decisions\n"
            "→ Real project: migrate a COBOL app to cloud\n"
            "→ AWS certification study guidance\n\n"
            "⏱ *2 sessions/month (60 min each)*\n"
            "📍 Online · Part-time basis",
            parse_mode="Markdown",
            reply_markup=keyboard
        )

    # ── COURSE: MAINFRAME
    elif data == "course_mainframe":
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("💰 See Pricing", callback_data="pricing")],
            [InlineKeyboardButton("📅 Book a Session", callback_data="book")],
            [InlineKeyboardButton("⬅️ Back", callback_data="courses")],
        ])
        await query.edit_message_text(
            "🖥️ *Enterprise Mainframe Engineering*\n\n"
            "What you'll learn:\n"
            "→ COBOL programming — beginner to advanced\n"
            "→ JCL job streams and batch processing\n"
            "→ DB2 on Mainframe — SQL & stored procs\n"
            "→ IMS hierarchical database design\n"
            "→ CICS transaction processing\n"
            "→ VSAM file systems & design patterns\n"
            "→ Debugging & performance tuning\n\n"
            "⏱ *2 sessions/month (60 min each)*\n"
            "📍 Online · Part-time basis\n\n"
            "🎯 8 years of AT&T & AmEx production experience",
            parse_mode="Markdown",
            reply_markup=keyboard
        )

    # ── COURSE: AGENTS
    elif data == "course_agents":
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("💰 See Pricing", callback_data="pricing")],
            [InlineKeyboardButton("📅 Book a Session", callback_data="book")],
            [InlineKeyboardButton("⬅️ Back", callback_data="courses")],
        ])
        await query.edit_message_text(
            "🤖 *Custom AI Agent Creation*\n\n"
            "What you'll learn:\n"
            "→ Python for AI — from scratch to agents\n"
            "→ LangChain — building agent pipelines\n"
            "→ Claude API — prompting & context design\n"
            "→ Router Agent architecture & orchestration\n"
            "→ Multi-agent systems — specialist + router\n"
            "→ Self-verification and quality loops\n"
            "→ Deploy agents on real enterprise use cases\n\n"
            "⏱ *2 sessions/month (60 min each)*\n"
            "🏆 I built 30+ production agents — 80-90% automation",
            parse_mode="Markdown",
            reply_markup=keyboard
        )

    # ── COURSE: FREE
    elif data == "course_free":
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("🔗 Follow on LinkedIn", url=YOUR_LINKEDIN)],
            [InlineKeyboardButton("📖 Read Latest Article", url=YOUR_ARTICLE)],
            [InlineKeyboardButton("⬅️ Back", callback_data="courses")],
        ])
        await query.edit_message_text(
            "🌱 *Free Learning — Always Free*\n\n"
            "No cost. No card. Just follow me.\n\n"
            "What's free:\n"
            "→ Monthly articles on latest tech trends\n"
            "→ AI, mainframe & cloud tool summaries\n"
            "→ Career tips for engineers\n"
            "→ Industry news & analysis\n"
            "→ New agent framework updates\n\n"
            "📍 Published on LinkedIn & my portfolio site",
            parse_mode="Markdown",
            reply_markup=keyboard
        )

    # ── PRICING
    elif data == "pricing":
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("📅 Book Free Intro Call", callback_data="book")],
            [InlineKeyboardButton("🌐 See Full Details", url=YOUR_SERVICES)],
            [InlineKeyboardButton("⬅️ Back to Menu", callback_data="menu")],
        ])
        await query.edit_message_text(
            "💰 *Pricing & Packages*\n\n"
            "🌱 *Free* — ₹0/month\n"
            "Articles, trends & LinkedIn updates\n\n"
            "⚡ *Single* — ₹4,999/month\n"
            "1 topic · 2 sessions · Personal roadmap\n"
            "Choose: AWS or Mainframe or AI Agents\n\n"
            "🔥 *Duo* — ₹8,499/month\n"
            "2 topics · 4 sessions · Resume review\n"
            "Save ₹1,499 vs two Single plans\n\n"
            "👑 *Complete* — ₹11,999/month ✦ Best Value\n"
            "All 3 topics · 6 sessions · Full support\n"
            "Resume + LinkedIn + GitHub review included\n\n"
            "💳 UPI · Bank Transfer · Razorpay\n"
            "📍 Part-time basis · Limited slots",
            parse_mode="Markdown",
            reply_markup=keyboard
        )

    # ── ARTICLE
    elif data == "article":
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("📖 Read on LinkedIn", url=YOUR_ARTICLE)],
            [InlineKeyboardButton("🌐 View Portfolio", url=YOUR_PORTFOLIO)],
            [InlineKeyboardButton("⬅️ Back to Menu", callback_data="menu")],
        ])
        await query.edit_message_text(
            "📖 *My Latest Article*\n\n"
            "*\"A Learner's Perspective: What I Built When I Connected Mainframe and AI\"*\n\n"
            "→ How I built 30+ AI agents on real mainframe\n"
            "→ 80-90% automation on AT&T production systems\n"
            "→ My original Translate-Verify-Learn architecture\n"
            "→ Honest lessons from 8 years in the field\n\n"
            "Published on LinkedIn · Read by engineers worldwide",
            parse_mode="Markdown",
            reply_markup=keyboard
        )

    # ── PORTFOLIO
    elif data == "portfolio":
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("🌐 Portfolio Website", url=YOUR_PORTFOLIO)],
            [InlineKeyboardButton("⚙️ GitHub Projects", url=YOUR_GITHUB)],
            [InlineKeyboardButton("💼 LinkedIn Profile", url=YOUR_LINKEDIN)],
            [InlineKeyboardButton("⬅️ Back to Menu", callback_data="menu")],
        ])
        await query.edit_message_text(
            "🌐 *Portfolio & GitHub*\n\n"
            "🏆 *Key Stats:*\n"
            "→ 8 years mainframe experience\n"
            "→ 30+ AI agents built & deployed\n"
            "→ 13 mission-critical applications\n"
            "→ 80-90% automation accuracy\n\n"
            "⚙️ *GitHub Projects:*\n"
            "→ AWS Mainframe Modernization App\n"
            "→ Mainframe to Java AWS Migration\n"
            "→ NIVESH — AI Investment Dashboard\n"
            "→ Spring Boot & JPA Applications\n\n"
            "Choose a link to explore 👇",
            parse_mode="Markdown",
            reply_markup=keyboard
        )

    # ── BOOK SESSION (starts lead collection)
    elif data == "book":
        await query.edit_message_text(
            "📅 *Book a Free 30-Min Intro Call*\n\n"
            "Let's understand your goals and design your learning roadmap.\n\n"
            "I just need a few details first.\n\n"
            "👤 *What is your full name?*",
            parse_mode="Markdown"
        )
        return ASK_NAME

    # ── CONTACT
    elif data == "contact":
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("📧 Email Umesh", url=f"mailto:{YOUR_EMAIL}")],
            [InlineKeyboardButton("💬 WhatsApp", url=f"https://wa.me/917083903479")],
            [InlineKeyboardButton("💼 LinkedIn", url=YOUR_LINKEDIN)],
            [InlineKeyboardButton("⬅️ Back to Menu", callback_data="menu")],
        ])
        await query.edit_message_text(
            "📩 *Contact Umesh Directly*\n\n"
            f"📧 Email: `{YOUR_EMAIL}`\n"
            f"📱 Phone: `+91 7083903479`\n"
            f"📍 Location: Pune, India\n"
            "🌐 Open to Remote / Relocation\n\n"
            "Response time: within 24-48 hours",
            parse_mode="Markdown",
            reply_markup=keyboard
        )

    # ── BACK TO MENU
    elif data == "menu":
        await query.edit_message_text(
            "🏠 *Main Menu*\n\nWhat would you like to know?",
            parse_mode="Markdown",
            reply_markup=main_menu_keyboard()
        )

# ── LEAD COLLECTION FLOW ──────────────────────────────────
async def ask_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["name"] = update.message.text
    await update.message.reply_text(
        f"Great, *{update.message.text}*! 👋\n\n"
        "📧 *What is your email address?*\n"
        "_(So Umesh can confirm your session)_",
        parse_mode="Markdown"
    )
    return ASK_EMAIL

async def ask_email(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["email"] = update.message.text
    await update.message.reply_text(
        "Almost done! 🎯\n\n"
        "🎯 *What is your main learning goal?*\n\n"
        "Example: _'I want to learn AWS Mainframe Modernization and transition from COBOL developer to cloud engineer'_",
        parse_mode="Markdown"
    )
    return ASK_GOAL

async def ask_goal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = context.user_data.get("name", "Unknown")
    email = context.user_data.get("email", "Unknown")
    goal = update.message.text
    telegram_user = update.effective_user.username or "No username"

    # Save lead
    lead = {
        "name": name,
        "email": email,
        "goal": goal,
        "telegram": f"@{telegram_user}"
    }
    leads.append(lead)

    # Log to console (in production: send to email/Google Sheets)
    print(f"\n🔔 NEW LEAD:\nName: {name}\nEmail: {email}\nGoal: {goal}\nTelegram: @{telegram_user}\n")

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("💬 WhatsApp Umesh Now", url="https://wa.me/917083903479")],
        [InlineKeyboardButton("⬅️ Back to Menu", callback_data="menu")],
    ])

    await update.message.reply_text(
        f"✅ *Request Received, {name}!*\n\n"
        f"📋 *Your Details:*\n"
        f"Name: {name}\n"
        f"Email: {email}\n"
        f"Goal: _{goal}_\n\n"
        "Umesh will reach out within *24-48 hours* to confirm your free intro call.\n\n"
        "Alternatively, message him directly on WhatsApp 👇",
        parse_mode="Markdown",
        reply_markup=keyboard
    )
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "No problem! Come back anytime. 😊",
        reply_markup=main_menu_keyboard()
    )
    return ConversationHandler.END

# ── FALLBACK ──────────────────────────────────────────────
async def fallback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Use the menu below to navigate 👇",
        reply_markup=main_menu_keyboard()
    )

# ── MAIN ──────────────────────────────────────────────────
def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # Conversation handler for booking flow
    conv = ConversationHandler(
        entry_points=[CallbackQueryHandler(button_handler, pattern="^book$")],
        states={
            ASK_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_name)],
            ASK_EMAIL: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_email)],
            ASK_GOAL: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_goal)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("menu", start))
    app.add_handler(conv)
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, fallback))

    print("🤖 Umesh Kamble Telegram Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
