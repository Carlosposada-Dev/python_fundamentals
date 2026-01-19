# Sección 2: Variables & Data Types - Resumen

## 🎯 Conceptos Clave

- **Variable**: Nombre que apunta a un valor en memoria
- **Tipado dinámico**: No necesitas declarar tipos, Python los infiere automáticamente
- **5 tipos básicos**: `int`, `float`, `str`, `bool`, `None`
- **Conversión de tipos**: `int()`, `float()`, `str()` para convertir entre tipos
- **Verificación de tipo**: `type()` muestra el tipo de una variable

## 🎨 Buenas Prácticas y Convenciones

### PEP 8 aplicado a variables

```python
# Variables y funciones: snake_case
edad_usuario = 25
altura_metros = 1.77
nombre_completo = "Carlos"

# Constantes: UPPER_SNAKE_CASE
MAX_INTENTOS = 3
PI = 3.14159
EDAD_MINIMA = 18

# Espaciado correcto
x = 5  # ✅ Un espacio antes y después de =
x=5    # ❌ Sin espacios
```

### Clean Code aplicado

**Nombres descriptivos:**
```python
# ❌ Malo
x = 25
n = "Juan"
d = 1.75

# ✅ Bueno
edad_usuario = 25
nombre_completo = "Juan"
altura_metros = 1.75
```

**Evitar números mágicos:**
```python
# ❌ Malo
if edad < 18:
    print("No permitido")

# ✅ Bueno
EDAD_MINIMA = 18
if edad < EDAD_MINIMA:
    print("No permitido")
```

## 💡 Puntos Importantes a Recordar

- **Una variable, un propósito**: No reutilices variables para cosas diferentes
- **Consistencia en el idioma**: Elige inglés o español, no mezcles
- **F-strings para formateo**: `f"Edad: {edad}"` es más legible
- **Validación de entrada**: Siempre convierte y valida datos del usuario
- **Try-except específico**: Captura errores concretos, no uses `except:` vacío

## ⚠️ Errores Comunes a Evitar

### Funcionales
```python
# ❌ Variable no definida
print(nombre)  # NameError

# ❌ Mezclar tipos incompatibles
edad = "25"
resultado = edad + 5  # TypeError

# ❌ Try-except incorrecto
except:
    variable: None  # ':' no asigna, usa '='
```

### De estilo
```python
# ❌ Nombres no descriptivos
x = 25  # ¿Qué es x?

# ❌ No usar constantes
if intentos > 3:  # ¿Por qué 3?

# ❌ Inconsistencia
user_edad = 25  # Mezclando inglés/español
```

## 🔗 Conexión con Otros Conceptos

- **Operadores** (siguiente): Manipularás variables con +, -, *, /, %, etc.
- **Strings**: Métodos avanzados para trabajar con texto
- **Condicionales**: Usarás booleanos para tomar decisiones
- **Loops**: Iterarás sobre rangos usando variables de control
- **Funciones**: Variables como parámetros y valores de retorno

## 📝 Vocabulario Técnico

- **Variable**: Nombre que referencia un valor en memoria
- **Tipo de dato**: Clasificación que determina qué operaciones son válidas
- **Casting**: Conversión entre tipos (`int()`, `float()`, `str()`)
- **Tipado dinámico**: El tipo se determina en tiempo de ejecución
- **Constante**: Variable cuyo valor no debería cambiar (convención)
- **snake_case**: Convención de nombres con guiones bajos
- **Número mágico**: Valor hardcodeado sin contexto

## ✅ Checklist de Dominio

- [x] Creo variables con diferentes tipos de datos
- [x] Entiendo qué es el tipado dinámico
- [x] Uso `type()` para verificar tipos
- [x] Convierto entre tipos correctamente
- [x] Nombro variables en snake_case
- [x] Uso constantes en UPPER_SNAKE_CASE
- [x] Evito números mágicos
- [x] Escribo código con nombres descriptivos
- [x] Manejo errores con try-except específico
