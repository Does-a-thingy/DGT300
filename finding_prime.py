# find prime numbers in specified range
# 1 make list for prime numbers
# 2 count up, and divide by all in list
# 3 make it have an adjustible end

prime_list = [2]
waiting_list = []
problem = []
loop = True
limit = 20
stop = 1

def max_range(base, numb):
    global waiting_list, escape
    waiting_list = []
    product = 1 # define product
    product = numb//base # whole number of bases that can go into number
    leftovers = numb - (base*product) # get rid of as much as possible
    if leftovers > 0:
        waiting_list = [] # empty list
        waiting_list.append(numb) # add tp the now empty list
    elif leftovers == 0:
        waiting_list == []
    else:
        print('def else')

for i in range(3, (limit + 1)): # for each number up to limit
    for item in prime_list: # check against every value in list
        if len(waiting_list) == 0:
            max_range(item, i)
            
        else:
            pass
        if len(waiting_list) == 0:
            break
    if len(waiting_list) == 1 and stop == 1:
        prime_list.append(waiting_list[0])
        waiting_list = []
    else:
        print('escape else', i)
        waiting_list = []
        
    


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
print(problem)
print(waiting_list)