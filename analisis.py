import ply.lex as lex
from tkinter import *

tokens = [
    'variable',
    'numero',
    'suma',
    'asignacion',
    'resta',
    'division',
    'multiplicacion', 

    'igual',
    'diferenteque',
    'mayorque',
    'menorque',
    'menorigual',
    'mayorigual',

    'dospuntos',
    'puntocoma',
    'comilladoble',
    'parentesisizq',
    'parentesisder',
    'llaveizq',
    'llaveder',
    'string',

    'masmas',
    'menosmenos',
]

palabras_reservadas = {
    'print': 'palabra_reservada',
    'terminalPrint': 'palabra_reservada',
    'FN': 'palabra_reservada',
    'loop': 'palabra_reservada',
    'assuming': 'palabra_reservada',
    'otherwise': 'palabra_reservada',
}

tokens = list(palabras_reservadas.values()) + tokens

t_ignore = ' '

t_suma = r'\+'
t_asignacion = r'='
t_resta = r'\-'
t_division = r'/'
t_multiplicacion = r'\*'

t_igual = r'=='
t_diferenteque = r'!='
t_mayorque = r'>'
t_menorque = r'<'
t_menorigual = r'<='
t_mayorigual = r'>='

t_dospuntos = r'\:'
t_puntocoma = r'\;'
t_comilladoble = r'"'
t_parentesisizq = r'\('
t_parentesisder = r'\)'
t_llaveizq = r'\{'
t_llaveder = r'\}'
t_string = r'["""][^"""]*["""]'

t_masmas = r'\+\+'
t_menosmenos = r'\-\-'


def t_variable(t):
    r'[a-zA-Z_][a-zA-Z0-9]*'
    t.type = palabras_reservadas.get(t.value, 'variable')
    return t

def t_numero(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_saltolinea(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_whitespace(t):
    r'\s+'
    pass

def t_comentario(t):
    r'\//.*'
    pass

def t_error(t):
    r'.'
    error_output = f"Carácter no reconocido '{t.value[0]}' en la posición {t.lexpos}"
    a.append(error_output)
    t.lexer.skip(1)

a = []

def analisis(input):
    analizador = lex.lex()
    analizador.input(input)
    a.clear()

    while True:
        tok = analizador.token()
        if not tok:
            break
        a.append(str(tok))
    return a

