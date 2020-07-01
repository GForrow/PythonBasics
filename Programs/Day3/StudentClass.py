class Student:

    def __init__(self, name, age, takenclass):
        self.name = name
        self.age = age
        self.takenclass = takenclass

    def testscore(self):
        result = 0
        finalresult = 0
        returnresult = 0
        for i in range(3):
            score = int(input("What did you score on " + self.takenclass + " test number " + str(i+1) + ": "))
            result += score
        finalresult = result / 3
        output = "Your final score for your " + self.takenclass + " tests was: " + str(round(finalresult, 2)) + "%"
        return output


John = Student("John", 21, "Tech")
Jim = Student("Jim", 23, "IT")

print("John is:", getattr(John, "age"))
print(John.testscore())
