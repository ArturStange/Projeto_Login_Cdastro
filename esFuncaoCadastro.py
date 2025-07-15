from esCadastro import *
from tkinter import messagebox

def compCadastro():
    if entradaCaMail.get().count() < 10 or '@' not in entradaCaMail.get():
                    messagebox.showerror(title='Error de Cadastro', message='Email insuficiente')
    elif entradaCaSen.get().count < 10:
                    messagebox.showerror(title='Error de Cadastro', message='Senha muito pequena, mínimo 10 caracteres')
    elif entradaCaNo.get().count < 10: 
                    messagebox.showerror(title='Error de Cadastro', message='Nome muito pequeno, mínimo 10 caracteres')
    elif entradaCaTel.get().count < 11 and entradaCaTel.get().count > 11 :
                    messagebox.showerror(title='Error de Cadastro', message='Número de celular não existe, coloque o código de área')
    elif entradaCaIdade.get().count < 6 and entradaCaIdade.get().count > 6:
                    messagebox.showerror(title='Error de Cadastro', message='Idade inválida, use apenas números')
    else:
                senhacadastro.append(entradaCaSen.get())
                emailcadastro.append(entradaCaMail.get())
                telcadastro.append(entradaCaTel.get())
                nomecadastro.append(entradaCaNo.get())
                idadecadastro.append(entradaCaIdade.get())
                
compCadastro()