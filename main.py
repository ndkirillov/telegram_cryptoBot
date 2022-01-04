import requests
import telebot
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()
telegramToken = os.getenv("TELEGRAM_TOKEN")


def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["start"])
    def start_message(message):
        bot.send_message(message.chat.id, "Welcome to LCryptoBot type 'help' to see available commands")

    @bot.message_handler(content_types=["text"])
    def send_text(message):
        if message.text.lower() == "help":
            bot.send_message(message.chat.id, "price_buy_btc - get buy price of bitcoin \nprice_buy_eth - get buy price of etherium \nprice_buy_sol - get buy price of solana \nprice_buy_dot - get buy price of polkadot \nprice_sell_btc - get selling price of bitcoin\nprice_sell_eth - get selling price of etherium\nprice_sell_sol - get selling price of solana\nprice_sell_dot - get selling price of polkadot")
        #Get buy price of bitcoin
        if message.text.lower() == "price_buy_btc":
            try:
                req = requests.get("https://api.coinbase.com/v2/prices/BTC-USD/buy")
                response = req.json()
                buyBtcPrice = response["data"]["amount"]
                bot.send_message(message.chat.id, f"{datetime.now().strftime('%d-%m-%y %H:%M')}\nBuy BTC price is: {buyBtcPrice} USD")

            except Exception as ex:
                print(ex)
                bot.send_message(message.chat.id, "Error. Something went wrong!")

        #Get sell price of bitcoin
        if message.text.lower() == "price_sell_btc":
            try:
                req = requests.get("https://api.coinbase.com/v2/prices/BTC-USD/sell")
                response = req.json()
                sellBtcPrice = response["data"]["amount"]
                bot.send_message(message.chat.id, f"{datetime.now().strftime('%d-%m-%y %H:%M')}\nSell BTC price is: {sellBtcPrice} USD")

            except Exception as ex:
                print(ex)
                bot.send_message(message.chat.id, "Error. Something went wrong!")

        #Get buy price of etherium
        if message.text.lower() == "price_buy_eth":
            try:
                req = requests.get("https://api.coinbase.com/v2/prices/ETH-USD/buy")
                response = req.json()
                buyEthPrice = response["data"]["amount"]
                bot.send_message(message.chat.id, f"{datetime.now().strftime('%d-%m-%y %H:%M')}\nBuy ETH price is: {buyEthPrice} USD")

            except Exception as ex:
                print(ex)
                bot.send_message(message.chat.id, "Error. Something went wrong!")

        #Get sell price of etherium
        if message.text.lower() == "price_sell_eth":
            try:
                req = requests.get("https://api.coinbase.com/v2/prices/ETH-USD/sell")
                response = req.json()
                sellEthPrice = response["data"]["amount"]
                bot.send_message(message.chat.id, f"{datetime.now().strftime('%d-%m-%y %H:%M')}\nSell ETH price is: {sellEthPrice} USD")

            except Exception as ex:
                print(ex)
                bot.send_message(message.chat.id, "Error. Something went wrong!")

        #Get buy price of solana
        if message.text.lower() == "price_buy_sol":
            try:
                req = requests.get("https://api.coinbase.com/v2/prices/SOL-USD/buy")
                response = req.json()
                buySolPrice = response["data"]["amount"]
                bot.send_message(message.chat.id, f"{datetime.now().strftime('%d-%m-%y %H:%M')}\nBuy SOL price is: {buySolPrice} USD")

            except Exception as ex:
                print(ex)
                bot.send_message(message.chat.id, "Error. Something went wrong!")

        #Get sell price of solana
        if message.text.lower() == "price_sell_sol":
            try:
                req = requests.get("https://api.coinbase.com/v2/prices/SOL-USD/sell")
                response = req.json()
                sellSolPrice = response["data"]["amount"]
                bot.send_message(message.chat.id, f"{datetime.now().strftime('%d-%m-%y %H:%M')}\nSell SOL price is: {sellSolPrice} USD")

            except Exception as ex:
                print(ex)
                bot.send_message(message.chat.id, "Error. Something went wrong!")

        #Get buy price of polkadot
        if message.text.lower() == "price_buy_dot":
            try:
                req = requests.get("https://api.coinbase.com/v2/prices/DOT-USD/buy")
                response = req.json()
                buyDotPrice = response["data"]["amount"]
                bot.send_message(message.chat.id, f"{datetime.now().strftime('%d-%m-%y %H:%M')}\nBuy DOT price is: {buyDotPrice} USD")

            except Exception as ex:
                print(ex)
                bot.send_message(message.chat.id, "Error. Something went wrong!")

        #Get sell price of polkadot
        if message.text.lower() == "price_sell_dot":
            try:
                req = requests.get("https://api.coinbase.com/v2/prices/DOT-USD/sell")
                response = req.json()
                sellDotPrice = response["data"]["amount"]
                bot.send_message(message.chat.id, f"{datetime.now().strftime('%d-%m-%y %H:%M')}\nSell DOT price is: {sellDotPrice} USD")

            except Exception as ex:
                print(ex)
                bot.send_message(message.chat.id, "Error. Something went wrong!")

    bot.polling()

if __name__ == '__main__':
    telegram_bot(telegramToken)