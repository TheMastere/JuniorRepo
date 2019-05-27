answers = {"как дела?": "Хорошо!", "что делаешь?": "Программирую", "что еще делаешь?": "Читаю",
                    "а еще что делаешь?": "Кино смотрю"}

def get_answer(question, answers):
    return answers.get(question)

def ask_user(answers):
    while True:
        user_input = input('Напишите что-либо: ')
        answer = get_answer(user_input.lower(), answers)
        print(answer)

        if user_input == 'пока':
            break


ask_user(answers)
if __name__ == '__main__':
    ask_user()