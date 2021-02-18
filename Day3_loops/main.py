def for_loop_sample():
    x = 0
    for i in range(10):
        print(i)
        # x = x + i
        x += i

    print("-------------")
    print(x)


def while_sample():
    i = 0
    while i < 10:
        print(i)
        i += 1


def while_endless():
    while True:
        print(1)
        user_input = input("Vai velaties iziet?")

        if user_input == "y":
            continue
        print("Nenospieda y")
    print("Pec metodes")


def task3_1():
    stars = ""

    for i in range(5):
        stars += "*"
        print(stars)


def task3_2():
    for i in range(5, 0, -1):
        print("*" * i)

    for i in reversed(range(1, 6)):
        print("*" * i)


def homework_calculator():
    while True:
        number1 = float(input("Kādu skaitli vēlaties ievadīt?\n"))
        number2 = float(input("Kādu skaitli vēlaties ievadīt?\n"))

        choice = input("Ievadīt +,-, * vai /")

        if choice == '+':
            print(number1+number2)
        elif choice == '-':
            print(number1-number2)
        elif choice == '*':
            print(number1*number2)
        elif choice == '/':
            print(number1 / number2)
        else:
            print("Kļūda! Bija jāievada +,-, * vai /")

        exit_calc = input("Vai velaties iziet? Ievadiet y, ja jā.\n")
        if exit_calc.upper() == 'Y':
            break


if __name__ == '__main__':
    homework_calculator()

