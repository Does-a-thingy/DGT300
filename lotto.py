from random import *
import os

# 1) ask user for n numbers
# 2) generate n random numbers - check if already there 
# 3) sort list 
# 4) compare
# 5) count number of 'tickets bought'

n = 6
loop_num = 1
cost = 7
losing = True
interest = True

lowest_tries = 10000000

place = ['1st', '2nd', '3rd', '4th', '5th', '6th']
user_num = []
comp_num = []

def ask_input():
    global user_num, place, n
    user_num = []
    for i in range(n):
        while True:
            num = input('Please choose your ' + place[i] + ' number under 41 and over 0: ')
            try:
                num = int(num)
                if num >= 41 or num < 0:
                    print('please try again')
                else:
                    if num in user_num:
                        print('please try again')
                    else:
                        user_num.append(num)
                        user_num.sort()
                        break
            except:
                print('please try again')
                
def comp_random():
    global comp_num, n
    comp_num = []
    for i in range(n):
        while True:
            number = randint(0,40)
            if number not in comp_num:
                comp_num.append(number)
                break
            else:
                continue

def compare():
    global user_num, comp_num, losing
    comp_num.sort()
    if user_num == comp_num:
        losing = False
    else:
        pass

def win_finish():
    global loop_num, cost, lowest_tries
    print('It cost you ${}.'.format(loop_num * cost))
    print('Best score: ', str(lowest_tries))
    if loop_num < lowest_tries:
        print('New best score: ', str(loop_num))

def main():
    global user_num, comp_num, loop_num, lowest_tries, interest, losing
    while interest == True:
        ask_input()    
        while losing == True:
            comp_random()
            compare()
            print('users number: ', str(user_num))
            print('lotto number: ', str(comp_num))
            print('loop number: ', str(loop_num), ''' 
            ''')
            compare()
            loop_num += 1
        win_finish()
        if loop_num < lowest_tries:
            lowest_tries = loop_num
        value = input('Type yes to enter new numbers: ')
        value.lower()
        value.strip()
        if value == 'yes':
            interest = True
            losing = True
            print('Restarting')
            os.system('cls')
        else:
            interest = False
            print('Goodbye')

main()
