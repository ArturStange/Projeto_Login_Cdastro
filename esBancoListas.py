import random
import time

li_idmaker = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
              'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','W','V','X','Y','Z',
              '1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','&','¨','*']

li_usuarios=[]
emailcadastro = ['0']
senhacadastro = ['0']
telcadastro = []
nomecadastro = []
idadecadastro = []

def criarID():
    id_usuario = random.sample(li_idmaker, 5) 
    if id_usuario not in li_usuarios:
            li_usuarios.append(id_usuario)
            print(li_usuarios)
            print(emailcadastro, senhacadastro, telcadastro, 
                  nomecadastro, idadecadastro)