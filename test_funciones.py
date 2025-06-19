"""
Este archivo contiene pruebas (tests) para las funciones definidas en ejercicios_funciones_resueltos.py.
Cada función será probada con 3 casos distintos.
"""

from Funciones import *

def test(funcion, esperado, *args):
    resultado = funcion(*args)
    correcto = resultado == esperado
    print(f"Test {funcion.__name__}({', '.join(map(str, args))}) => Esperado: {esperado}, Resultado: {resultado} {'✅' if correcto else '❌'}")

print("=== TESTS ===\n")

# 3 tests por función
test(sumar, 5, 2, 3)
test(sumar, 0, -1, 1)
test(sumar, -4, -2, -2)

test(mayor, 7, 5, 7)
test(mayor, 10, 10, 3)
test(mayor, 0, -1, 0)

test(es_par, True, 4)
test(es_par, False, 3)
test(es_par, True, 0)

test(area_triangulo, 6.0, 3, 4)
test(area_triangulo, 0.0, 0, 10)
test(area_triangulo, 15.0, 5, 6)

test(contar_letras, 9, "hola mundo")
test(contar_letras, 6, "python")
test(contar_letras, 0, "    ")

test(revertir, "odnum", "mundo")
test(revertir, "ana", "ana")
test(revertir, "", "")

test(a_fahrenheit, 98.6, 37)
test(a_fahrenheit, 32.0, 0)
test(a_fahrenheit, 212.0, 100)

test(saludar, "Hola, Ana!", "Ana")
test(saludar, "Hola, Juan!", "Juan")
test(saludar, "Hola, Mundo!", "Mundo")

test(tabla_multiplicar, [3,6,9,12,15,18,21,24,27,30], 3)
test(tabla_multiplicar, [5,10,15,20,25,30,35,40,45,50], 5)
test(tabla_multiplicar, [0,0,0,0,0,0,0,0,0,0], 0)

test(factorial, 120, 5)
test(factorial, 1, 0)
test(factorial, 6, 3)

test(es_primo, True, 7)
test(es_primo, False, 1)
test(es_primo, False, 10)

test(contar_vocales, 4, "Hola Mundo")
test(contar_vocales, 0, "rhythm")
test(contar_vocales, 10, "aeiouAEIOU")

test(es_palindromo, True, "anita lava la tina")
test(es_palindromo, False, "python")
test(es_palindromo, True, "reconocer")

test(maximo, 9, [1, 9, 3, 2])
test(maximo, 100, [100, 99, 98])
test(maximo, -1, [-5, -10, -1])

test(es_perfecto, True, 28)
test(es_perfecto, True, 6)
test(es_perfecto, False, 10)

test(fibonacci, [0,1,1], 3)
test(fibonacci, [0,1,1,2,3,5,8,13,21,34], 10)
test(fibonacci, [0], 1)

test(contar_palabras, 3, "hola qué tal")
test(contar_palabras, 5, "uno dos tres cuatro cinco")
test(contar_palabras, 0, "")

test(sin_duplicados, [1, 2, 3], [1, 2, 2, 3, 3])
test(sin_duplicados, [4, 5], [4, 4, 5, 5])
test(sin_duplicados, [0], [0, 0, 0])

print(f"Contraseña generada: {generar_contrasena(8)} (verificar longitud)")
print(f"Contraseña generada: {generar_contrasena(12)} (verificar longitud)")
print(f"Contraseña generada: {generar_contrasena(4)} (verificar longitud)")

test(calculadora, 8, 5, 3, '+')
test(calculadora, 2, 5, 3, '-')
test(calculadora, "Error: División por cero", 10, 0, '/')

print("\n=== FIN DE LOS TESTS ===")
