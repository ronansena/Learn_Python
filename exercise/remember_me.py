import json

# Carrega o nome do usuário se foi armazenado anteriormente
# # Caso contrário, pede que o usuário forneça o nome e armazena essa informação

filename = 'username.json'

try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    print("We'll remember you when you come back, " + username + "!")
else:
    print("Welcome back, " + username + "!")

#Refatoração 1

def greet_user():
    """Saúda o usuário pelo nome."""
    
    filename = 'username.json'

    try:
        with open(filename) as f_obj:
            username = json.load(f_obj) 
    except FileNotFoundError: 
        username = input("What is your name? ") 
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj) 
            print("We'll remember you when you come back, " + username + "!") 
    else: 
        print("Welcome back, " + username + "!")
        
greet_user()

#refatoração 2

def get_stored_username(): 
    """Obtém o nome do usuário já armazenado se estiver disponível."""
    filename = 'username.json'
    try: 
        with open(filename) as f_obj: 
            username = json.load(f_obj) 
    except FileNotFoundError:
        return None 
    else: 
        return username

def greet_user2(): 
    """Saúda o usuário pelo nome."""
    username = get_stored_username() 
    if username: 
        print("Welcome back, " + username + "!") 
    else: 
        username = input("What is your name? ") 
        filename = 'username.json'

        with open(filename, 'w') as f_obj: 
            json.dump(username, f_obj)
            print("We'll remember you when you come back, " + username + "!")

greet_user2() 

#Refatoração 3


def get_new_username(): 
    """Pede um novo nome de usuário."""
    username = input("What is your name? ") 
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj) 
    return username

def greet_user3(): 
    """Saúda o usuário pelo nome."""
    username = get_stored_username() 
    if username: 
        print("Welcome back, " + username + "!") 
    else: 
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user3() 