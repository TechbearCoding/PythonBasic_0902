def print_string(name):
    print(f'Hi, {name}')


def print_sum(a, b):
    print(a + b)


def default_sample(a="defaultaa vertiba"):
    print(a)


def power(base, pow):
    result = 1

    for i in range(pow):
        result *= base
    return result


def check_string(to_check):
    return 10 <= len(to_check) <= 20 and to_check.isupper() == True


if __name__ == '__main__':

    print(10 % 4)
    # atgriez atlikumu

    a = check_string("AAAAAAAaAAAAAAAAAAA")
    print(a)

    if a:
        print("Viss ir labi")
    else:
        print("Nav labi")
