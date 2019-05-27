def get_summ(num_one, num_two):
    try:
        return int(num_one) + int(num_two)
    except(ValueError):
        print("Необходимо ввести два целых числа")

get_summ(1, "abcd")