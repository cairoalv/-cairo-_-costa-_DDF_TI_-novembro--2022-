import subprocess 
import sys
import pandas as pd


def criarUser(): 

    # Recebe o arquivo csv chamado dados e adiciona na tabela df
    df = pd.read_csv('dados.csv')
    
    # A variavel user recebe os valores da coluna users_emails
    user = df['users_emails']

    # Percorre todos os users 
    for nome in user:
        
        # A variavele name recebe o valor do email de cada loop
        name = nome

        # separa a string do email ate o caractere @ para facilizar na geração de senha
        spli = nome.split("@")
        
        # a variavel senha recebe o valor do email antes do @
        senha = spli[0]
            
        # verifica se existe algum erro no loop    
        try: 
            # caso não exista erro realiza a criação do usuario
            subprocess.run(['useradd', '-p', senha, name ])       
        except: 
            # caso tenha erro mostra a seguinte mensagem
            print("Falhar ao criar o usuario")          
            #encerra o sistema            
            sys.exit(1) 
#realiza a inicialização do modulo
criarUser()