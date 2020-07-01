file = open("examplefile.txt", "w")

for n in range(1, 11):
    newline = "This is line " + str(n) + "\n"
    file.write(newline)
file.close()

file = open("examplefile.txt", "r")

print("First Line: " + file.readline())
print("Second Line: " + file.readline())
print("Rest of file: " + file.read())
print("Final blank line: " + file.readline())

file.close()

file = open("examplefile.txt", "r")
file.close()
