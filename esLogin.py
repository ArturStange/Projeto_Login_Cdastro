from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from esBancoListas import *
mostrasenha = 0 #variável de mostrar senha
 
def LoginTela():
    
    loginTel = Tk()
    loginTel.geometry("600x800")
    loginTel.resizable(False, False)
    loginTel.title("Login")
    loginTel.config(background="black")
    
    imgLogin = ImageTk.PhotoImage(file='telLoginEd.png')
    imgBotaoEnt = ImageTk.PhotoImage(file='entrarBotao.png')
    imgBotaoCadas=ImageTk.PhotoImage(file='cadastroBotao.png')
    imgRevelSen=ImageTk.PhotoImage(file='revelSen.png')
    icone = ImageTk.PhotoImage(file='icone.jpeg')
    
    loginTel.iconphoto(True, icone)

    fundo = Label(loginTel, image=imgLogin)
    
    def clicarEnt(): #Função do botão de Enter
        if entradaMail.get() in emailcadastro and entradaSen.get() in senhacadastro:
            import esLogado as logadoTel
            loginTel.destroy()
            logadoTel.janelaLogado()
        else:
            messagebox.showerror(title='Error de Login', message='Login ou Senha Incorretos')
            
    def clicarCadas(): #Função do botão do Cadastrar-se
        from esCadastro import janelaCadastro
        loginTel.destroy()
        janelaCadastro()


    def revelSen(): #Função do botão de mostrar senha
        global mostrasenha
        if mostrasenha == 0:
            entradaSen.config(font=('Arial', 24), width=24,show='')
            mostrasenha = 1
            
        elif mostrasenha == 1:
            entradaSen.config(font=('Arial', 24), width=24,show='*')
            mostrasenha= 0
    
    entradaMail = Entry()
    entradaMail.config(font=('Arial', 24),
                    width=29)
    entradaMail.place(x=36, y=270)

    entradaSen = Entry()
    entradaSen.config(font=('Arial', 24),
                    width=24,
                    show= '*')
    entradaSen.place(x=36, y=480)

    botaoMostra = Button(loginTel)
    botaoMostra.config(command=revelSen,
                    image=imgRevelSen,)
    botaoMostra.place(x=510,y=484)

    botaoLogin = Button(loginTel)
    botaoLogin.config(command=clicarEnt,
                    image=imgBotaoEnt, 
                    state=ACTIVE)
    botaoLogin.place(x=26, y=591)

    botaoCadastro = Button(loginTel)
    botaoCadastro.config(command=clicarCadas,
                        image=imgBotaoCadas,
                        state=ACTIVE)
    botaoCadastro.place(x=194, y=736)

    fundo.pack()
    loginTel.mainloop()
