# find prime numbers in specified range
# 1 make list for prime numbers
# 2 count up, and divide by all in list
# 3 make it have an adjustible end

prime_list = [2]
waiting_list = []
problem = []
loop = True
limit = 20

def max_range(base, numb):
    powered = 1
    i = 0
    limit = 1
    while limit > 0:
        i += 1
        powered = base ** i
        limit = numb//powered


for i in range(3, limit):
    for item in prime_list:
        num = i / item
        try:
            number = int(num)
            if number == 1:
                print('if')
            elif num > 1:
                print('elif')
                if type(i/item) == float:
                    prime_list.append(i)
                else:
                    waiting_list.append(i)
            else:
                print('else')
                waiting_list = []
        except:
            print('problem ' + i)
            problem.append(i)
        
                
        
print(prime_list)
print(problem)
print(waiting_list)