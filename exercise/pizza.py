def make_pizza(*toppings): #Passando um número arbitrário de argumentos

    """Exibe a lista de ingredientes pedidos."""
    print(toppings)

make_pizza('pepperoni') 
make_pizza('mushrooms', 'green peppers', 'extra cheese') 

def make_pizza(*toppings): 
    """Apresenta a pizza que estamos prestes a preparar."""
    print("\nMaking a pizza with the following toppings:") 
    for topping in toppings: 
        print("- " + topping)

make_pizza('pepperoni') 
make_pizza('mushrooms', 'green peppers', 'extra cheese') 

#Misturando argumentos posicionais e arbitrários

def make_pizza(size, *toppings): 
    """Apresenta a pizza que estamos prestes a preparar."""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:") 
    for topping in toppings:
        print("- " + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
