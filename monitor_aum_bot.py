import os
import requests
from bs4 import BeautifulSoup
from telegram import Bot
from telegram.parsemode import ParseMode


# Telegram Bot Token obtained from GitHub Secrets
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# Website URL for scraping AUM data (replace with your website URL)
WEBSITE_URL = 'https://jup.ag/perps-earn/buy/SOL'

# AUM threshold to trigger a message
AUM_THRESHOLD = 10000000  # Adjust this threshold as needed

# Initialize the Telegram Bot
bot = Bot(TOKEN)

def send_telegram_message(message):
    try:
        chat_id = 'YOUR_TELEGRAM_CHAT_ID'  # Replace with your Telegram chat ID
        bot.send_message(chat_id=chat_id, text=message, parse_mode=ParseMode.HTML)
    except Exception as e:
        print(f"Error sending message: {e}")

def main():
    try:
        # Fetch the HTML content of the website
        response = requests.get(WEBSITE_URL)
        response.raise_for_status()

        # Parse the HTML content using Beautiful Soup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the div container holding the AUM value
        aum_container = soup.find('div', class_='flex space-x-1 text-xs text-v2-lily/50 mt-1')

        # Extract AUM value from the span tags within the container
        spans = aum_container.find_all('span')
        aum_value = spans[-1].text.strip()  # Get the last span (assuming it contains the AUM)

        # Clean up AUM value (remove '$' and commas)
        cleaned_aum = float(aum_value.replace('$', '').replace(',', ''))

        # Check if AUM exceeds threshold
        if cleaned_aum > AUM_THRESHOLD:
            message = f"AUM limit exceeded: ${cleaned_aum}"
            send_telegram_message(message)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
