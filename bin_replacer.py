values = []
check_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

number = 11
base = 2

counting = '0'

def make_values(base):
    global values
    for i in range(8, -1, -1):
        values.append(base ** i)

def making_final():
    global counting, values, number, check_list
    for part in values:
        if number >= part:
            counting += "1"
            number -= part
        else:
            counting += "0"


make_values(base)
making_final()
print(values)
print(counting)
