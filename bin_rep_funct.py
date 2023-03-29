values = []
check_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
conv = 'to convert'

number = 0
base = 2
end_value = 1
counting = ''
intre = True

def max_range(base, numb):
    powered = 1
    i = 0
    limit = 1
    while limit > 0:
        i += 1
        powered = base ** i
        limit = numb//powered
    return i

def make_values(base, limit):
    global values
    for i in range(limit, -1, -1):
        values.append(base ** i)

def making_final():
    global counting, values, number, check_list
    for part in values:
        if number >= part:
            num = number//part #gives whole number after division round down, ignore left over
            counting += check_list[num] # allows for up to base 36
            number -= part*num
        else:
            counting += check_list[0]

def inputing(filler, check):
    while True:
        number = input('What do you want ' + filler)
        try:
            output = int(number)
            if output >= 0:
                if check == 0:
                    return output
                elif check == 1 and output >= 2 and output <= 36:
                    return output
                else:
                    print('please give me a valid number')
            else:
                print('please give me a valid number')
        except:
            print('please give me a valid number')

def main():
    intre = True
    while intre is True:
        number = inputing('to convert? make sure it is more than -1: ', 0)
        base = inputing('for base? make sure it is between 1 and 37: ', 1)
        end_value = max_range(base, number)
        make_values(base, end_value)
        making_final()
        print(values)
        print(counting)
        if inp == 'yes':
            number = 0
            base = 2
            end_value = 1
            intre = True
            counting = ''
            values = []
        else:
            intre = False
