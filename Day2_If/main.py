def task1():
    # variants 1
    # print('Ievadiet dzīvesvietu!')
    # placeOfLiving = input()

    # variants 2

    place_of_living = input('Ievadiet dzīvesvietu!\n')
    print("Jūsu dzīvesvieta ir " + place_of_living)


def task2():
    number1 = int(input("Ievadiet 1. skaitli!\n"))
    number2 = int(input("Ievadiet 2. skaitli!\n"))

    print("Summa: " + str(number1 + number2))
    print("Starpība: " + str(number1 - number2))


def task3():
    number1 = int(input("Ievadiet 1. skaitli!\n"))
    number2 = int(input("Ievadiet 2. skaitli!\n"))

    choice = input("Ievadiet + vai -")

    if choice == "+":
        print("Summa: " + str(number1 + number2))
    elif choice == "-":
        print("Starpība: " + str(number1 - number2))
    else:
        print("Kļūda!!!")


def integer_sample():
    sample_number = int(input("Ievadiet skaitli!\n")) # ar int() norada, ka inputs bus integers
    print(sample_number)


def float_sample():
    sample_number = float(input("Ievadiet skaitli ar komatu!\n"))
    # ar float() norada, ka inputs bus skaitlis ar komatu
    print(sample_number)


def to_string_sample():
    sample_number = float(input("Ievadiet skaitli ar komatu!\n"))
    print(str(sample_number) + " abc") # ar str konverte uz string'u


def var_sample():
    a = "aa"
    # Lokals mainigais "a", kas strada tikai var_sample() funkcija
    print(a)


def if_sample():
    # Izvadit "**", ja cilveka ievadita vertiba ir lielaka par 5, ja ne, tad izvadit "*"
    personal_input = int(input("Ievadiet skaitli!"))

    # >
    # <
    # <=
    # >=
    # ==
    # !=

    if personal_input > 5:
        print("**")
    else:
        print("*")

    string_input = input("ievadiet vardu!")
    if string_input != "aa":
        print("**")
    else:
        print("*")


def if_sample2():
    # lietotajs ievada skaitli, parbaudit vai sis skaitlis ir diapazona no 1 lidz 10
    personal_input = int(input("Ievadiet skaitli!"))

    # if personal_input > 0 and personal_input < 11:  sis ir tas pats, kas rindina zemak
    if 0 < personal_input < 11:
        print("Skaitlis ir diapazona")
    else:
        print("Nav diapazona!")

    # lietotajs ievada skaitli, parbaudit vai sis skaitlis nav diapazona no 1 lidz 10
    if personal_input < 1 or personal_input > 10:
        print("True")
    else:
        print("False")


if __name__ == '__main__':
    task3()

    a = 3
    # Lokals mainigais "a", kas strada tikai main funkcija
    print(a)

    var_sample()

    # a, kurs ir var_sample() nav tas pats a, kurs ir main

    print(a+4)
    # to_string_sample()

    # -------------- if --------------
    if_sample()
