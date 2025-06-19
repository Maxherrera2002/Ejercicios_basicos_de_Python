import random
import string

def sumar(a, b):
    return a + b

def mayor(a, b):
    return a if a > b else b

def es_par(n):
    return n % 2 == 0

def area_triangulo(base, altura):
    return (base * altura) / 2

def contar_letras(cadena):
    return len(cadena.replace(" ", ""))

def revertir(texto):
    return texto[::-1]

def a_fahrenheit(celsius):
    return celsius * 9/5 + 32

def saludar(nombre):
    return f"Hola, {nombre}!"

def tabla_multiplicar(n):
    return [n * i for i in range(1, 11)]

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def contar_vocales(cadena):
    return sum(1 for c in cadena.lower() if c in 'aeiou')

def es_palindromo(palabra):
    palabra = palabra.lower().replace(" ", "")
    return palabra == palabra[::-1]

def maximo(lista):
    return max(lista)

def es_perfecto(n):
    return sum(i for i in range(1, n) if n % i == 0) == n

def fibonacci(n):
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq[:n]

def contar_palabras(frase):
    return len(frase.split())

def sin_duplicados(lista):
    return list(set(lista))

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for _ in range(longitud))

def calculadora(a, b, operacion):
    if operacion == '+':
        return a + b
    elif operacion == '-':
        return a - b
    elif operacion == '*':
        return a * b
    elif operacion == '/':
        return a / b if b != 0 else "Error: División por cero"
    else:
        return "Operación no válida"
