import logic as l


def task1():
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
            l.print_lst(student_lst)
        elif choice == "2":
            l. add(student_lst)
        elif choice == "3":
            l.remove_val(student_lst)
        elif choice == "4":
            l.remove_index(student_lst)
        elif choice == "5":
            l.search(student_lst)
        elif choice == "0":
            break
        else:
            print("Nav ievadīta pareiza vērtība")


def dict_sample():
    sample = {
        "studentName": "Test1",
        "studentLastName": "Test2",
        "course": 3
    }

    for val in sample.values():
        print(val)

    for val in sample.keys():
        print(val)

    for key, val in sample.items():
        print(str(key) + ": " + str(val))

    lst_of_dict = [
        {
            "studentName": "Test1",
            "studentLastName": "Test2",
            "course": 3
        },
        {
            "studentName": "Test1",
            "studentLastName": "Test2",
            "course": 3
        }

    ]
    print(sample)
    print(sample["studentName"])


if __name__ == '__main__':
    dict_sample()

