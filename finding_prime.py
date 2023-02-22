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
                prime_list.append(number)
                if output >= 0:
                    print('if statement ' + output)
                    loop = False
                    break
                else:
                    prime_list.append()
                    print('else statement ' + output)
                    loop = False
                    break
            except:
                print('except statement ' + str(output))
                loop = False
                break
            break
        
print(prime_list)