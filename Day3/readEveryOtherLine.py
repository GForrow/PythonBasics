file = open("examplefile.txt", "r")

outfile = ""

for line in range(1, 11):
    if line % 2 == 0:
        outfile += file.readline()
    else:
        file.readline()

file = open("outputfile.txt", "w")
file.write(outfile)
file.close()
