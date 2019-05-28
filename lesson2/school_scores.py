school_scores = [{'school_class': '4a', 'scores': [3,4,4,5,2]}, {'school_class': '6b', 'scores': [5,1,2,3,3]},
{'school_class': '2a', 'scores': [3,4,2,5,2,5]}, {'school_class': '10B', 'scores': [5,5,5,4,3,4,5,2]}]
school_middle = []
# сначала вывожу средний балл по каждому классу
for school in school_scores: # итерируем по словарям в списке
    class_score = sum(school['scores']) # суммируем все оценки в словаре scores
    class_middle = class_score/(len(school['scores'])) # делим получившуюся сумму оценок на количество чисел в scores
    print('Cредний балл в классе {0}: {1}'.format(school['school_class'], class_middle)) # присваиваем каждому школьному классу соответствующую оценку
    school_middle.append(class_middle) # добавляем все средние баллы в список
    print(school_middle) # выводим полученный список для наглядности
school_all_score = sum(school_middle)/len(school_middle) # делим средние баллы по каждой школе на количество средних баллов по каждому классу
print('Средний балл по всей школе: ', school_all_score) # выводим средни балл по всей школе.