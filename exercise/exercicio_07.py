
# prompt com várias linhas e escrever uma instrução e input
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt) 
print("\nHello, " + name  + "!") 

#Usando int() para aceitar entradas numéricas

age = input("How old are you? ") 
age = int(age) 
age >= 18

height = input("How tall are you, in inches? ") 
height = int(height)
if height >= 36: 
    print("\nYou're tall enough to ride!") 
else:
    print("\nYou'll be able to ride when you're a little older.") 

#Operador de módulo

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0: 
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")

current_number = 1

while current_number <= 5: 
    print(current_number) 
    current_number += 1
    

