###################################################################
# Python Challenge Level 1 Solution
# Wilson Woods
# 10/16/19
# Program translates a string where all chars are shifted by a set amount
# In this case shift is +2 (a = c, b = d, etc.)
# increment = [shift amount] & decrement = [26 - shift amount]
###################################################################
increment = 2
decrement = 24

mystring = raw_input('Enter string: ')

for c in mystring:
   
    if ord(c) < 97:
        print (c),
    elif ord(c) > 120:
        newAsc = ord(c) - decrement
        newChar = chr(newAsc)
        print(newChar),
    else:
        newAsc = ord(c) + increment
        newChar = chr(newAsc)
        print(newChar),
