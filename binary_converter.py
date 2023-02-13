# ask for from
while True:
  FROM = int(input('''What would you like to convert from?:
  '1' for Decimal
  '2' for Binary
  '3' for Hexadecimal
  '4' for Octal
  '''))
  if FROM > 5 or < 0:
    print('please try again')
  else:
    break

# ask for into
while True:
  INTO = int((input'''What would you like to convert into?:
  '1' for Decimal
  '2' for Binary
  '3' for Hexadecimal
  '4' for Octal
  '''))
  if FROM > 5 or < 0:
    print('please try again')
  else:
    break

# getting

# get decimal number
def deci_get():
  while True:
    deci_number = int(input('Please enter an integer more than -1: '))
    if deci_number < 0:
      print('Try again')
    else:
      break

# get binary number
def bina_get():
  while True:
    bina_number = int(input('Please enter a binary number: '))
    for x in bina_number:
      if x > 1 or x < 0:
        print('Try again')
        break
      else:
        continue
      break

# get hex number
def hexa_get():
  while True:
    hexa_number = input('Please enter a hexadecimal number: ')
    for x in hexa_number:
      if x < 10 and x > -1:
        continue
      elif x == 'a' or x == 'A':
        continue
      elif x == 'b' or x == 'B':
        continue
      elif x == 'c' or x == 'C':
        continue
      elif x == 'd' or x == 'D':
        continue
      elif x == 'e' or x == 'E':
        continue
      elif x == 'f' or x == 'F':
        continue
      else:
        print('Try again') 
        break
      break
        
# get octal number
def octa_get():
  while True:
    octa_number = int(input('Please enter a octal number: '))
    for x in octa_number:
      if x > 7 or x < 0:
        print('Try again')
        break
      else:
        continue
      break
    
# converting

# number into decimal
def into_deci(numb, mode):
  if mode

# convertion into binary
def bina_convert(numb):
  bin_number = bin(numb)
  print('{} in binary is {}'.format(numb, bin_number))
