def print_lst(lst):
    if not lst:
        print("Saraksts ir tukšs")
        return
    print("Studenti: ")
    for val in lst:
        print(val)


def add(lst):
    user_in = input("Kādu elementu vēlaties pievienot?\n")
    lst.append(user_in)


def remove_val(lst):
    if not lst:
        print("Saraksts ir tukšs")
        return

    user_in = input("Kuru elementu vēlaties dzēst?\n")
    lst.remove(user_in)


def remove_index(lst):
    if not lst:
        print("Saraksts ir tukšs")
        return

    user_in = int(input("Kuru elementu vēlaties dzēst?\n"))
    lst.pop(user_in)


def search(lst):
    if not lst:
        print("Saraksts ir tukšs")
        return

    user_in = input("Kuru elementu vēlaties atrast?\n")
    found = True
    for i in range(0, len(lst)):
        if lst[i] == user_in:
            found = True
            print(f"Atrada {user_in} {i}. pozīcijā")
    if not found:
        print("Neko neatrada")


if __name__ == '__main__':
    student_lst = []
    while True:
        print("1- Izvadīt")
        print("2- Pievienot")
        print("3- Dzēst")
        print("4- Dzēst pēc indeksa")
        print("5- Atrast")
        print("0- Iziet")
        choice = input("Ko velaties darit?\n")

        if choice == "1":
            print_lst(student_lst)
        elif choice == "2":
            add(student_lst)
        elif choice == "3":
            remove_val(student_lst)
        elif choice == "4":
            remove_index(student_lst)
        elif choice == "5":
            search(student_lst)
        elif choice == "0":
            break
        else:
            print("Nav ievadīta pareiza vērtība")

