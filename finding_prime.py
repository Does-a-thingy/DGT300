# find prime numbers in specified range
# 1 make list for prime numbers
# 2 count up, and divide by all in list
# 3 make it have an adjustible end

prime_list = [2, 3]
loop = True
limit = 20

for num in range(limit):
    for item in prime_list:
        loop = True
        while loop == True:
            try:
                number = num/item
                output = int(number)
                if output >= 0:
                    loop = False
                    continue
                else:
                    prime_list.append()
                    loop = False
                    break
            except:
                prime_list.append()
                loop = False
                break
        
print(prime_list)