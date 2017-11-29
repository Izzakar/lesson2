from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import re

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot_calc.log'
                    )


def main():
    updater = Updater("508192645:AAHpRrgje5XPMUs-Qlyz9H_bDeF4YYsMjc4")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("calc", calculation, pass_args=True))
    updater.start_polling()
    updater.idle()

def calculation(bot, update, args):
    if args == []:
        update.message.reply_text("Здесь только пустая строка. Попробуешь ещё?")
    else:
        matches = re.match('\d+[-+]\d+', args[0])
        sum_of_equation = 0
        if matches:
            str_equation = matches.group()
            if "+" in str_equation:
                arr_equation = str_equation.split("+")
                for parts in arr_equation: 
                    sum_of_equation += int(parts)
                update.message.reply_text(sum_of_equation)

            elif "-" in str_equation:
                arr_equation = str_equation.split("-")
                sub_of_equation = int(arr_equation[0])- int(arr_equation[1])
                update.message.reply_text(sub_of_equation)
        else:
            update.message.reply_text("Не уверен что я смогу это посчитать.")
        
if __name__ == "__main__":
    main()
