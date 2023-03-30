values = [16, 1]
check_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

def making_final(number):
    global values, check_list
    counting = ''
    for part in values:
        if number >= part:
            num = number//part #gives whole number after division round down, ignores leftovers
            counting += check_list[num] # pulls from letters and numbers
            number -= part*num # gets rid of parts times num
        else:
            counting += check_list[0] # will slap a zero on it if theres nothing
    return counting

