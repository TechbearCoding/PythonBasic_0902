import random


def generate_file(count):
    lst_rows = []
    for i in range(count):
        result = ""
        for j in range(6):
            result += str(random.randint(1, 10)) + ","
        result = result.rstrip(",")
        result += "\n"
        lst_rows.append(result)
    f = open("task1.txt", "w")
    f.writelines(lst_rows)


def read_file():
    f = open("task1.txt", "r")
    file = f.readlines()

    total = 0
    num_count = 0

    for i in range(len(file)):
        file[i] = file[i].rstrip("\n")
        num_list = file[i].split(",")
        num_count = 6 * len(file)
        line_sum = 0
        for val in num_list:
            line_sum += int(val)
        total += line_sum
        print(line_sum)
        print(line_sum/len(num_list))
        print("-------------------")

    print("Total-")
    print(total)
    print(total / num_count)




if __name__ == '__main__':
    # generate_file(4)
    read_file()
