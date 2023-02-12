# ask for mode
while True:
  basetype = int(input('''What would you like to convert from?:
  '1' for Decimal
  '2' for Binary
  '3' for Hexadecimal
  '4' for Octal
  '''))
  if basetype > 5 or < 0:
    print('please try again')
  else:
    




# get decimal number
def deci_get():
  while True:
    deci_number = int(input('Please enter an integer more than -1: '))
    if deci_number < 0:
      print('Try again')
    else:
      break

# convertion into binary
def binary_convert(numb):
  bin_number = bin(numb)
  print('{} in binary is {}'.format(numb, bin_number))
