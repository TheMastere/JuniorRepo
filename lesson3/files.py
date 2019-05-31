with open('referat.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    line_length = len(content)
    number_words = (len(content.split()))
    change = content.replace('.', '!')
    print("Количество символов в тексте:", line_length)
    print("Количество слов в тексте:", number_words)
with open('referat2.txt', 'w', encoding='utf-8') as f:
    print(change, file=f)