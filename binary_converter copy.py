# define all var's
FROM = 1
INTO = 1
holder = 0
deci_number = 0
bina_number = 0
hexa_number = 0
octa_number = 0
final_number = 0
loop = True

import os

# ask for from
def form_fetch():
  global FROM
  while True:
    FROM = int(input('''What would you like to convert from?:
    '1' for Decimal
    '2' for Binary
    '3' for Hexadecimal
    '4' for Octal
    '''))
    if FROM > 5 or FROM < 0:
      print('please try again')
    else:
      break

# ask for into
def into_fetch():
  global INTO
  while True:
    INTO = int(input('''What would you like to convert into?
    '1' for Decimal
    '2' for Binary
    '3' for Hexadecimal
    '4' for Octal
    '''))
    if INTO > 5 or INTO < 0:
      print('please try again')
    else:
      break

# getting

# get decimal number
def deci_get():
  global deci_number, holder
  while True:
    deci_number = int(input('Please enter an integer more than -1: '))
    if deci_number < 0:
      print('Try again')
    else:
      holder = deci_number
      break

# get binary number
def bina_get():
  global bina_number, holder
  while True:
    bina_number = int(input('Please enter a binary number: '), 2)
    holder = bina_number
    break

# get hex number
def hexa_get():
  global hexa_number, holder
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
      holder = int(haxa_number, 16)
      break
        
# get octal number
def octa_get():
  global octa_number, holder
  while True:
    octa_number = int(input('Please enter a octal number: '))
    for x in octa_number:
      if x > 7 or x < 0:
        print('Try again')
        break
      else:
        continue
      holder = int(octa_number, 8)
      break
    
# converting

# convertion into binary
def bina_convert(numb, mode):
  global hexa_number, octa_number
  final_number = bin(numb)
  if mode == 1:
    print('{} in binary is {}'.format(numb, final_number))
  if mode == 3:
    print('{} in binary is {}'.format(hex(hexa_number), final_number))
  if mode == 4:
    print('{} in binary is {}'.format(oct(octa_number), final_number))

def hexa_convert(numb, mode):
  global bina_number, octa_number
  final_number = hex(numb)
  if mode == 1:
    print('{} in hexadecimal is {}'.format(numb, final_number))
  if mode == 2:
    print('{} in hexadecimal is {}'.format(bin(bina_number), final_number))
  if mode == 4:
    print('{} in hexadecimal is {}'.format(oct(octa_number), final_number))
  
def deci_convert(numb, mode):
  global bina_number, octa_number, octa_number
  final_number = numb
  if mode == 2:
    print('{} in decimal is {}'.format(bin(bina_number), final_number))
  if mode == 3:
    print('{} in decimal is {}'.format(hex(hexa_number), final_number))
  if mode == 4:
    print('{} in decimal is {}'.format(oct(octa_number), final_number))

def octa_convert(numb, mode):
  global bina_number, hexa_number
  final_number = oct(numb)
  if mode == 1:
    print('{} in octal is {}'.format(numb, final_number))
  if mode == 2:
    print('{} in octal is {}'.format(bin(bina_number), final_number))
  if mode == 3:
    print('{} in octal is {}'.format(hex(hexa_number), final_number))


# just to be safe I have put the main at the bottom :)
# numbers and presenting:
while loop == True:
  os.system('cls')
  form_fetch()
  into_fetch()
  if FROM == 1:
    deci_get()
  elif FROM == 2:
    bina_get()
  elif FROM == 3:
    hexa_get()
  elif FROM == 4:
    octa_get()
  else:
    print('This is a catastrophe!')
  
  if INTO == 1:
    deci_convert(holder, FROM)
  elif INTO == 2:
    bina_convert(holder, FROM)
  elif INTO == 3:
    hexa_convert(holder, FROM)
  elif INTO == 4:
    octa_convert(holder, FROM)
  else:
    print('This is another catastrophe!')
    
  check = int(input('''To try another number type '1'.
  To to exit type '2'.'''))
  if check == 1:
    loop == True
    os.system('cls')
    print('Restarting')
  elif check == 2:
    loop == False
    print('Goodbye')
    os.system('cls')
    break
    
