from warnings import catch_warnings
import mysql.connector
from re import search
from unidecode import unidecode
from unicodedata import normalize

def rename_campo_banco_mysql(campo1,campo2,tabela,db1):
	
	sqlTbProduto='select '+ campo1 +','+ campo2 +'  from ' +tabela

	try:

		cursorSqlTbProduto= db1.cursor(dictionary=True)

		cursorSqlTbProduto.execute(sqlTbProduto)

		myResultSqlTbProduto = cursorSqlTbProduto.fetchall()	

	except:

		print('Ocorreu erro ao tentar carregar a lista de produto!') 
	
	for nomeProdutoTemp in myResultSqlTbProduto:
		
		nome = nomeProdutoTemp["nomeProduto"]
		idProduto = nomeProdutoTemp["idproduto"]
		
		if(nome.find("#") != -1):  			
		
			print(nome)
		
			nomeProdutoCorrigido = nomeProdutoTemp["nomeProduto"].replace("#","")
		
			print(nomeProdutoCorrigido)

			sqlTbProdutoUpdate='update produto set nomeProduto='+'"'+ nomeProdutoCorrigido +'"'+' where idProduto=' +str(idProduto)

			cursorSqlTbProdutoUpdate= db1.cursor(dictionary=True)

			try:				

				cursorSqlTbProdutoUpdate.execute(sqlTbProdutoUpdate)

				db1.commit()

			except:

  				print('Ocorreu erro ao tentar atualizar o produto idProduto=' +str(idProduto)) 
				
try:
	
	dbControlMoney = mysql.connector.connect(
	
		host="localhost",
		user="usuario",
		passwd="sua_senha",
		database="nome_banco"

	)

except:
		
	print('Ocorreu erro ao tentar conectar com o banco de dados!') 

rename_campo_banco_mysql("nomeProduto","idproduto","produto",dbControlMoney)