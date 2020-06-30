import random

def examScore():

    name = str(input("What is your name?: "))
    hwScore = int(input("What was your homework score?: "))
    assScore = int(input("What was your assessment score?: "))
    examScore = int(input("What was your exam score?: "))
    totalScore = ((hwScore + assScore + examScore) / 175) * 100

    print("Your total score is:", totalScore)

    if totalScore >= 85:
        print(name, "you have passed with distinction.")
    elif totalScore >= 65:
        print(name, "you have passed.")
    else:
        print(name, "you have failed.")

def dice(numofdice):
    for i in range(numofdice):
        print("Dice number", i+1, "is:", random.randint(1, 6))