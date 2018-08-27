'''
Created on 02-Sep-2017

@author: anshu
'''
number=int(input('Please enter a number: '))

i = 2

while i<number:
    if number%i == 0:
        print ("Your number is NOT a prime number!");
        break
    else:
        print ("Your number is a prime number!");
        break