---

## 🙋‍♂️ About This Project

This is **not** a polished or production-grade app — it's a personal tool I built for myself during times when I wanted to stay informed, but not overwhelmed by alerts.

It uses a direct connection to Telegram via my account and bot, which requires setup steps like creating a bot, getting API credentials, and running the script on a machine tied to your Telegram number.

I'm sharing it in case others find it useful or want to replicate something similar — especially if you're technically inclined and comfortable setting things up manually.  
No guarantees, no support, just something that worked for me.

---

# Tsofar Alert Filter

A lightweight, real-time Telegram filter that listens to the **“Tzeva Adom”** alert channel and forwards messages to you **only if they contain specific locations** you care about.

This avoids constant notifications for irrelevant alerts — and ensures you're notified immediately when it matters.


## 🔍 What It Does

- Monitors messages from the official alert channel (`@tzevaadomm`)
- Filters alerts based on keywords for:
  - Emergency areas (e.g., your home)
  - Critical or nearby regions
  - Custom areas of interest
  - Heads-up alerts
- Sends a Telegram message to your group or personal chat via a bot when a match is found

## ⚙️ Requirements

- Python 3.7+
- [Telethon](https://github.com/LonamiWebs/Telethon)
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)

Install with:
```pip install telethon python-telegram-bot```

You’ll also need to:

1. **Create a Telegram Bot**  
   Talk to [@BotFather](https://t.me/BotFather), create a new bot, and get the **bot token**.

2. **Create a Telegram Group**  
   Add your bot to the group and make it an **admin** so it can send messages.

3. **Get Chat IDs**  
   - Use the script’s debug mode (or a temporary handler) to print `event.chat.id`
   - Identify your:
     - Group chat ID (`GROUPCHAT_ID`)
     - Debug/testing chat ID (`DEBUG_CHAT_ID`)

4. **Get Telegram API credentials**  
   - Visit [my.telegram.org](https://my.telegram.org/)
   - Create a new application and save the `API_ID`, `API_HASH`, and your Telegram phone number.

## 🚀 How to Use

Clone the repo:

```git clone https://github.com/yourusername/tsofar-filter.git```

```cd tsofar-filter```


Replace the placeholder values at the top of tsofar-filter.py:

- API_ID, API_HASH, BOT_TOKEN, PHONE
- Target CHANNEL, GROUPCHAT_ID, DEBUG_CHAT_ID
- Location keywords (emergency_word, critical_words, etc.)

Run the script in the background:

```nohup python tsofar-filter.py &```
- Output will be saved to ```nohup.out``` by default.
- To monitor logs, use: ```tail -f output.log```

## 💡 Notes
- The code is optimized for low-latency, real-time message handling.
- Some repetition is intentional to reduce overhead.
- You can use DEBUG_CHAT_ID to echo test messages and verify setup.

## 🛡️ Disclaimer
This tool is provided as-is for personal use.
- It is not affiliated with or endorsed by Tsofar, Tzeva Adom, the Home Front Command, or any official alerting entity.
- It simply listens to the public Telegram channel and filters messages based on user-defined keywords.
- Always verify alerts with official sources and do not rely solely on this script in life-critical situations.

Made with ❤️ to reduce notification fatigue during tense times.
