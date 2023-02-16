values = []
check_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
conv = 'to convert'

number = 0
base = 2

counting = ''

def make_values(base):
    global values
    for i in range(12, -1, -1):
        values.append(base ** i)

def making_final():
    global counting, values, number, check_list
    for part in values:
        if number >= part:
            counting += "1"
            number -= part
        else:
            counting += check_list[0]
            
def inputing(filler):
    global loop
    while True:
        number = input('What do you want ' + filler + '? ')
        try:
            output = int(number)
            return output
        except:
            print('please give me a number')
        

number = inputing('to convert')
make_values(base)
making_final()
print(values)
print(counting)
