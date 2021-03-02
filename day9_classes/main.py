from student import Student
from pprint import pprint


if __name__ == '__main__':
    student1 = Student("Janis", "Berzins", 1)
    student2 = Student("Juris", "Berzins", 1)

    student2.print_info()
    pprint(vars(student2))
