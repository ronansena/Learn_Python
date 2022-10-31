import sys

for i in range(1, len(sys.argv)):
    
    codigoProduto=sys.argv[1]
    idProduto=sys.argv[2]
    idCategoriaDespesa=sys.argv[3]
    idSubCategoriaDespesa=sys.argv[4]
    optionPrecoProduto=sys.argv[5]
    db=sys.argv[6]
    

print(codigoProduto)
print(idProduto)
print(idCategoriaDespesa)
print(idSubCategoriaDespesa)
print(optionPrecoProduto)
print(db)
