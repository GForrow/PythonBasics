logpiles = [2, 2, 1, 1, 1, 1, 1, 4, 1]
logsToStack = int(input("How many logs are being added?: "))

while logsToStack > 0:
    for i in logpiles:
        if logpiles[i] == min(logpiles): #if the increment is equal to smallest value in array
            logpiles[i] += 1 #add +1 to the value of that increment
            logsToStack -= 1 #take a log from the stack
            print("Remaining logs to stack: ", logsToStack)

print(logpiles) #print final logpile array

