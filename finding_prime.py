# find prime numbers in specified range
# 1 make list for prime numbers
# 2 count up, and divide by all in list
# 3 make it have an adjustible end

prime_list = []
waiting_list = []
problem = []
loop = True
limit = 20
bad = 0
x = True

def ask_input():
    while True:
        num = input('Please choose the limit over 0: ')
        try:
            num = int(num)
            if num < 0:
                print('please try again')
            else:
                return num
        except:
            print('please try again')

def max_range(base, numb):
    global waiting_list, bad
    product = numb//base # whole number of bases that can go into number
    leftovers = numb - (base*product) # get rid of as much as possible
    if leftovers == 0:
        bad = 1


limit = ask_input()

for i in range(0, (limit + 1)): # for each number up to limit
    waiting_list = []
    if len(prime_list) == 1000:
        print('1000, still working')
    elif len(prime_list) == 2000:
        print('2000, still working')
    elif len(prime_list) == 3000:
        print('3000, still working')
    elif len(prime_list) == 4000:
        print('4000, still working')
    elif len(prime_list) == 5000:
        print('5000, still working')
    elif len(prime_list) == 6000:
        print('6000, still working')
    elif len(prime_list) == 7000:
        print('7000, still working')
    elif len(prime_list) == 8000:
        print('8000, still working')
    elif len(prime_list) == 9000:
        print('9000, still working')    
    if i != 0 and i != 1:
        for item in prime_list: # check against every value in list
            max_range(item, i)
        if bad == 0:
            prime_list.append(i)
            bad = 0
        else:
            bad = 0
    elif i == 2:
        prime_list.append(2)
    else:
        pass

print(prime_list, '\n', len(prime_list))