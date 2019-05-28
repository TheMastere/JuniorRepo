def comparison_strings(string1, string2):
    if type(string1) != str:
        return ("0")
    if type(string2) != str:
        return ("0")
    if string1 == string2:
        return ("1")
    if len(string1) > len(string2):
        return ("2")
    elif string1 != "learn" or string1 != string2:
        return ("3")
print(comparison_strings("learj", "learn"))