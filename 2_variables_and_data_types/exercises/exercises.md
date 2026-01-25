"""
Sección 2: Variables & Data Types
Ejercicios Prácticos

Instrucciones Generales:
- Sigue las convenciones de PEP 8 (snake_case, nombres descriptivos, espaciado)
- Usa nombres de variables que revelen su intención
- Evita números mágicos - usa constantes con nombres descriptivos
- Comenta tu código solo cuando sea necesario (el código debe ser auto-explicativo)
- Piensa en casos extremos y validaciones
- Crea tu archivo 'soluciones.py' con tus respuestas

IMPORTANTE: Mantén consistencia en el idioma (inglés o español) en todos tus ejercicios.
"""

# ============================================
# Ejercicio 1: Información Personal
# ============================================
# Dificultad: Fácil
# Objetivo: Practicar creación de variables con diferentes tipos de datos
# Requisitos de código limpio: nombres descriptivos en snake_case
#
# TODO:
# 1. Crea variables para almacenar tu información personal:
#    - Nombre completo (string)
#    - Edad (int)
#    - Altura en metros (float)
#    - Si estás empleado actualmente (bool)
#    - Tu ciudad actual (string)
# 2. Imprime cada variable con un mensaje descriptivo
#    Ejemplo: "Mi nombre es: Ana García"
# 3. Usa f-strings para formatear la salida
#
# Escribe tu solución en soluciones.py


# ============================================
# Ejercicio 2: Calculadora de Área de Rectángulo
# ============================================
# Dificultad: Fácil
# Objetivo: Trabajar con operaciones matemáticas y conversión de tipos
# Requisitos de código limpio: evitar números mágicos, nombres descriptivos
#
# TODO:
# 1. Solicita al usuario el ancho del rectángulo (puede tener decimales)
# 2. Solicita al usuario el alto del rectángulo (puede tener decimales)
# 3. Calcula el área del rectángulo
# 4. Calcula el perímetro del rectángulo
# 5. Imprime los resultados con 2 decimales de precisión
#
# EXTRA: Asegúrate de convertir los inputs a float
# NOTA: Área = ancho × alto, Perímetro = 2 × (ancho + alto)
#
# Escribe tu solución en soluciones.py


# ============================================
# Ejercicio 3: Conversor de Temperatura
# ============================================
# Dificultad: Fácil-Medio
# Objetivo: Practicar conversión de tipos y uso de constantes
# Requisitos de código limpio: usar constantes para fórmulas, evitar números mágicos
#
# TODO:
# 1. Define constantes para las fórmulas de conversión:
#    - Factor de multiplicación Celsius a Fahrenheit (9/5)
#    - Valor de ajuste para Fahrenheit (32)
# 2. Solicita al usuario una temperatura en Celsius
# 3. Convierte la temperatura a Fahrenheit usando: F = C × (9/5) + 32
# 4. Convierte la temperatura a Kelvin usando: K = C + 273.15
# 5. Imprime las tres temperaturas con mensajes claros
#
# EXTRA: Formatea las salidas con 2 decimales
#
# Escribe tu solución en soluciones.py


# ============================================
# Ejercicio 4: Validación de Edad
# ============================================
# Dificultad: Medio
# Objetivo: Trabajar con constantes, booleanos y validación de datos
# Requisitos de código limpio: constantes en UPPER_CASE, nombres booleanos descriptivos
#
# TODO:
# 1. Define constantes para:
#    - Edad mínima para votar (18)
#    - Edad mínima para licencia de conducir (16)
#    - Edad para ser mayor de edad (18)
# 2. Solicita al usuario su edad
# 3. Crea variables booleanas que determinen si la persona:
#    - Puede votar
#    - Puede conducir
#    - Es mayor de edad
# 4. Imprime el resultado de cada validación con mensajes claros
#    Ejemplo: "¿Puedes votar? True" o "¿Puedes votar? False"
#
# EXTRA: Los nombres de variables booleanas deben ser autodescriptivos
# Sugerencia: puede_votar, puede_conducir, es_mayor_edad
#
# Escribe tu solución en soluciones.py


# ============================================
# Ejercicio 5: Intercambio de Variables (Swap)
# ============================================
# Dificultad: Medio
# Objetivo: Practicar asignación múltiple y manipulación de variables
# Requisitos de código limpio: nombres descriptivos, demostrar antes/después claramente
#
# TODO:
# 1. Crea dos variables con valores diferentes:
#    - primera_variable = 100
#    - segunda_variable = 200
# 2. Imprime los valores originales con un mensaje claro
# 3. Intercambia los valores de las variables usando asignación múltiple de Python
#    (sin usar una variable temporal)
# 4. Imprime los valores después del intercambio
#
# Salida esperada:
#   Antes: primera = 100, segunda = 200
#   Después: primera = 200, segunda = 100
#
# Escribe tu solución en soluciones.py


# ============================================
# Ejercicio 6: Calculadora de Propina
# ============================================
# Dificultad: Medio
# Objetivo: Trabajar con múltiples variables, constantes y cálculos
# Requisitos de código limpio: constantes para porcentajes, nombres descriptivos
#
# TODO:
# 1. Define constantes para los porcentajes de propina:
#    - Servicio excelente: 20% (0.20)
#    - Servicio bueno: 15% (0.15)
#    - Servicio regular: 10% (0.10)
# 2. Solicita al usuario:
#    - El monto total de la cuenta
#    - El nivel de servicio (1=regular, 2=bueno, 3=excelente)
# 3. Calcula la propina según el nivel de servicio
# 4. Calcula el total a pagar (cuenta + propina)
# 5. Imprime:
#    - Monto de la cuenta
#    - Porcentaje de propina aplicado
#    - Monto de la propina
#    - Total a pagar
#
# NOTA: Usa if/elif/else para determinar el porcentaje según el nivel
#
# Escribe tu solución en soluciones.py


# ============================================
# Ejercicio 7: Detector de Tipos de Datos
# ============================================
# Dificultad: Medio-Difícil
# Objetivo: Practicar conversión de tipos y uso de type()
# Requisitos de código limpio: manejo de errores, código robusto
#
# TODO:
# 1. Solicita al usuario que ingrese un valor
# 2. Intenta convertir el valor a diferentes tipos y muestra cuál funciona:
#    - Intenta convertir a int (si falla, captura el error)
#    - Intenta convertir a float (si falla, captura el error)
#    - Siempre se puede mantener como string
# 3. Imprime el tipo original del input (siempre es string)
# 4. Imprime qué conversiones fueron exitosas
# 5. Sugiere el "mejor tipo" para ese valor
#
# Ejemplos de comportamiento:
#   Input: "42" → Puede ser int, float o string. Mejor tipo: int
#   Input: "3.14" → Puede ser float o string. Mejor tipo: float
#   Input: "Hola" → Solo puede ser string. Mejor tipo: string
#
# PISTA: Usa try/except para manejar errores de conversión
# EXTRA: Este ejercicio te prepara para validación de entrada de usuario
#
# Escribe tu solución en soluciones.py


# ============================================
# IMPORTANTE: 
# ============================================
# 1. Crea un archivo llamado 'soluciones.py' en la misma carpeta
# 2. Copia el número de ejercicio como comentario antes de cada solución
# 3. Resuelve cada ejercicio aplicando PEP 8 y Clean Code
# 4. Cuando termines, comparte tu código completo para revisión
# 5. No te preocupes si algo no sale perfecto, ¡estamos aquí para aprender!
#
# ¡Éxito! 🚀
# ============================================