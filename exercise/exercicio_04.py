magicians = ['alice', 'david', 'carolina']

for magician in magicians:
    print(magician.title() + ", that was a great joke!") 
    print("I can't wait to see your next trick, " + magician.title() + ".\n") 
    print("Thank you, folks. That was a great magic show!.\n") 

    for magician in magicians:
        print(magician.title() + ", that was a great trick!")  
        print("I can't wait to see your next trick, " + magician.title() + ".\n") 


print("Linha 1 teste.\n")         
print("Linha 2 teste.\n")   

for value in range(1,6): 
    print(value)

even_numbers = list(range(2,11,3)) #os parâmetro de range são número inicial da lista que é considerado, final que não faz parte da lista, e o fator multiplicador que neste exemplo é 3.
print(even_numbers) 
numbers = list(range(1,6))
print(numbers)

squares = [] # criando uma lista de quadrados perfeitos em 4 linhas 
for value in range(1,11): 
     square = value**2     
     squares.append(square)
print(squares) 
squares = [value**2 for value in range(1,11)] # list comprehensions =  serve para por exemplo ,  criar uma lista de quadrados perfeitos em 1 linha 
print(squares)

digits = [1, 2, 3,4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))


#exercícios:
counts20 = []
for count20 in range(1,21):
    counts20.append(count20)
print(counts20 )

milhaoCount = []
for milhao in range(1,1000001):
    milhaoCount.append(milhao)
#print(milhaoCount)
print(min(milhaoCount))
print(max(milhaoCount))
print(sum(milhaoCount))

print(list(range(1,21,2))) # lista de número impares até 10

#4.7– Três: Crie uma lista de múltiplos de 3, de 3 a 30. Use um laço for para exibir os números de sua lista.
multiplo3 = list(range(0,31,3))

multiplo3.remove(0)

for showNumber in multiplo3:
    print(showNumber)


#4.8 – Cubos: Um número elevado à terceira potência é chamado de cubo. Por exemplo, o cubo de 2 é escrito como 2**3 em Python. 
# Crie uma lista dos dez primeiros cubos (isto é, o cubo de cada inteiro de 1 a 10), e utilize um laço for para exibir o valor de cada cubo.

multiplo3 = list(range(1,11))

for showNumber in multiplo3:
    print(showNumber**3)

# 4.9 – Comprehension de cubos: Use uma list comprehension para gerar uma lista dos dez primeiros cubos.

cubo = [cubos**3 for cubos in range(1,11)]
print(cubo)

####################
players = ['charles', 'martina', 'michael','florence', 'eli']
print("Here are the first three players on my team:") 
for player in players[:3]:
    print(player.title()) 

####################


my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] #cria listas independentes 
print("My favorite foods are:") 
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods) 

my_foods.append('cannoli') 
friend_foods.append('ice cream')
print("\nMy favorite foods are:") 
print(my_foods)
print("\nMy friend's favorite foods are:") 
print(friend_foods) 


friend_foods = my_foods # não cria lista independentes
my_foods.append('pasta') 
friend_foods.append('cucumbe')
print("\nMy favorite foods are:") 
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

#Tupla

dimensions = (200, 50,25)
print(dimensions[0]) 
print(dimensions[1]) 
# dimensions[0] = 250 TypeError: 'tuple' object does not support item assignment

for dimension in dimensions:
    print(dimension)


dimensions = (400,27)
print("\nModified dimensions:") 

for dimension in dimensions: 
    print(dimension) 

#Estilizando seu código
# use PEP (Python Enhancement Proposal, ou Proposta de Melhoria de Python)
#linha-padrão de 79 caracteres código
# 72 caracteres por linha de comentãrio
#quatro espaços por nível de indentação
# converta a tecla de tabulação em 4 espaços, e não esqueça de verifica se o arquivo trabalhado já não possue tabulação, e transforme em espaços, pois isso pode gerar problemas difícies de idenfificar.
