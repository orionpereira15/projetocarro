from carro import Carro
from trem import Trem
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

"""Função de criação de objeto"""
lista=[]
def cadastraVeiculo():
    marca=entryMarca.get()
    modelo=entryModelo.get()
    ano=entryAno.get()
    tipo=varTipo.get()
    portas=entryNportas.get()
   # print(modelo)
    erro=0

    if tipo=="Carro":
        if modelo=="":
            messagebox.showerror("Erro", "Deve ser preenchido o nome do modelo!")
            erro=1
        if marca=="":
            messagebox.showerror("Erro", "Deve ser preenchido a marca do carro!")
            erro=1
        
        if ano=="":
            messagebox.showerror("Erro", "Deve ser preenchido o ano do carro!")
            erro=1
        
        if portas=="":
            messagebox.showerror("Erro", "Deve ser preenchido o número de portas do carro!")
            erro=1
        
        if erro==0:
            c=Carro(marca, modelo, ano, portas)
            salvar(c)
            messagebox.showinfo("Cadastro", f"{tipo} cadastrado com sucesso")
    
    else:
        if tipo=="Trem":
            if modelo=="":
                messagebox.showerror("Erro", "Deve ser preenchido o modelo do trem!")
                erro=1
            if marca=="":
                messagebox.showerror("Erro", "Deve ser preenchido a marca do trem!")
                erro=1
        
            if ano=="":
                messagebox.showerror("Erro", "Deve ser preenchido o ano do trem!")
                erro=1
        
            if portas=="":
                messagebox.showerror("Erro", "Deve ser preenchido o números de vagões do trem!")
                erro=1
        
            if erro==0:
                t=Trem(marca, modelo, ano, portas)
                salvar(t)
                messagebox.showinfo("Cadastro", f"{tipo} cadastrado com sucesso")
    
def salvar(obj):
    lista.append(obj)

def atualizaListabox():
    listbox.delete(0,tk.END)
    for obj in lista:
        listbox.insert(tk.END, obj.mostrar())


janela = tk.Tk()
janela.title("Cadastro de veículos")
janela.geometry("500x300")

janela.grid_rowconfigure(0,weight=1)
janela.grid_columnconfigure(0,weight=1)

janelinha = ttk.Notebook(janela)
janelinha.grid(row=0, column=0, sticky="nsew")

tab1 = ttk.Frame(janelinha)
for i in range(6):
    tab1.grid_rowconfigure(i, weight=1)
tab1.grid_columnconfigure(0, weight=1)
tab1.grid_columnconfigure(1, weight=1)

tab2=ttk.Frame(janelinha)
tab2.grid_rowconfigure(0,weight=1)
tab2.grid_columnconfigure(0, weight=1)

janelinha.add(tab1,text="Cadastro")
janelinha.add(tab2,text="Lista")

label1=tk.Label(tab1, text="Marca:", font=("",15))
label1.grid(row=0, column=0, sticky="w", padx=15)

entryMarca=tk.Entry(tab1, font=("", 15))
entryMarca.grid(row=0,column=1, sticky="nsew", padx=10, pady=5)

label2=tk.Label(tab1, text="Modelo:", font=("",15))
label2.grid(row=1, column=0, sticky="w", padx=15)

entryModelo=tk.Entry(tab1, font=("", 15))
entryModelo.grid(row=1,column=1, sticky="nsew", padx=10,  pady=5)

label3=tk.Label(tab1, text="Ano:", font=("",15))
label3.grid(row=2, column=0, sticky="w", padx=15)

entryAno=tk.Entry(tab1, font=("", 15))
entryAno.grid(row=2,column=1, sticky="nsew", padx=10, pady=5)

label4=tk.Label(tab1, text="N Portas/Vagoes:", font=("",15))
label4.grid(row=3, column=0, sticky="w", padx=15)

entryNportas=tk.Entry(tab1, font=("", 15))
entryNportas.grid(row=3, column=1, sticky="nsew", padx=10, pady=5)

tk.Label(tab1, text="Tipo", font=("",15)).grid(row=4, column=0, sticky="w", padx=10)
varTipo = tk.StringVar(value="Carro")
tk.Radiobutton(tab1, text="Carro", font=("", 15), variable=varTipo, value="Carro").grid(row=4, column=1, sticky="W", padx=10)
tk.Radiobutton(tab1, text="Trem", font=("", 15), variable=varTipo, value="Trem").grid(row=4, column=1, sticky="e", padx=10)

tk.Button(tab1, text="Cadastrar", font=("",15), command=cadastraVeiculo).grid(row=5, columnspan=2)

############################################################
listbox=tk.Listbox(tab2)
listbox.config(font=("",15))
listbox.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
tk.Button(tab2, text="Atulizar", font=("",15), command=atualizaListabox).grid(row=1, column=0)

janela.mainloop()