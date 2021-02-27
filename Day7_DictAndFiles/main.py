import studentParser as stParse


def task1():
    name = input("Ievadiet vārdu!\n")
    last_name = input("Ievadiet uzvārdu!\n")
    course = int(input("Ievadiet kursu!\n"))

    student_dict = stParse.create_student_dict(name, last_name, course)
    for key, val in student_dict.items():
        print(key + ": " + str(val))


def sample():
    # f = open("test.txt", "w")
    # f.write("Musu pirmais fails\n")
    # f.write("jauna rinda\n")
    # f.close()

    f = open("test.txt", "r")
    # in_range = [0, 1]
    # # print(f.read())
    for position, line in enumerate(f):
        if position == 0:
            a = line.rstrip("\n")
            print(a)
    print("aaa")
    # lines_list = f.readlines()
    # print(lines_list)

    f.close()


def read(filepath):
    f = open(filepath, "r", encoding="utf-8")
    file_list = f.readlines()
    f.close()
    return file_list


def write(filepath, poem_lst):
    f = open(filepath, "w", encoding="utf-8")
    rev = []
    for i in range(len(poem_lst)-1, -1,-1):
        rev.append(poem_lst[i])
    f.writelines(rev)
    f.close()


if __name__ == '__main__':
    poem = read("C:/Users/Marti//Desktop/eglite.txt")
    write("C:/Users/Marti//Desktop/eglite2.txt", poem)