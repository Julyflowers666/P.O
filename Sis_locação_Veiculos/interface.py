import tkinter as tk
from tkinter import messagebox
from cliente import Cliente

cliente = []

def cadastrar_cliente():
    nome = entrada_nome.get()
    cpf = entrada_cpf.get()

    if nome.strip():
        messagebox.showerror(
            "Error",
            "informe o nome cliente"
        )
        return

    if cpf.strip() == "":
        messagebox.showerror(
            "erro",
            "informe o CPF"
        )
        return

    codigo = len (cliente) + 1

    cliente = Cliente(
        codigo,
        nome,
        cpf
    )

    cliente.append(cliente)

    messagebox.showinfo(
        "cadastro",
        f"cliente {cliente.get_nome()} cadastrado!"
    )

    entrada_nome.delete(0,tk.END)
    entrada_cpf.delete(0,tk.END)

janela = tk.Tk()
janela.title("sistema de locação de veiculos")
janela.geometry("800x500")

titulo = tk.Label(
    janela,text="Cadasto do cliente",
    font=("Arial", 18)
)

titulo.pack(pady=20)

tk.Label(
    janela,
    text="nome: "
).pack()

entrada_nome= tk.Entry(
    janela,
    width=40
)

entrada_nome.pack(
    pady=5
)

tk.Label(
    janela,
    text='cpf: '
).pack()

entrada_cpf = tk.Entry(
    janela,
    width=40
)

entrada_cpf.pack(
    pady=5
)

botao_cadastrar = tk.Button(
    janela,
    text="Cadastar Cliente",
    command=cadastrar_cliente,
    width=25
)

botao_cadastrar.pack(pady=20)

botao_sair = tk.Button(
    janela,
    text="sair",
    command=janela.destroy,
    width=25
)

botao_sair.pack(pady=5)

janela.mainloop()