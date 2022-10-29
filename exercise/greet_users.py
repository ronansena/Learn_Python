"""Exibe uma saudação simples a cada usuário da lista."""
def greet_users(names): 
    for name in names: 
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)