import ply.lex as lex
from tkinter import *

tokens = [
    'variable',
    'numero',
    'aritmetica',
    'asignacion',

    'comparacion',

    'dospuntos',
    'puntocoma',
    'comilladoble',
    'parentesis',
    'llaves',
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

t_aritmetica = r'\+|\-|\*|\/'
t_asignacion = r'='

t_comparacion = r'> <|>=|<=|==|!='

t_dospuntos = r'\:'
t_puntocoma = r'\;'
t_comilladoble = r'"'
t_parentesis = r'\(|\)'
t_llaves = r'\{|\}'
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

