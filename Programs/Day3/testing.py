def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
            return True


#print(is_prime(11))

item_list = ["burger", "hotdog", "bun", "ketchup", "cheese"]
n = 0

while n < 5:
    for i in item_list:
        print(item_list[n])
        n += 1

print(item_list[4])
