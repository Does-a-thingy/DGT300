values = [16, 1]
check_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

number = 0
base = 16
counting = ''
intre = True

def making_final():
    global counting, values, number, check_list
    for part in values:
        if number >= part:
            num = number//part #gives whole number after division round down, ignore left over
            counting += check_list[num] # allows for up to base 36
            number -= part*num
        else:
            counting += check_list[0]

def main():
    
    while intre is True:
        making_final()
        if inp == 'yes':
            number = 0
            base = 2
            end_value = 1
            intre = True
            counting = ''
            values = []
        else:
            intre = False
