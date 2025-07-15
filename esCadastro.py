from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from esBancoListas import *
from esLogin import LoginTela

def janelaCadastro():
    global entradaCaIdade
    global entradaCaMail
    global entradaCaNo
    global entradaCaSen
    global entradaCaTel
    
    cadasTel = Tk()

    icone = ImageTk.PhotoImage(file='icone.jpeg')
    imgCadastro = ImageTk.PhotoImage(file='telCadastro.png')
    imgBotaoCadastro2 = ImageTk.PhotoImage(file='cadasBotao2.png')
    icone = ImageTk.PhotoImage(file='icone.jpeg')
    
    cadasTel.iconphoto(True, icone)
    cadasTel.geometry("600x800")
    cadasTel.resizable(False, False)
    cadasTel.title("Cadastro")
    cadasTel.config(background="black")
       
    fundo = Label(cadasTel, image=imgCadastro)
    
    entradaCaMail = Entry()
    entradaCaMail.config(font=('Arial', 24),
                  width=29)
    entradaCaMail.place(x=37, y=175)
    
    entradaCaNo = Entry()
    entradaCaNo.config(font=('Arial', 24),
                  width=29)
    entradaCaNo.place(x=37, y=310)
    
    entradaCaTel = Entry()
    entradaCaTel.config(font=('Arial', 24),
                  width=29)
    entradaCaTel.place(x=37, y=445)
    
    entradaCaSen = Entry()
    entradaCaSen.config(font=('Arial', 24),
                  width=29)
    entradaCaSen.place(x=37, y=580)
    
    entradaCaIdade = Entry()
    entradaCaIdade.config(font=('Arial', 24),
                  width=10)
    entradaCaIdade.place(x=150, y=654)
    
    def voltaTel():
        cadasTel.destroy()
        LoginTela()
        
    def compCadastro():
            if entradaCaMail.get().count("") < 10 or '@gmail' not in entradaCaMail.get():
                    messagebox.showerror(title='Error de Cadastro', message='Email inválido')
            elif entradaCaSen.get().count("") < 10:
                    messagebox.showerror(title='Error de Cadastro', message='Senha muito pequena, mínimo 10 caracteres')
            elif entradaCaNo.get().count("") < 10: 
                    messagebox.showerror(title='Error de Cadastro', message='Nome muito pequeno, coloque o nome completo')
            elif entradaCaTel.get().count("") != 12:
                    messagebox.showerror(title='Error de Cadastro', message='Número de celular não existe, coloque o código de área')
            elif entradaCaIdade.get().count("") > 3:
                    messagebox.showerror(title='Error de Cadastro', message='Idade inválida')
            else:
                senhacadastro.append(entradaCaSen.get())
                emailcadastro.append(entradaCaMail.get())
                telcadastro.append(entradaCaTel.get())
                nomecadastro.append(entradaCaNo.get())
                idadecadastro.append(entradaCaIdade.get())
                criarID()
                cadasTel.destroy()
                LoginTela()
                
    def clicarCadas():
        if entradaCaMail.get() in emailcadastro:
            messagebox.showerror(title='Error de Cadastro', message='Email já cadastrado')
        elif entradaCaTel.get() in telcadastro:
            messagebox.showerror(title='Error de cadastro', message='Telefone já cadastro')
        else:
                compCadastro()
            
    botaoCadastro = Button(cadasTel)
    botaoCadastro.config(command=clicarCadas,
                     image=imgBotaoCadastro2,
                     state=ACTIVE)
    botaoCadastro.place(x=27, y=720)
    
    botaoVolta = Button(cadasTel)
    botaoVolta.config(command=voltaTel,
                      text='Voltar',
                     state=ACTIVE)
    botaoVolta.place(x=2, y=2)

    fundo.pack()
    cadasTel.mainloop()

