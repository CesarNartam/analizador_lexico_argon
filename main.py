import ply.lex as lex
from tkinter import *
import analisis as ana

ventana = Tk()
ventana.title("Analizador Léxico")
ventana.geometry("700x600")
ventana.resizable(False, False)

entrada = StringVar()

f = Frame()
f.pack()
f.config(width="680", height="580")
f.place(x=10, y=10)

l1 = Label(f, width="20", height="1", fg="black", font=("Arial", 20), text="Analizador léxico de Argon")
l1.place(x=80, y=1)

l2 = Label(f, width=20, height=1, text="Código a analizar:",font=("Arial", 12))
l2.grid(sticky="w")
l2.place(x=20, y=70)

input_codigo = Text(f, width="56", height="7", font=("Arial", 12))
input_codigo.place(x=20, y=100)
scrollinput_codigo = Scrollbar(f, command=input_codigo.yview)
scrollinput_codigo.grid(sticky="nsew")
scrollinput_codigo.place(in_=input_codigo, relx=1, relheight=1, bordermode="outside")
input_codigo.config(yscrollcommand=scrollinput_codigo.set)

l3 = Label(f, width=10, height=1, text="Resultados:", font=("Arial", 12))
l3.grid(sticky="e")
l3.place(x=20, y=270)

output_codigo = Text(f, width="56", height="9", font=("Arial", 12))
output_codigo.place(x=20, y=300)
scrolloutput_codigo = Scrollbar(f, command=input_codigo.yview)
scrolloutput_codigo.grid(sticky="nsew")
scrolloutput_codigo.place(in_=output_codigo, relx=1, relheight=1, bordermode="outside")
output_codigo.config(yscrollcommand=scrolloutput_codigo.set)
output_codigo.config(state="normal")

def analizar():
    entrada = input_codigo.get("1.0", "end-1c")
    print(entrada)
    output_codigo.delete("1.0", "end")

    ana.a.clear()
    ana.analisis(entrada)

    print(ana.a)
    for output in ana.a:
        output_codigo.insert(INSERT, output + "\n")

button = Button(f, text="Analizar", font=("Arial Black", 10), bg='blue', fg='white', command=analizar)
button.place(x=280, y=530, width=100, height=30)

ventana.mainloop()