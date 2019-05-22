def ask_user():
    while True:
        user_say = input('Как дела? ')
        if user_say == 'Хорошо':
            break
ask_user()
if __name__ == '__main__':
    ask_user()