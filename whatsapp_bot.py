"""
╔══════════════════════════════════════════════════════════╗
║   UMESH KAMBLE — WHATSAPP BOT (Twilio)                  ║
║   Courses · Mentorship · Portfolio · Lead Collection    ║
╚══════════════════════════════════════════════════════════╝

SETUP:
1. pip install flask twilio
2. Sign up at twilio.com (free trial available)
3. Enable WhatsApp Sandbox in Twilio Console
4. Replace ACCOUNT_SID and AUTH_TOKEN below
5. Run: python whatsapp_bot.py
6. Use ngrok to expose local server:
   ngrok http 5000
7. Paste ngrok URL into Twilio WhatsApp Sandbox webhook

HOW IT WORKS:
- User sends "Hi" to your WhatsApp Sandbox number
- Bot replies with menu buttons
- User replies with a number to navigate
"""

from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import datetime

# ── CONFIG ────────────────────────────────────────────────
ACCOUNT_SID = "YOUR_TWILIO_ACCOUNT_SID"
AUTH_TOKEN = "YOUR_TWILIO_AUTH_TOKEN"
YOUR_EMAIL = "umeshkamble036@gmail.com"
YOUR_LINKEDIN = "https://www.linkedin.com/in/umesh-kamble-a21704134/"
YOUR_ARTICLE = "https://www.linkedin.com/pulse/learners-perspective-what-i-built-when-connected-mainframe-kamble-pevkc"
YOUR_PORTFOLIO = "https://umeshkamble036.github.io/resume"
YOUR_GITHUB = "https://github.com/Umeshkamble036"
YOUR_SERVICES = "https://umeshkamble036.github.io/resume/services"

app = Flask(__name__)

# In-memory session & lead store (use DB in production)
sessions = {}
leads = []

# ── MENUS ─────────────────────────────────────────────────
MAIN_MENU = """👋 *Hello! Welcome to Umesh Kamble's Bot*

I'm a Senior Mainframe Lead & AI Agent Builder from Pune 🇮🇳

Reply with a number to navigate:

1️⃣  📚 Courses & Mentorship
2️⃣  💰 Pricing & Plans  
3️⃣  📖 My Article & Portfolio
4️⃣  📅 Book a Free Intro Session
5️⃣  📩 Contact Umesh Directly

Type *0* anytime to return to this menu."""

COURSES_MENU = """📚 *Courses & Mentorship*

I offer part-time 1:1 mentorship in:

1️⃣  ☁️ AWS Mainframe Modernization
2️⃣  🖥️ Enterprise Mainframe Engineering
3️⃣  🤖 Custom AI Agent Creation
4️⃣  🌱 Free Learning Content

Type *0* for Main Menu"""

PRICING_MSG = """💰 *Pricing & Packages*

🌱 *Free — ₹0/month*
Articles, trends & LinkedIn updates

⚡ *Single — ₹4,999/month*
• 1 topic of your choice
• 2 x 1:1 sessions/month (60 min)
• Personal learning roadmap
• WhatsApp support

🔥 *Duo — ₹8,499/month*
• Any 2 topics combined
• 4 x 1:1 sessions/month
• Resume & LinkedIn review
• Save ₹1,499!

👑 *Complete — ₹11,999/month* ✦ Best Value
• All 3 topics
• 6 x 1:1 sessions/month
• Full career support
• Resume + LinkedIn + GitHub review
• Agent architecture templates

💳 UPI · Razorpay · Bank Transfer

Type *4* to book a free intro call
Type *0* for Main Menu"""

COURSE_AWS = """☁️ *AWS Mainframe Modernization*

What you'll learn:
→ AWS Blu Age — COBOL to Java
→ AWS Mainframe Modernization Service
→ AWS Transform — AI-assisted migration
→ 8R Framework — right strategy per system
→ Real project: migrate COBOL app to cloud
→ AWS certification study guidance

⏱ 2 sessions/month · 60 min each
📍 Online · Part-time basis

Type *2* for Pricing
Type *4* to Book a Session
Type *0* for Main Menu"""

COURSE_MAINFRAME = """🖥️ *Enterprise Mainframe Engineering*

What you'll learn:
→ COBOL — beginner to advanced
→ JCL job streams & batch processing
→ DB2 on Mainframe — SQL & stored procs
→ IMS hierarchical database design
→ CICS transaction processing
→ VSAM file systems & design patterns
→ Debugging & performance tuning

⏱ 2 sessions/month · 60 min each
🎯 8 years AT&T & AmEx experience

Type *2* for Pricing
Type *4* to Book a Session
Type *0* for Main Menu"""

COURSE_AGENTS = """🤖 *Custom AI Agent Creation*

What you'll learn:
→ Python for AI from scratch
→ LangChain — building agent pipelines
→ Claude API — prompting & context design
→ Router Agent architecture
→ Multi-agent orchestration systems
→ Self-verification quality loops
→ Deploy agents on real enterprise systems

⏱ 2 sessions/month · 60 min each
🏆 I built 30+ production agents — 80-90% accuracy

Type *2* for Pricing
Type *4* to Book a Session
Type *0* for Main Menu"""

COURSE_FREE = f"""🌱 *Free Learning — Always Free*

No cost. No card. Just follow me!

What's free:
→ Monthly articles on latest tech trends
→ AI, mainframe & cloud tool summaries
→ Career tips for engineers
→ Industry news & analysis
→ New agent frameworks updates

📖 Latest Article:
{YOUR_ARTICLE}

💼 Follow on LinkedIn:
{YOUR_LINKEDIN}

Type *0* for Main Menu"""

PORTFOLIO_MSG = f"""🌐 *Portfolio & GitHub*

🏆 Key Stats:
→ 8 years mainframe experience
→ 30+ AI agents built & deployed
→ 13 mission-critical applications
→ 80-90% automation accuracy

🌐 Portfolio: {YOUR_PORTFOLIO}
⚙️ GitHub: {YOUR_GITHUB}
💼 LinkedIn: {YOUR_LINKEDIN}

📖 Latest Article:
{YOUR_ARTICLE}

Type *0* for Main Menu"""

CONTACT_MSG = f"""📩 *Contact Umesh Directly*

📧 Email: {YOUR_EMAIL}
📱 WhatsApp: +91 7083903479
📍 Location: Pune, India
🌐 Open to Remote / Relocation

⏱ Response time: 24-48 hours

Type *4* to book a free intro call
Type *0* for Main Menu"""

# ── WEBHOOK ───────────────────────────────────────────────
@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    from_number = request.form.get("From", "")
    body = request.form.get("Body", "").strip()
    msg_lower = body.lower()

    resp = MessagingResponse()
    msg = resp.message()

    # Get or create session
    session = sessions.get(from_number, {"state": "menu", "data": {}})

    # ── BOOKING FLOW ──
    if session["state"] == "ask_name":
        session["data"]["name"] = body
        session["state"] = "ask_email"
        sessions[from_number] = session
        msg.body(f"Great, *{body}*! 👋\n\n📧 What is your *email address*?")
        return str(resp)

    elif session["state"] == "ask_email":
        session["data"]["email"] = body
        session["state"] = "ask_goal"
        sessions[from_number] = session
        msg.body(
            "Almost done! 🎯\n\n"
            "What is your *main learning goal*?\n\n"
            "_Example: I want to learn AWS Mainframe Modernization and move from COBOL to cloud_"
        )
        return str(resp)

    elif session["state"] == "ask_goal":
        name = session["data"].get("name", "Unknown")
        email = session["data"].get("email", "Unknown")
        goal = body

        # Save lead
        lead = {
            "name": name,
            "email": email,
            "goal": goal,
            "whatsapp": from_number,
            "timestamp": datetime.datetime.now().isoformat()
        }
        leads.append(lead)
        print(f"\n🔔 NEW WHATSAPP LEAD:\nName: {name}\nEmail: {email}\nGoal: {goal}\nWhatsApp: {from_number}\n")

        session["state"] = "menu"
        sessions[from_number] = session

        msg.body(
            f"✅ *Request Received, {name}!*\n\n"
            f"📋 Your Details:\n"
            f"Name: {name}\n"
            f"Email: {email}\n"
            f"Goal: {goal}\n\n"
            f"Umesh will contact you within *24-48 hours* to confirm your free intro call! 🎯\n\n"
            f"Type *0* to return to Main Menu"
        )
        return str(resp)

    # ── RESET TO MENU ──
    if body in ["0", "menu", "hi", "hello", "start", "hey"]:
        session["state"] = "menu"
        sessions[from_number] = session
        msg.body(MAIN_MENU)

    # ── MAIN MENU CHOICES ──
    elif body == "1" and session["state"] == "menu":
        session["state"] = "courses"
        sessions[from_number] = session
        msg.body(COURSES_MENU)

    elif body == "2" and session["state"] in ["menu", "courses"]:
        msg.body(PRICING_MSG)

    elif body == "3":
        msg.body(PORTFOLIO_MSG)

    elif body == "4":
        session["state"] = "ask_name"
        sessions[from_number] = session
        msg.body(
            "📅 *Book a Free 30-Min Intro Call*\n\n"
            "Let's understand your goals and design your roadmap!\n\n"
            "👤 What is your *full name*?"
        )

    elif body == "5":
        msg.body(CONTACT_MSG)

    # ── COURSE SUBMENU ──
    elif body == "1" and session["state"] == "courses":
        msg.body(COURSE_AWS)

    elif body == "2" and session["state"] == "courses":
        msg.body(COURSE_MAINFRAME)

    elif body == "3" and session["state"] == "courses":
        msg.body(COURSE_AGENTS)

    elif body == "4" and session["state"] == "courses":
        msg.body(COURSE_FREE)

    else:
        msg.body(
            "I didn't understand that. 😊\n\n"
            "Type *0* to see the Main Menu\n"
            "or *Hi* to start fresh!"
        )

    return str(resp)

@app.route("/", methods=["GET"])
def health():
    return f"✅ Umesh Kamble WhatsApp Bot Running | {len(leads)} leads collected"

if __name__ == "__main__":
    print("🤖 Umesh Kamble WhatsApp Bot starting on port 5000...")
    print(f"📊 Leads collected so far: {len(leads)}")
    app.run(debug=True, port=5000)
