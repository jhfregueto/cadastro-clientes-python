import tkinter as tk
from tkinter import messagebox

clientes = []

def cadastrar_cliente():
    nome = entry_nome.get()
    email = entry_email.get()
    telefone = entry_telefone.get()

    if nome and email and telefone:
        cliente = f"{nome} | {email} | {telefone}"
        clientes.append(cliente)
        messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
        entry_nome.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_telefone.delete(0, tk.END)
    else:
        messagebox.showwarning("Atenção", "Preencha todos os campos.")

def listar_clientes():
    if clientes:
        lista = "\n".join(clientes)
        messagebox.showinfo("Lista de Clientes", lista)
    else:
        messagebox.showinfo("Lista vazia", "Nenhum cliente cadastrado ainda.")

# Janela principal
janela = tk.Tk()
janela.title("Cadastro de Clientes")

# Layout
tk.Label(janela, text="Nome:").grid(row=0, column=0, sticky='e')
entry_nome = tk.Entry(janela, width=40)
entry_nome.grid(row=0, column=1)

tk.Label(janela, text="Email:").grid(row=1, column=0, sticky='e')
entry_email = tk.Entry(janela, width=40)
entry_email.grid(row=1, column=1)

tk.Label(janela, text="Telefone:").grid(row=2, column=0, sticky='e')
entry_telefone = tk.Entry(janela, width=40)
entry_telefone.grid(row=2, column=1)

tk.Button(janela, text="Cadastrar", command=cadastrar_cliente).grid(row=3, column=0, pady=10)
tk.Button(janela, text="Listar Clientes", command=listar_clientes).grid(row=3, column=1)

janela.mainloop()
