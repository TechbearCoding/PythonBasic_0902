def for_loop_sample():
    x = 0
    for i in range(10):
        print(i)
        x = x + i

    print("-------------")
    print(x)


def task3_1():
    stars = ""

    for i in range(5):
        stars = stars + "*"
        print(stars)


def task3_2():
    for i in range(5, 0, -1):
        print("*" * i)

    for i in reversed(range(1, 6)):
        print("*" * i)


if __name__ == '__main__':
    task3_2()

