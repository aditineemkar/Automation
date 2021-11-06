# print("A Digital Calculator")
# input1=input('Enter the first number: ')
# input2 = input("Enter the second number: ")
# print("Which mathematical operation do you want to perform?")
# print("Type 1 for addition")
# print("Type 2 for subtraction")
# print("Type 3 for multiplication")
# print("Type 4 for division")
# input_operation = input("Enter the number: ")
# input1_str = int(input1)
# input2_str = int(input2)
# if input_operation==1:
#     print(input1_str+input2_str)
# elif input_operation==2:
#     print(input1_str-input2_str)
# elif input_operation==3:
#     print(input1_str/input2_str)
# elif input_operation==4:
#     print(input1_str*input2_str)

import os
choice= input("What do you wish? (Shutdown / Restart): ")

if choice=="Shutdown":
    os.system("shutdown /s /t 1")
elif choice=="Restart":
    os.system("shutdown /r /t 1")
