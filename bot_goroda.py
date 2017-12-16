from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from settings import SECRET_KEY
from cities_list import cities
import json
import random


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot_goroda.log'
                    )


def main():
    updater = Updater(SECRET_KEY)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("goroda", game_core,
                                  pass_args=True, pass_user_data=True))
    dp.add_handler(CommandHandler("start", update_game, pass_user_data=True))
    updater.start_polling()
    updater.idle()


def update_game(bot, update, user_data):
    with open('cities.json', 'r', encoding='utf-8') as g:
        cities = json.load(g)
    random.shuffle(cities)
    user_data["state"] = {
        "available_cities": cities, "already_used_cities": []}
    print(user_data["state"])


def game_core(bot, update, user_data, args):
    if args == []:
        update.message.reply_text(
            "Здесь только пустая строка. Попробуешь ещё?")
    else:
        if args[0] in user_data["state"]["available_cities"]:
            named_city = args[0].lower()
            last_word = named_city[-1]
            user_data["state"]["already_used_cities"].append(
                named_city.capitalize())
            user_data["state"]["available_cities"].remove(
                named_city.capitalize())
            for city in user_data["state"]["available_cities"]:
                if city[0].lower() == last_word:
                    update.message.reply_text(
                        "{}, твой ход!".format(city.capitalize()))
                    user_data["state"]["already_used_cities"].append(
                        city.capitalize())
                    user_data["state"]["available_cities"].remove(
                        city.capitalize())
                    print(user_data["state"]["available_cities"])
                    break

        elif args[0] in user_data["state"]["already_used_cities"]:
            update.message.reply_text("Этот город уже был. Давай другой!")
        else:
            update.message.reply_text(
                "Я не знаю такого города. Попробуешь ещё?")


if __name__ == "__main__":
    main()
