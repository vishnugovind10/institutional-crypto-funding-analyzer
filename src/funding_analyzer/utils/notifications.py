import requests
import logging

logging.basicConfig(filename='logs/funding_analyzer.log', level=logging.INFO)

def send_alert(subject, message):
    logging.info(f"Sending alert: {subject} - {message}")
    # Placeholder for Slack/WhatsApp/Signal integration
    try:
        # Example: Slack webhook
        requests.post("https://hooks.slack.com/your/webhook", json={"text": f"{subject}: {message}"})
    except Exception as e:
        logging.error(f"Alert failed: {e}")