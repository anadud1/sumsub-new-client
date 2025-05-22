from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Telegram Bot credentials
TELEGRAM_BOT_TOKEN = '7564625699:AAG0sqTBB8WCA4azyjIFGrbInPCRfrEh52E'
TELEGRAM_CHAT_ID = '7427345918'  # Your confirmed chat ID

@app.route('/sumsub-webhook', methods=['POST'])
def sumsub_webhook():
    data = request.json
    print("✅ Webhook received:", data)

    # Format the message (you can customize this)
    message = f"👤 *New Sumsub Event Received*\n\n```json\n{data}```"

    # Send to Telegram
    telegram_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message,
        'parse_mode': 'Markdown'
    }

    response = requests.post(telegram_url, json=payload)

    if response.ok:
        return jsonify({'status': 'sent'}), 200
    else:
        print("❌ Error sending to Telegram:", response.text)
        return jsonify({'status': 'error', 'details': response.text}), 500

@app.route('/')
def home():
    return "✅ Sumsub → Telegram bot is running!"

