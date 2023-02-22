# find prime numbers in specified range
# 1 make list for prime numbers
# 2 count up, and divide by all in list
# 3 make it have an adjustible end

prime_list = [2]
waiting_list = []
problem = []
loop = True
limit = 20

for i in range(2, limit):
    for item in prime_list:
        num = i / item
        if type(num) == float:
            waiting_list.append(i)
        elif type(num) == int:
            if num == 1:
                waiting_list.append(i)
                prime_list.append(i)
            else:
                waiting_list = []
        else:
            print('somethings wrong.')
            problem.append(i)
            waiting_list = []
        
                
        
print(prime_list)
print(problem)
print(waiting_list)