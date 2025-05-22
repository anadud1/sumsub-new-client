from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Telegram Bot credentials
TELEGRAM_BOT_TOKEN = '7564625699:AAG0sqTBB8WCA4azyjIFGrbInPCRfrEh52E'
TELEGRAM_CHAT_ID = '7427345918'  # Your Telegram chat ID

@app.route('/sumsub-webhook', methods=['POST'])
def sumsub_webhook():
    data = request.json
    print("✅ Webhook received:", data)

    # Build message to send to Telegram
    message = f"👤 *New Sumsub Event Received*\n\n```json\n{data}```"

    # Send message to Telegram
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
        print("❌ Telegram error:", response.text)
        return jsonify({'status': 'error', 'details': response.text}), 500

@app.route('/')
def home():
    return "✅ Sumsub → Telegram bot is running!"

# === Port binding for Render ===
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
