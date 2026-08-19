#importando a biblioteca
import tkinter as tk

def mostrar_nome():
    nome= entrada_nome.get()
    resultado.config(
        text=f"olá {nome}"
    )
#cria a janela principal
janela = tk.Tk()

#definir o titulo exibindo na barra superior
janela.title("primeira janela")

#definir o tamanho da janela
janela.geometry("500x300")

#mudar cor de fundo
janela.config(bg='pink')

#criar um texto dentro da janela
titulo = tk.Label(
    janela,
    text="sistema de locadora",
    font=("arial", 18)
)

tk.Label(
    janela,
    font=("arial", 18, "bold"), bg="black", fg="white",
    text="digite seu nome: "
).pack(pady=10)

#def mensagem():
 #  print("botão clicado")

#adicionando um botão
#botao = tk.Button(
#    janela,
#    text="clique aqui",
 #   command=mensagem
#)

#campo de entrada
entrada_nome = tk.Entry(
    janela,
    width=40
)
entrada_nome.pack()

tk.Button(
    janela,
    text="cofirmar",
    command=mostrar_nome,
    bg="red"
).pack(pady=15)

resultado = tk.Label(
    janela,
    text="",
)

resultado.pack()

#exibe o componente na janela
#titulo.pack(pady=30)
#botao.pack(pady=20)
entrada_nome.pack()

#mantem a janela aberta
janela.mainloop()