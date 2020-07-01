class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


John = Student("John", 21)
Jim = Student("Jim", 23)

print("John is:", getattr(John, "age"))
