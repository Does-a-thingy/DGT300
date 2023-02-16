variable = 4
values = []
number = 106
final = ''
list = ['0','1','2','3','4']
count = 0

for i in range(4, -1, -1):
    values.append(variable ** i)
    
print(values)
    
for item in values:
    if number >= item:
        while number >= item:
            count += 1
            number -= item
        final = list[count]
        count = 0
    else:
        final += '0'

print(final)
print(number)