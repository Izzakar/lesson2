answer = {'Привет': 'И тебе привет!', 'А как твои?': 'Лучше всех!'}


def ask_user():
    while True:
        user_text = input("Как дела?\n")
        if user_text == "Пока":
            break
        get_answer(user_text)

def get_answer(user_text):
    if answer.get(user_text) is None:
        print ('Повтори ещё раз,пожалуйста.')
    else:
        print (answer.get(user_text))

try:
    ask_user()    
except KeyboardInterrupt:
    print ("Ну и ладно. Пока!")