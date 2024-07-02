# PASSWORD GENERATOR
import random
userInput = int(input("\nEnter The Length of password:- "))
letter="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
small_letter="abcdefghijklmnopqrstuvwxyz"
num="1234567890"
special_character="!@#$%^&*"
ratio1 = userInput // 3
ratio2 = userInput % 3

def passwordGenerator(userInput):
    password=""
    for i in range(ratio1):
        password += letter[random.randint(0,25)]
        password += small_letter[random.randint(0,25)]
        password += num[random.randint(0,9)]
    for i in range(ratio2):
        password += special_character[random.randint(0,7)]
    return password
print(f"\nYOUR GENERATED PASSWORD IS:- {passwordGenerator(userInput)}\n")
        
