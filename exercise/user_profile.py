
#Usando argumentos nomeados arbitrários

def build_profile(first, last,**user_info): 
    """Constrói um dicionário contendo tudo que sabemos sobre um usuário."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last 

#atribuir chave e valor passados através dos parâmetros da chamada da função a uma variável do tipo dicionário
    for key, value in user_info.items(): 
        profile[key] = value 
        return profile

user_profile = build_profile('albert', 'einstein', location='princeton',field='physics') 
print(user_profile) 