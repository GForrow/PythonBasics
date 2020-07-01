count = 0

# while count < 5:
#     name = str(input("What is your name? "))
#     print(name, "is awesome!")
#     count +=1

# for i in range(1, 100):
#     ans = i*i
#     if ans < 2000:
#         print(ans)

vcount =0
word = str(input("Give me a word."))
wordlower = word.lower()
for char in wordlower:
    if (char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'):
        vcount +=1
print(word, "has", vcount, "vowels.")

vcount2 = 0
vowels = "aeiouAEIOU"
for char in word:
    if char in vowels:
        vcount2 += 1
print(word, "has", vcount2, "vowels.")