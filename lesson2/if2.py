def sravnenie_strok(stroka1, stroka2):
    if type(stroka1) != str:
        print("0")
    if type(stroka2) != str:
        print("0")
    if stroka1 == stroka2:
        print("1")
    if len(stroka1) > len(stroka2):
        print("2")
    if stroka1 != "learn":
        print("3")
print(sravnenie_strok("Python", "learn"))