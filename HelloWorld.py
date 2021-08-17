'''
Created on Nov 9, 2020

@author: arpaghos
'''

from project.bank import bank
#Hello World
print('hello World')

#variable test
# _a = 23
# print(_a)
# 
# a=b=c = 67
# print(b)
# 
# d="Hi 'Arpan', I am here"
# print(d)
# 
# strData = "Hi I am Arpan"
# print(strData.split(' '))
# 
# 
# #age = input('enter your age: ')
# def verifyAge(age):
#     if(age < 18):
#         print('My age is below 18')
#     elif (age == 18):
#         print('My age is 18')
#     else:
#         print('My age is above 18')
#         
# print('Enter your age:')
# data = input()
# intData = int(data)
# verifyAge(intData)
# 
# for x in range(6):
#     print(x)
# else:
#     print("Finally finished!")


bankObj = bank('SBI123', 'SBI', 'Garia', 'Kolkata')
print(bankObj.getSavingAccountInfo())
