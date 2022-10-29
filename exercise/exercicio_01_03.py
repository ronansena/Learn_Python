number = 2**3 # operador de exponencial **
print(str(number) + " --> operador de exponencial **")
number = 7%3   # operador de módulo %, sendo que em outra linguages costuma ser ^
print(str(number) + " --> operador de módulo %")
name = "ronan pereira de sena"
print("testes ,\n" + name.title())
print("Languages:\nPython\nC\nJavaScript") 
print("Languages:\n\tPython\n\tC\n\tJavaScript")
favorite_language = 'python '
print(favorite_language)
print(favorite_language.rstrip())
if favorite_language.strip() == favorite_language.rstrip():
    print("igual")
else:    
    print("diferente")

message =  "One of Python's strengths is its diverse community."
print(message)
print(round(0.2523 + 0.1,3))
age=23
message = "Happy " + str(age) + "rd Birthday!"
print(message)
# import this
bicycles = ['trek','cannondale', 'redline', 'specialized','magura','sense','adapt'] # cria um lista 
bicycles[2] = 'mongoosee'
bikeVal = "trek"
bicycles.append("caloi") # inseri o item da lista na última posição
bicycles.insert(0,"monark") # inseri o item da lista na posição indicada
del bicycles[5] # remove o item da lista na posição indicada
lastBicycles = bicycles.pop(4) # remove o item da lista na posição indicada
bicycles.reverse() # não reorganiza em ordem alfabética inversa; ele simplesmente inverte a ordem da lista, e altera a lista de forma permanente
print("Lista 1: " + str(bicycles)) 
bicycles.remove(bikeVal)  #remove o item da lista de acordo com a string informada NOTA O método remove() apaga apenas a primeira ocorrência do valor que
#você especificar. Se houver a possibilidade de o valor aparecer mais de uma vez na lista, será necessário usar um laço para determinar se todas as ocorrências desse valor foram removidas. Aprenderemos a fazer isso no Capítulo 7
print("Lista 2: " + str(sorted(bicycles,reverse=True))) # ordena a lista de forma temporária com a possibilidade de passar um parâmetro de ordenação em ordem inversa
lastBicycles = bicycles.pop() # remove o item da lista na última posição 
print("Lista 3: " + str(bicycles))
bicycles.sort()#ordena a lista definitivamente em ordem crescente
print("Lista 4: " + str(bicycles))
bicycles.sort(reverse=True) #ordena a lista definitivamente em ordem decrescente
print("Lista 5: " + str(bicycles))
print(lastBicycles)
print(len(bicycles))
print(bicycles[-1]) #Tenha em mente que, sempre que quiser acessar o último item de uma lista, você deve usar o índice -1. Isso sempre funcionará, mesmo que sua lista tenha mudado de tamanho desde a última vez que você a acessou
#A única ocasião em que essa abordagem causará um erro é quando solicitamos o último item de uma lista vazia

