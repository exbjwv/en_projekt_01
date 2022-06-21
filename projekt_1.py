"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Václav Svoboda
email: vacsvoboda@gmail.com
discord: XXXX
"""

from projekt_1_fce import *
from task_template import *

#vstupy
registrovani = {"bob":"123","ann":"pass123","mike":"password123","liz":"pass123"}
sep = "+" * 30


#program
username = input("Your username: ")
if username in registrovani:
    userpass = input("Your password: ")
    print(sep)
    if userpass == registrovani[username]:
        print(f"Welcome, user {username}, U are logged in")
        print(sep)
        print(f"Text offer: {TEXTS[0]} (1), {TEXTS[1]} (2), {TEXTS[0]} (3)")
        print(sep)
        vyber = (input("Choose text (1/2/3): "))
        print(sep)
        if vyber == "1" or vyber == "2" or vyber == "3":
            vyber_cislo = int(vyber)
            vybrany_text = TEXTS[vyber_cislo - 1]
            print(f"YOUR CHOICE nr. {vyber_cislo} is: {vybrany_text}")
            print(sep)
            print("TEXT STATS:")

            # funkce 1 = words
            print(f"There are {len(vybrany_text.split())} words in the selected text.")

            # funkce 2 = tittlecase
            count_tittle = count_tittle_case_letters(vybrany_text)
            print(f"There are {count_tittle} titlecase words.")

            # funkce 3 = uppercase
            count_upper = count_upper_case_letters(vybrany_text)
            print(f"There are {count_upper} uppercase words.")

            # funkce 4 = lowercase
            count_lower = count_lower_case_letters(vybrany_text)
            print(f"There are {count_lower} lowercase words.")

            # funkce 5 = numeric
            count_numeric = count_numeric_case(vybrany_text)
            print(f"There are {count_numeric} numeric strings.")

            # funkce 6 = sum of all numbers
            sum_dig = sum_digits(vybrany_text)
            print(f"The sum of all the numbers {sum_dig}")
            print(sep)

            # funkce 7 cetnosti
            pocet_cetnosti = cetnost(vybrany_text)
            print("LEN|  OCCURENCES  |NR.:")
            print(sep)
            for k, v in pocet_cetnosti.items():
                print(f'{k:>3}| {v * "*":<13}|{v}')

        else:
            print("Wrong choice, quiting")
            quit()
    else:
        print(f"Invalid password for username {username}")
        quit()
else:
    print("Unregistred username")
    quit()
