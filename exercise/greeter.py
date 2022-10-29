"""Devolve um nome completo formatado de modo elegante."""
def get_formatted_name(first_name,last_name):    
    full_name = first_name + ' ' + last_name 
    return full_name.title()
# Este é um loop infinito!
while True:
    print("\nPlease tell me your name:") 
    f_name = input("First name: ") 

    if f_name == 'q':
        break
    
    l_name = input("Last name: ")  
    
    if l_name == 'q': 
        break

    formatted_name = get_formatted_name(f_name, l_name) 
    print("\nHello, " + formatted_name + "!") 