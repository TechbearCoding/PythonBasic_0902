import random


def list_sample():
    my_list = [1, 2, 3, 4, 5, 1]
    print(str(my_list[0])+"\n\n")

    # for x in my_list:
    #     print(str(x)+"\n")

    # print(my_list.count(2))

    # for i in range(len(my_list)):
    #     print(my_list[i])

    for i in range(0, len(my_list), 2):
        print(my_list[i])


def list_append():
    my_list = []

    for i in range(5):
        my_list.append(i)

    for x in my_list:
        print(str(x)+"\n")


def task1():
    string_list = []
    length = int(input("Cik elementus vēlies ievadīt?\n"))

    sum_of_len = 0
    for i in range(length):
        string_list.append(input("Ievadiet simbolu virkni!"))
        sum_of_len += len(string_list[i])
    print(sum_of_len/len(string_list))


def task2():
    rand_list = []
    sum_of_nr = 0

    for i in range(5):
        rand_list.append(random.randint(0, 10))
        sum_of_nr += rand_list[i]

    print(rand_list)

    if sum_of_nr > 20:
        print("**")
    else:
        print("*")


def task3():
    a = []
    b = []

    for i in range(5):
        a.append(random.randint(0, 10))

    for i in range(0, len(a)):
        b.append(a[len(a)-1-i])

    # for i in range(4, -1, -1):
    #     b.append(a[i])

    # for i in reversed(range(5)):
    #     b.append(a[i])

    print(a)
    print(b)


def arg_sample(a):
    for x in a:
        print(x)
    a.append(111)


def biggest_number(number_list):
    biggest = number_list[0]
    for val in number_list:
        if val > biggest:
            biggest = val
    return biggest


def search(string_list, item):
    found = False

    for i in range(len(string_list)):
        if item == string_list[i]:
            found = True
            print(i)
    if not found:
        print("Saraksta sadas vertibas nav")


def compare_lists(a, b):
    if len(a) != len(b):
        return False

    a.sort()
    b.sort()

    for i in range(0, len(a)):
        if a[i] != b[i]:
            return False
    return True


def compare_lists2(a, b):
    if len(a) != len(b):
        return False

    a.sort()
    b.sort()

    if a == b:
        return True
    return False


def set_sample():
    dic1 = {4: 'geeks', 1: 'for', 3: 'geeks'}
    lst = [4, 1, 3]
    print(dic1)
    print(lst)

    print(set(dic1))
    print(set(lst))


if __name__ == '__main__':
    # my_list = [-1, -2, -3, -4, -5, -1]
    #
    # string_list = ['AA', 'BB', 'CC', 'AA', 'BB', 'CC']
    # string_list2 = ['AA', 'BB', 'CC']
    #
    # joined = string_list2 + string_list
    # print(joined)
    # search(string_list, 'AA')
    # int_list = [1, 3, 2, 4]
    # int_list2 = [4, 1, 2, 3]
    # print(compare_lists2(int_list, int_list2))

    set_sample()
