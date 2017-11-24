'''Задание: Написать функцию ask_user() чтобы с помощью input() спрашивать пользователя “Как дела?”,
   пока он не ответит “Хорошо”. При помощи функции get_answer() отвечать на вопросы пользователя 
   в ask_user(), пока он не скажет “Пока!”'''


def ask_user():
    while True:
        user_say = input("Как дела?\n")
        if user_say == "Хорошо":
            break
        elif "?" in user_say:
            get_answer(user_say)
            break


def get_answer(user_say):
    while True:
        user_say = input("Неплохо. А может всё-таки расскажешь как дела?\n")
        if user_say == "Пока":
            print("Пока-пока")
            break

ask_user()
