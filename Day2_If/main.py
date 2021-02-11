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


if __name__ == '__main__':
    task2()

    # to_string_sample()


