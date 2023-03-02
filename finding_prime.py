# find prime numbers in specified range
# 1 make list for prime numbers
# 2 count up, and divide by all in list
# 3 make it have an adjustible end

prime_list = [2]
waiting_list = []
problem = []
loop = True
limit = 20
bad = 0
x = True

limit = int(input('give me the limit: '))

def max_range(base, numb):
    global waiting_list, bad
    product = numb//base # whole number of bases that can go into number
    leftovers = numb - (base*product) # get rid of as much as possible
    if leftovers == 0:
        bad = 1

for i in range(0, (limit + 1)): # for each number up to limit
    waiting_list = []
    if i != 0 and i != 1:
        for item in prime_list: # check against every value in list
            max_range(item, i)
        if bad == 0:
            prime_list.append(i)
            print(prime_list)
            bad = 0
        else:
            bad = 0
    elif i == 2:
        prime_list.append(2)
    


        #num = i / item
        #try:
            #number = int(num)
            #if number == 1:
                #print('if')
            #elif num > 1:
                #print('elif')
                #if type(i/item) == float:
                    #prime_list.append(i)
                #else:
                    #waiting_list.append(i)
            #else:
                #print('else')
                #waiting_list = []
        #except:
            #print('problem ' + i)
            #problem.append(i)
        
print(prime_list)