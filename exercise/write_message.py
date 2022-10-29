filename = 'text_files/programming.txt'

with open(filename, 'a') as file_object: 
    file_object.write("I love love love programming.") 


#Podemos abrir um arquivo em modo de leitura ('r'), em modo de
#escrita ('w'), em modo de concatenação ('a') ou em um modo que permita ler
#e escrever no arquivo ('r+').

#NOTA Python escreve apenas strings em um arquivo-texto. Se quiser
#armazenar dados numéricos em um arquivo-texto, será necessário
#converter os dados em um formato de string antes usando a função
#str()


with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n") 
    file_object.write("I love creating new games.\n") 


with open(filename, 'a') as file_object: 
    file_object.write("I also love finding meaning in large datasets.\n") 
    file_object.write("I love creating apps that can run in a browser.\n") 