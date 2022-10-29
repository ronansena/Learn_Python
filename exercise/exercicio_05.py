cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:  
    if car == 'bmw': 
        print(car.upper()) 
    else:
        print(car.title()) 

#Verificando se um valor está em uma lista

requested_toppings = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in requested_toppings: 
    print(requested_toppings[0].upper()) 
if 'pepperoni' in requested_toppings: 
    print(requested_toppings[2].upper()) 

#Verificando se um valor não está em uma lista

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users: 
    print(user.title() + ", you can post a response if you wish.") 

age = 12

if age < 4: 
   price = 0
elif age < 18: 
   price = 7
elif age < 65: 
   price = 10
else: 
   price = 5

print("Your admission cost is $" + str(price) + ".") 


age = 12
if age < 4: 
    price = 0
elif age < 18: 
    price = 5
elif age < 65: 
    price = 10
elif age >= 65: 
    price = 9
print("Your admission cost is $" + str(price) + ".")


requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings: 
    print("Adding mushrooms.") 
if 'pepperoni' in requested_toppings: 
    print("Adding pepperoni.") 
if 'extra cheese' in requested_toppings: 
    print("Adding extra cheese.")
    print("\nFinished making your pizza!")

#Esse código não funcionaria de modo apropriado se tivéssemos usado
#um bloco if -elif-else , pois o código pararia de executar depois que
#apenas um teste tivesse passado. 

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings: 
    print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!") 

print("Verificando itens especiais\n")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings: 
    if requested_topping == 'green peppers': 
        print("Sorry, we are out of green peppers right now.")
    else: 
        print("Adding " + requested_topping + ".")
        print("\nFinished making your pizza!")

print("\nVerificando se uma lista não está vazia\n")

requested_toppings = []
if requested_toppings: 
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".") 
        print("\nFinished making your pizza!") 
else: 
    print("Are you sure you want a plain pizza?")         

print("\nUsando várias listas\n")

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings: 
    if requested_topping in available_toppings: 
        print("Adding " + requested_topping + ".") 
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!\n") 