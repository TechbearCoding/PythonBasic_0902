class Student:
    def __init__(self, name, last_name, course):
        self.name = name
        self.last_name = last_name
        self.course = course

    def print_info(self):
        print("Name- " + self.name)
        print("Lastname- " + self.last_name)

    def __private_fun(self):
        print("test")



