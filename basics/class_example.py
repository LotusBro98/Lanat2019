class Human:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        return self.name + " " + self.surname + " (" + str(self.age) + ")"

    def is_graduated(self):
        return self.age >= 18

    def grow_up(self):
        self.age = self.age + 1

list = [Human("Vasya", "Ivanov", 20), Human("Petya", "Sidorov", 15),
        Human("Roma", "Petrov", 17)]
for item in list:
    print(item, item.is_graduated())
    item.grow_up()
    print("After growing up:", item, item.is_graduated())

list_graduated_only = [item for item in list if item.is_graduated()]
print("Graduated humans:")
for item in list_graduated_only:
    print(item, item.is_graduated())
