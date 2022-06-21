# funkce 1 = words
    # funkce je zabudovana v kodu

# funkce 2 = tittlecase
def count_tittle_case_letters(str_obj):
    count_tittle = 0
    for elem in str_obj.strip().split():
        if elem[0].istitle():
            count_tittle += 1
    return count_tittle

#funkce 3 = uppercase
def count_upper_case_letters(str_obj):
    count_upper = 0
    for elem in str_obj:
        if elem.isupper():
            count_upper += 1
    return count_upper

#funkce 4 = lowercase
def count_lower_case_letters(str_obj):
    count_lower = 0
    for elem in str_obj:
        if elem.islower():
            count_lower += 1
    return count_lower

#funkce 5 = numeric
def count_numeric_case(str_obj):
    count_numeric = 0
    for elem in str_obj:
        if elem.isnumeric():
            count_numeric += 1
    return count_numeric

# funkce 6 = sum of all numbers
def sum_digits(str_obj):
    return sum(int(x) for x in (str_obj) if x.isdigit())

# funkce 7 = cetnosti
def cetnost (str_obj):
    seznam = dict()
    for x in str_obj.split():
        if len(x) not in seznam.keys():
            seznam[len(x)] = 1
        else:
            seznam[len(x)] += 1
    return seznam