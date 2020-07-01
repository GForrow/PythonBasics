
file = open("teams.txt", "w")

for n in range(1, 6):
    newline = "Team number " + str(n) + "\n"
    file.write(newline)
file.close()

file = open("teams.txt", "r")
print(file.readline())
file.readline()
file.readline()
print(file.readline())

file.close()

file = open("teams.txt", "a")
appendline = "added this line after"
file.seek(0)
file.write(appendline)
file.close()

