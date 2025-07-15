from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image

def janelaLogado ():
    LogadoTel = Tk()
    imgFundo = ImageTk.PhotoImage(file='agendarTel.png')
    LogadoTel.geometry("600x800")
    LogadoTel.resizable(False, False)
    LogadoTel.title("Logado")
    LogadoTel.config(background="black")
    fundo = Label(LogadoTel, image=imgFundo)
    fundo.pack()
    LogadoTel.mainloop()