# Sección 2: Variables & Data Types

## 🎯 ¿Qué son las Variables?

Una **variable** es un contenedor que almacena datos en la memoria de tu computadora. Piensa en ella como una caja etiquetada donde guardas información que necesitarás usar más tarde.

En Python, crear una variable es tan simple como darle un nombre y asignarle un valor:

```python
edad = 25
nombre = "Ana"
temperatura = 36.5
esta_activo = True
```

### Características importantes de las variables en Python:

1. **Tipado dinámico**: No necesitas declarar el tipo de dato explícitamente. Python lo infiere automáticamente.
2. **Reasignables**: Puedes cambiar el valor (y hasta el tipo) de una variable cuando quieras.
3. **Case-sensitive**: `edad`, `Edad` y `EDAD` son tres variables diferentes.

## 📊 Tipos de Datos Básicos en Python

Python tiene varios tipos de datos fundamentales. Aquí están los más importantes para comenzar:

### 1. **Enteros (int)** - Números sin decimales

```python
edad_usuario = 25
anio_actual = 2025
temperatura_celsius = -5
```

### 2. **Flotantes (float)** - Números con decimales

```python
altura_metros = 1.75
precio_producto = 49.99
pi = 3.14159
```

### 3. **Cadenas de texto (str)** - Texto entre comillas

```python
nombre_completo = "María García"
ciudad = 'Bogotá'
mensaje = """Este es un texto
que ocupa varias líneas"""
```

**Nota**: Puedes usar comillas simples `' '` o dobles `" "`, pero es convención usar dobles para strings normales.

### 4. **Booleanos (bool)** - Valores de verdad

```python
esta_logueado = True
es_mayor_edad = False
tiene_descuento = True
```

**Importante**: `True` y `False` van con mayúscula inicial en Python.

### 5. **NoneType** - Ausencia de valor

```python
resultado = None  # Aún no tiene valor asignado
usuario_actual = None  # No hay usuario logueado
```

## 🔍 Verificar el tipo de una variable

Usa la función `type()` para saber qué tipo de dato es una variable:

```python
edad = 30
print(type(edad))  # <class 'int'>

precio = 99.99
print(type(precio))  # <class 'float'>

nombre = "Python"
print(type(nombre))  # <class 'str'>
```

## 🔄 Conversión de Tipos (Type Casting)

A veces necesitas convertir un tipo de dato a otro:

```python
# String a entero
edad_texto = "25"
edad_numero = int(edad_texto)  # 25 (int)

# Entero a string
puntos = 100
mensaje = "Tienes " + str(puntos) + " puntos"

# String a float
precio_texto = "49.99"
precio_numero = float(precio_texto)  # 49.99 (float)

# Float a int (pierde los decimales)
promedio = 8.7
promedio_entero = int(promedio)  # 8 (trunca, no redondea)
```

## 🎨 Buenas Prácticas con Variables

### ✅ Nombres Descriptivos (PEP 8)

Los nombres de variables deben revelar su intención. Cualquier persona que lea tu código debe entender qué contiene la variable sin necesidad de comentarios.

**❌ Malo:**
```python
x = 25
n = "Juan"
d = 1.75
t = True
p = 49.99
```

**✅ Bueno:**
```python
edad_usuario = 25
nombre_completo = "Juan"
altura_metros = 1.75
esta_activo = True
precio_producto = 49.99
```

### ✅ Convención de Nombres en Python (snake_case)

Python usa **snake_case** para variables y funciones: palabras en minúscula separadas por guiones bajos.

```python
# Variables normales: snake_case
nombre_completo = "Ana López"
edad_actual = 30
total_productos = 5
temperatura_promedio = 22.5

# Constantes: UPPER_SNAKE_CASE
PI = 3.14159
MAX_INTENTOS = 3
EDAD_MINIMA = 18
URL_BASE = "https://api.example.com"

# Nombres de una palabra: sin guiones
edad = 25
nombre = "Pedro"
precio = 99.99
```

### ✅ Evitar Números Mágicos

Un "número mágico" es un valor hardcodeado sin contexto. Usa constantes con nombres descriptivos.

**❌ Malo:**
```python
if edad < 18:
    print("No puedes registrarte")

precio_final = precio * 0.19
```

**✅ Bueno:**
```python
EDAD_MINIMA_REGISTRO = 18
if edad < EDAD_MINIMA_REGISTRO:
    print("No puedes registrarte")

IVA = 0.19
precio_final = precio * IVA
```

### ✅ Una Variable, Un Propósito

Evita reutilizar variables para propósitos diferentes. Crea una nueva variable con un nombre descriptivo.

**❌ Malo:**
```python
dato = input("Nombre: ")
print(f"Hola {dato}")
dato = int(input("Edad: "))  # Reutilizando 'dato' para otra cosa
print(f"Tienes {dato} años")
```

**✅ Bueno:**
```python
nombre = input("Nombre: ")
print(f"Hola {nombre}")
edad = int(input("Edad: "))
print(f"Tienes {edad} años")
```

### ✅ Nombres en Inglés vs Español

**Recomendación**: Elige un idioma y mantén consistencia en todo tu proyecto.

- **Inglés**: Estándar en la industria, facilita colaboración internacional
- **Español**: Válido para proyectos locales o educativos

```python
# Opción 1: Todo en inglés
user_age = 25
product_price = 49.99

# Opción 2: Todo en español
edad_usuario = 25
precio_producto = 49.99

# ❌ NO MEZCLAR
user_edad = 25  # Inconsistente
precio_product = 49.99  # Inconsistente
```

## 💡 Conceptos Importantes

### Asignación Múltiple

Python permite asignar valores a múltiples variables en una línea:

```python
# Asignar diferentes valores
nombre, edad, ciudad = "Ana", 28, "Medellín"

# Asignar el mismo valor
x = y = z = 0

# Intercambiar valores (swap)
a = 5
b = 10
a, b = b, a  # Ahora a=10, b=5
```

### Variables y Memoria

Cuando asignas un valor a una variable, Python crea un objeto en memoria y la variable es solo una "etiqueta" que apunta a ese objeto.

```python
edad = 25  # Python crea un objeto int con valor 25
edad = 30  # Python crea un NUEVO objeto int con valor 30
```

### Palabras Reservadas

Python tiene palabras que NO puedes usar como nombres de variables porque tienen significados especiales:

```python
# ❌ NO USAR COMO VARIABLES:
# False, True, None, and, or, not, if, else, elif, 
# for, while, break, continue, def, class, return, etc.

# Esto da error:
for = 10  # SyntaxError
class = "Python"  # SyntaxError
```

## 🎓 Comparación con otros lenguajes

Si vienes de otros lenguajes, aquí algunas diferencias clave:

| Aspecto | Java/C++ | Python |
|---------|----------|--------|
| Declaración | `int edad = 25;` | `edad = 25` |
| Tipado | Estático | Dinámico |
| Punto y coma | Requerido `;` | No se usa |
| Constantes | `final int MAX = 10;` | `MAX = 10` (convención) |

## ⚠️ Errores Comunes

### 1. Variables no definidas
```python
print(nombre)  # NameError: name 'nombre' is not defined
# Primero debes asignar: nombre = "Ana"
```

### 2. Mezclar tipos incompatibles
```python
edad = "25"
resultado = edad + 5  # TypeError: can't concatenate str and int
# Solución: resultado = int(edad) + 5
```

### 3. Nombres inválidos
```python
1edad = 25  # SyntaxError: no puede empezar con número
mi-variable = 10  # SyntaxError: el guion se interpreta como resta
mi variable = 5  # SyntaxError: no se permiten espacios
```

### 4. Confundir asignación (=) con comparación (==)
```python
edad = 25  # Asignación: le das el valor 25 a edad
edad == 25  # Comparación: preguntas si edad es igual a 25 (devuelve True/False)
```

## 📝 Ejemplo Completo con Buenas Prácticas

```python
"""
Programa: Calculadora de IMC (Índice de Masa Corporal)
Demuestra el uso correcto de variables y tipos de datos
"""

# Constantes (valores que no cambian)
IMC_BAJO_PESO = 18.5
IMC_PESO_NORMAL = 24.9
IMC_SOBREPESO = 29.9

# Entrada de datos del usuario
nombre_paciente = input("Ingresa tu nombre: ")
peso_kilogramos = float(input("Ingresa tu peso en kg: "))
altura_metros = float(input("Ingresa tu altura en metros: "))

# Cálculo del IMC
indice_masa_corporal = peso_kilogramos / (altura_metros ** 2)

# Determinación de categoría
if indice_masa_corporal < IMC_BAJO_PESO:
    categoria = "Bajo peso"
elif indice_masa_corporal <= IMC_PESO_NORMAL:
    categoria = "Peso normal"
elif indice_masa_corporal <= IMC_SOBREPESO:
    categoria = "Sobrepeso"
else:
    categoria = "Obesidad"

# Mostrar resultados
print(f"\n--- Resultados para {nombre_paciente} ---")
print(f"IMC: {indice_masa_corporal:.2f}")
print(f"Categoría: {categoria}")
```

**Nota lo que hace que este código sea limpio:**
- Nombres descriptivos que revelan intención
- Constantes para valores importantes
- snake_case consistente
- Comentarios que explican secciones, no lo obvio
- Cálculos claros y legibles

## 🔗 Conexión con lo que viene

Las variables y tipos de datos son la base de TODO en programación. En las próximas secciones verás:

- **Operadores**: Cómo manipular y combinar variables
- **Strings**: Métodos avanzados para trabajar con texto
- **Estructuras de datos**: Listas, diccionarios para agrupar variables
- **Funciones**: Cómo organizar tu código usando variables como parámetros

## ✅ Checklist de Dominio

Antes de continuar, asegúrate de poder:

- [ ] Crear variables con diferentes tipos de datos
- [ ] Explicar qué es el tipado dinámico
- [ ] Usar `type()` para verificar tipos de datos
- [ ] Convertir entre tipos (int, float, str)
- [ ] Nombrar variables siguiendo snake_case
- [ ] Identificar y evitar números mágicos
- [ ] Escribir código con nombres descriptivos

---

**¡Ahora es tu turno!** 🎤

Antes de pasar a los ejercicios, necesito validar que has comprendido estos conceptos.

Por favor, responde estas preguntas con tus propias palabras:

1. **¿Qué es una variable y por qué es importante usar nombres descriptivos?**
2. **¿Cuál es la diferencia entre `int`, `float` y `str`? Dame un ejemplo de cuándo usarías cada uno.**
3. **¿Qué significa que Python tenga "tipado dinámico"? ¿En qué se diferencia de Java o C++?**
4. **¿Qué es un "número mágico" y por qué debemos evitarlos?**

Tómate tu tiempo para pensar y responder. No hay prisa, lo importante es que entiendas bien estos fundamentos. 😊