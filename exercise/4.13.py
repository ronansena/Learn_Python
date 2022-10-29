#4.13 – Buffet: Um restaurante do tipo buffet oferece apenas cinco tipos básicos
#de comida. Pense em cinco pratos simples e armazene-os em uma tupla.
#• Use um laço for para exibir cada prato oferecido pelo restaurante.
#• Tente modificar um dos itens e cerifique-se de que Python rejeita a mudança.
#• O restaurante muda seu cardápio, substituindo dois dos itens com pratos
#diferentes. Acrescente um bloco de código que reescreva a tupla e, em
#seguida, use um laço for para exibir cada um dos itens do cardápio
#revisado.

#• Use um laço for para exibir cada prato oferecido pelo restaurante.
five_simple_foods = ('arroz','feijao','macarrao','ovo','batata_frita')

for food in five_simple_foods:
    print(food)

#• Tente modificar um dos itens e cerifique-se de que Python rejeita a mudança.
#five_simple_foods[0] = 'quiabo'
#five_simple_foods[1] = 'angu'

#• O restaurante muda seu cardápio, substituindo dois dos itens com pratos
#diferentes. Acrescente um bloco de código que reescreva a tupla e, em
#seguida, use um laço for para exibir cada um dos itens do cardápio
#revisado.

five_simple_foods = ('tomate','pimentao','macarrao','ovo','batata_frita')

print("\n New five foods:")

for food in five_simple_foods:
    print(food)