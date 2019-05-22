def ask_user():
    while True:
        user_say = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую", "Что еще делаешь?": "Читаю",
                    "А еще что делаешь?": "Кино смотрю"}
        print('Напишите что-либо: ')
        user_otvet = input()
        if user_otvet in user_say:
            print(user_say[user_otvet])
        else:
            print('Ничем не могу помочь')
ask_user()
if __name__ == '__main__':
    ask_user()