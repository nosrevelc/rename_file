import os
import sys
import subprocess

cabecalho = '''

|  __ \                                         | |           
| |__) |___ _ __   ___  _ __ ___   ___  __ _  __| | ___  _ __ 
|  _  // _ \ '_ \ / _ \| '_ ` _ \ / _ \/ _` |/ _` |/ _ \| '__|
| | \ \  __/ | | | (_) | | | | | |  __/ (_| | (_| | (_) | |   
|_|  \_\___|_| |_|\___/|_| |_| |_|\___|\__,_|\__,_|\___/|_|   
                                                              
 '''                                                             
print(cabecalho)
#FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')
#path = 'C:/'
#subprocess.run([FILEBROWSER_PATH, path])

def reiniciar_sistema():
    python = sys.executable
    os.execl(python, python, * sys.argv)

caminho = input('Digite o caminho da pasta que deseja trabalhar ou x para nenhum -> ')+'\\'

if caminho == 'x':
    caminho == (".")


lista_tarefas=['Adicionar prefixo','Buscar parte e renomear ou remover','Listar arquivo de diretório', 'renomear tirando _00001']

print('\nLista de tarefas\n')
for index, item in enumerate(lista_tarefas):
    print(index,'-',item)

tarefa=input('\nQual tarefa a executar?\nDigite o número da tarefa :')

def lista_arquivos():
    nom_arq_cami = nome_arquivo
    qtd_carcteres = len(nome_arquivo)
    print(nome_arquivo)

if tarefa == '0':
    prefixo=input('Qual prefixo deseja?')
    
    for nome_arquivo in os.listdir(caminho):
        nom_arq_cami = caminho + nome_arquivo
        novo_nome = caminho + prefixo + nome_arquivo
        os.rename(nom_arq_cami,novo_nome)    
     

if tarefa == '1':
    print(' --- ATENÇÃO A LETRAS MAIUSCULAS E MINUSCULAS --- ')
    for nome_arquivo in os.listdir(caminho):
        lista_arquivos()    
    str_atual=input('O que deseja buscar e renomear?')
    str_novo=input('Renomear para.., ou omitir para remover -> ')
    
    print('O que buscar {}, Mudar para {}'.format(str_atual,str_novo))
    
    for nome_arquivo in os.listdir(caminho):
        nom_arq_cami = caminho + nome_arquivo
        qtd_carcteres = len(nome_arquivo)
        novo_nome =  nom_arq_cami.replace(str_atual,str_novo)  
        os.rename(nom_arq_cami,novo_nome)
    lista_arquivos()

if tarefa == '2':
    print('Lista do diretório{}\n\n'.format(caminho))
    for nome_arquivo in os.listdir(caminho):
        lista_arquivos()

continuar = input('\n\nDeseja reiniciar o sistema? Se sim digite S ->')
continuar.lower()
if continuar == 's':
    reiniciar_sistema()
    
if tarefa == '3':
    str_atual='_00001'
str_novo=''
    
    
for nome_arquivo in os.listdir('.'):
    novo_nome =  nome_arquivo.replace(str_atual,str_novo)  
    os.rename(nome_arquivo,novo_nome)