alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color']) 
print(alien_0['points']) 

alien_0 = {'color':'green', 'points': 5}
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0) 

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5

alien_0 = {'color': 'green'}

print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'

print("The alien is now " + alien_0['color'] + ".") 


alien_0 = {'x_position': 1,'y_position': 25, 'speed': 'medium'}

print("Original x-position: " + str(alien_0['x_position']))

if alien_0['speed'] == 'slow': 
    x_increment = 1
elif alien_0['speed'] == 'high': 
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position'])) 


alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0) 

#Um dicionário de objetos semelhantes

favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 
    'phil': 'python' }

print("Sarah's favorite language is " +  favorite_languages['sarah'].title() +
    ".") 

#Percorrendo todos os pares chave-valor com um laço

user_0 = {'username': 'efermi', 'first': 'enrico', 'last': 'fermi', }

for key, value in user_0.items(): 
    print("\nKey: " + key) 
    print("Value: " + value) 

favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python', }

for name, language in favorite_languages.items(): 
    print(name.title() + "'s favorite language is " + language.title() + ".")     

#Percorrendo todas as chaves de um dicionário com um laço
 
for name in favorite_languages.keys(): 
    print(name.title())     

friends = ['phil', 'sarah']
for name in favorite_languages.keys(): 
    print(name.title())
    if name in friends: 
        print(" Hi " + name.title() + ", I see your favorite language is " +
        "favorite_languages[name].title()" + "!")

#Percorrendo as chaves de um dicionário em ordem usando um laço

for name in sorted(favorite_languages.keys()): 
    print(name.title() + ",thank you for taking the poll.") 

#Percorrendo todos os valores de um dicionário com um laço

print("The following languages have been mentioned:")

for language in favorite_languages.values(): 
    print(language.title())

print("The following languages have been mentioned:") 

for language in set(favorite_languages.values()): 
    print(language.title()) 

#Uma lista de dicionários

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]

for alien in aliens: 
    print(alien)

aliens = []
# Cria 30 alienígenas verdes 
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
# Mostra os 5 primeiros alienígenas 
for alien in aliens[:5]:
    print(alien) 
    print("...")
# Mostra quantos alienígenas foram criados y 
print("Total number of aliens: " + str(len(aliens))) 

aliens = []
# Cria 30 alienígenas verdes 
for alien_number in range (0,30): 
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[0:3]: 
    if alien['color'] == 'green': 
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
# Mostra os 5 primeiros alienígenas for alien in aliens[0:5]:
print(alien) 
print("...") 

for alien in aliens[0:3]: 
    if alien['color'] == 'green': 
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow': 
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

#Uma lista em um dicionário

pizza = {'crust': 'thick', 'toppings': ['mushrooms', 'extra cheese'], }
# Resume o pedido
print("You ordered a " + pizza['crust'] + "-crust pizza " + "with the following toppings:")
    
for topping in pizza['toppings']: 
    print("\t" + topping)        


favorite_languages = { 'jen': ['python', 'ruby'],
'sarah': ['c'], 'edward': ['ruby', 'go'], 'phil': ['python', 'haskell'], }

for name, languages in favorite_languages.items(): 
    print("\n" + name.title() + "'s favorite languages are:") 
    for language in languages:
        print("\t" + language.title()) 


#Um dicionário em um dicionário
users = {
    'aeinstein': {
    'first': 'albert', 'last': 'einstein', 'location': 'princeton', },
    'mcurie': { 'first': 'marie', 'last': 'curie', 'location': 'paris', },
}

for username, user_info in users.items(): 
    print("\nUsername: " + username) 
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title()) 
    print("\tLocation: " + location.title()) 