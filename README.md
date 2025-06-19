# Ejercicios_basicos_de_Python

Ejercicio 1: Crear una función `sumar(a, b)` que retorne la suma de dos números.

Ejercicio 2: Crear una función `mayor(a, b)` que retorne el número mayor entre dos.

Ejercicio 3: Crear una función `es_par(n)` que retorne True si el número es par, False en caso contrario.

Ejercicio 4: Crear una función `area_triangulo(base, altura)` que retorne el área de un triángulo.

Ejercicio 5: Crear una función `contar_letras(cadena)` que cuente cuántas letras tiene una cadena, sin contar los espacios.

Ejercicio 6: Crear una función `revertir(texto)` que retorne el texto dado al revés.

Ejercicio 7: Crear una función `a_fahrenheit(celsius)` que convierta grados Celsius a Fahrenheit.

Ejercicio 8: Crear una función `saludar(nombre)` que retorne "Hola, [nombre]!".

Ejercicio 9: Crear una función `tabla_multiplicar(n)` que retorne una lista con la tabla de multiplicar del número n (hasta el 10).

Ejercicio 10: Crear una función `factorial(n)` que retorne el factorial del número dado.

Ejercicio 11: Crear una función `es_primo(n)` que indique si el número es primo.

Ejercicio 12: Crear una función `contar_vocales(cadena)` que cuente cuántas vocales hay en la cadena.

Ejercicio 13: Crear una función `es_palindromo(palabra)` que indique si la palabra se lee igual al revés.

Ejercicio 14: Crear una función `maximo(lista)` que retorne el valor máximo de una lista.

Ejercicio 15: Crear una función `es_perfecto(n)` que indique si un número es perfecto (la suma de sus divisores propios es igual a sí mismo).

Ejercicio 16: Crear una función `fibonacci(n)` que retorne una lista con los n primeros términos de la secuencia de Fibonacci.

Ejercicio 17: Crear una función `contar_palabras(frase)` que retorne la cantidad de palabras en una frase.

Ejercicio 18: Crear una función `sin_duplicados(lista)` que retorne una lista sin elementos duplicados.

Ejercicio 19: Crear una función `generar_contrasena(longitud)` que genere una contraseña aleatoria de la longitud especificada, con letras y números.

Ejercicio 20: Crear una función `calculadora(a, b, operacion)` que realice operaciones básicas (+, -, *, /).

---

## 📂 Archivos

- `Ejercicios/EjercicioN`: Carperta ejercicios contiene un archivo .py para cada ejercicio.
- `test_funciones.py`: contiene los tests que verifican el funcionamiento de cada función.

---

## 🧪 Cómo testear

1. Ejecutá `test_funciones.py` con Python.
2. Observá en consola si los tests pasan (✅) o fallan (❌).
3. Si un test falla, revisá la función correspondiente en `Funciones.py`.

---

## ✅ Ejemplo de testeo

```
Test contar_vocales(Hola Mundo) => Esperado: 4, Resultado: 4 ✅
```

Este test indica que la función recibió correctamente la entrada `"Hola Mundo"` y retornó 4 vocales, como se esperaba.

---

## 📋 Lista de funciones y ejemplos

| Función                          | Ejemplo                                |
|----------------------------------|----------------------------------------|
| `sumar(a, b)`                    | `sumar(2, 3)` → 5                      |
| `mayor(a, b)`                    | `mayor(4, 7)` → 7                      |
| `es_par(n)`                      | `es_par(6)` → True                     |
| `area_triangulo(base, altura)`   | `area_triangulo(5, 4)` → 10.0          |
| `contar_letras(cadena)`          | `contar_letras("hola mundo")` → 9      |
| `revertir(texto)`                | `revertir("python")` → "nohtyp"        |
| `a_fahrenheit(celsius)`          | `a_fahrenheit(0)` → 32.0               |
| `saludar(nombre)`                | `saludar("Ana")` → "Hola, Ana!"        |
| `tabla_multiplicar(n)`           | `tabla_multiplicar(3)` → [3,6,...,30]  |
| `factorial(n)`                   | `factorial(5)` → 120                   |
| `es_primo(n)`                    | `es_primo(7)` → True                   |
| `contar_vocales(cadena)`         | `contar_vocales("Hola Mundo")` → 4     |
| `es_palindromo(palabra)`         | `es_palindromo("reconocer")` → True    |
| `maximo(lista)`                  | `maximo([1, 5, 3])` → 5                |
| `es_perfecto(n)`                 | `es_perfecto(6)` → True                |
| `fibonacci(n)`                   | `fibonacci(5)` → [0,1,1,2,3]           |
| `contar_palabras(frase)`         | `contar_palabras("hola que tal")` → 3  |
| `sin_duplicados(lista)`          | `sin_duplicados([1,2,2,3])` → [1,2,3]   |
| `generar_contrasena(longitud)`   | `generar_contrasena(8)` → "a8Tz92Lp"   |
| `calculadora(a, b, operacion)`   | `calculadora(5, 3, "+")` → 8           |

---

> 📎 Recordá: los resultados pueden variar si usás funciones aleatorias como `generar_contrasena`.

