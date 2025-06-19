# Ejercicios_basicos_de_Python

Este proyecto contiene una serie de ejercicios diseñados para practicar el uso de funciones en Python.  
Las consignas están en el archivo `Funciones.py`, donde deberás implementar cada función.

---

## 📂 Archivos

- `Funciones.py`: contiene las 20 funciones a implementar.
- `test_funciones.py`: contiene los tests que verifican el funcionamiento de cada función.
- `GEjercicios_Funciones.pdf`: documento con todas las consignas y ejemplos de uso.

---

## 🧪 Cómo testear

1. Asegurate de que ambos archivos (`Funciones.py` y `test_funciones.py`) estén en el mismo directorio.
2. Ejecutá `test_funciones.py` con Python.
3. Observá en consola si los tests pasan (✅) o fallan (❌).
4. Si un test falla, revisá la función correspondiente en `Funciones.py`.

---

## ✅ Ejemplo de testeo

```
Test contar_vocales(Hola Mundo) => Esperado: 4, Resultado: 4 ✅
```

Este test indica que la función recibió correctamente la entrada `"Hola Mundo"` y retornó 4 vocales, como se esperaba.

---

## 🔍 Observaciones importantes

- La función `sin_duplicados` usa `set()` por defecto, lo que puede alterar el orden. Para mantener el orden, se puede usar:
  ```python
  def sin_duplicados(lista):
      return list(dict.fromkeys(lista))
  ```
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

