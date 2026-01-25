# Sección 3: Operators

## 🎯 ¿Qué son los Operadores?

Los **operadores** son símbolos que le indican a Python qué operaciones realizar con las variables y valores. Son las herramientas que usas para manipular datos, hacer cálculos, comparar valores y tomar decisiones.

En DevOps y Cloud Engineering los usarás constantemente para: calcular recursos, comparar métricas, validar estados, y tomar decisiones automatizadas.

## 🔢 Tipos de Operadores en Python

### 1. **Operadores Aritméticos** - Cálculos matemáticos

```python
# Operaciones básicas
suma = 10 + 5           # 15
resta = 10 - 5          # 5
multiplicacion = 10 * 5  # 50
division = 10 / 5       # 2.0 (siempre devuelve float)

# Operaciones especiales
division_entera = 10 // 3   # 3 (descarta decimales)
modulo = 10 % 3             # 1 (residuo de la división)
potencia = 2 ** 3           # 8 (2 elevado a 3)
```

**Casos de uso en DevOps/Cloud:**
```python
# Calcular uso de CPU
cpu_total = 100
cpu_usado = 75
cpu_disponible = cpu_total - cpu_usado  # 25%

# Calcular costo mensual (730 horas/mes)
HORAS_MES = 730
costo_hora = 0.10
costo_mensual = costo_hora * HORAS_MES  # $73.00

# Distribuir carga entre servidores
total_requests = 1000
servidores = 3
requests_por_servidor = total_requests // servidores  # 333

# Verificar si necesitas instancias adicionales
if total_requests % servidores != 0:
    print("Carga no distribuida uniformemente")
```

### 2. **Operadores de Comparación** - Comparan valores

Devuelven `True` o `False` (booleanos).

```python
# Igualdad y diferencia
5 == 5   # True (igual a)
5 != 3   # True (diferente de)

# Comparaciones
5 > 3    # True (mayor que)
5 < 3    # False (menor que)
5 >= 5   # True (mayor o igual)
5 <= 3   # False (menor o igual)
```

**Casos de uso en DevOps/Cloud:**
```python
# Verificar umbral de CPU
cpu_uso = 85
CPU_MAX = 80
alerta = cpu_uso > CPU_MAX  # True

# Validar disponibilidad
instancias_activas = 2
INSTANCIAS_MINIMAS = 3
necesita_escalar = instancias_activas < INSTANCIAS_MINIMAS  # True

# Verificar puerto estándar
puerto = 8080
es_puerto_http = puerto == 80  # False
es_puerto_https = puerto == 443  # False
```

### 3. **Operadores Lógicos** - Combinan condiciones booleanas

```python
# AND - Ambas condiciones deben ser True
True and True    # True
True and False   # False

# OR - Al menos una condición debe ser True
True or False    # True
False or False   # False

# NOT - Invierte el valor booleano
not True         # False
not False        # True
```

**Casos de uso en DevOps/Cloud:**
```python
# Verificar salud del servidor
cpu_ok = cpu_uso < 80
memoria_ok = memoria_uso < 90
servidor_saludable = cpu_ok and memoria_ok

# Alerta si algún recurso está crítico
cpu_critico = cpu_uso > 95
memoria_critica = memoria_uso > 95
requiere_atencion = cpu_critico or memoria_critica

# Verificar que el servicio NO esté en mantenimiento
en_mantenimiento = False
puede_recibir_trafico = not en_mantenimiento
```

### 4. **Operadores de Asignación** - Asignan y modifican valores

```python
# Asignación simple
x = 10

# Asignación con operación (shortcuts)
x += 5   # x = x + 5  → 15
x -= 3   # x = x - 3  → 12
x *= 2   # x = x * 2  → 24
x /= 4   # x = x / 4  → 6.0
x //= 2  # x = x // 2 → 3.0
x %= 2   # x = x % 2  → 1.0
x **= 3  # x = x ** 3 → 1.0
```

**Casos de uso en DevOps/Cloud:**
```python
# Incrementar contador de requests
total_requests = 1000
total_requests += 150  # Más legible que total_requests = total_requests + 150

# Actualizar memoria disponible después de despliegue
memoria_disponible_gb = 16
memoria_disponible_gb -= 4  # Se consumen 4GB

# Duplicar capacidad
capacidad_actual = 100
capacidad_actual *= 2  # Escalamiento 2x
```

## 📊 Precedencia de Operadores

Python evalúa las operaciones en un orden específico (como en matemáticas):

```python
# Orden de precedencia (mayor a menor):
# 1. ** (potencia)
# 2. *, /, //, % (multiplicación, división)
# 3. +, - (suma, resta)
# 4. ==, !=, <, >, <=, >= (comparación)
# 5. not
# 6. and
# 7. or

resultado = 10 + 5 * 2    # 20, no 30 (multiplicación primero)
resultado = (10 + 5) * 2  # 30 (paréntesis tienen prioridad)
```

**Buena práctica: Usa paréntesis para claridad**
```python
# ❌ Confuso
calculo = cpu * 100 / total + overhead

# ✅ Claro
calculo = ((cpu * 100) / total) + overhead
```

## 🎨 Buenas Prácticas con Operadores

### ✅ Espaciado según PEP 8

```python
# ✅ Correcto - espacios alrededor de operadores
x = 5 + 3
resultado = (a * b) + c
es_valido = edad >= 18

# ❌ Incorrecto - sin espacios o inconsistente
x=5+3
resultado = (a*b)+c
es_valido = edad>=18
```

**Excepción:** No uses espacios en argumentos de funciones con valores por defecto
```python
# ✅ Correcto
def calcular_costo(instancias=1, precio_hora=0.10):
    pass

# ❌ Incorrecto
def calcular_costo(instancias = 1, precio_hora = 0.10):
    pass
```

### ✅ Nombres descriptivos para resultados booleanos

```python
# ❌ Malo
x = cpu > 80

# ✅ Bueno
cpu_excedida = cpu > 80
necesita_alerta = cpu > 80 and memoria > 90
servidor_disponible = estado == "running" and health_check_ok
```

### ✅ Comparaciones con constantes primero (Yoda Conditions)

Opcional pero ayuda a prevenir errores:

```python
ESTADO_ACTIVO = "running"

# Estilo normal
if estado == ESTADO_ACTIVO:
    pass

# Yoda style (menos propenso a errores de asignación accidental)
if ESTADO_ACTIVO == estado:
    pass

# En Python no es tan crítico porque 'if estado = ESTADO_ACTIVO' da error de sintaxis
```

### ✅ Evita comparaciones innecesarias con booleanos

```python
# ❌ Redundante
if servidor_activo == True:
    pass

# ✅ Directo
if servidor_activo:
    pass

# ❌ Redundante
if servidor_activo == False:
    pass

# ✅ Directo
if not servidor_activo:
    pass
```

## 💡 Conceptos Importantes

### División vs División Entera

```python
# / siempre devuelve float
10 / 2    # 5.0
10 / 3    # 3.333...

# // devuelve int (trunca decimales)
10 // 2   # 5
10 // 3   # 3

# Uso en DevOps:
# Calcular número de servidores necesarios (siempre entero)
usuarios = 1500
USUARIOS_POR_SERVIDOR = 500
servidores_necesarios = usuarios // USUARIOS_POR_SERVIDOR  # 3
```

### Módulo (%) - El Residuo

```python
# % devuelve el residuo de la división
10 % 3   # 1
15 % 5   # 0
7 % 2    # 1

# Usos prácticos:
# 1. Verificar si un número es par o impar
numero = 42
es_par = numero % 2 == 0  # True

# 2. Round-robin (distribución circular)
servidor_id = request_number % total_servidores

# 3. Verificar si necesitas instancias adicionales
if total_requests % servidores != 0:
    print("Considerar balance de carga")
```

### Operadores de Cortocircuito (Short-circuit)

Python optimiza las evaluaciones lógicas:

```python
# AND: Si el primero es False, no evalúa el segundo
False and funcion_costosa()  # funcion_costosa() NO se ejecuta

# OR: Si el primero es True, no evalúa el segundo
True or funcion_costosa()    # funcion_costosa() NO se ejecuta

# Uso práctico:
if archivo_existe and archivo_tiene_permisos():
    # Si archivo_existe es False, no se llama a archivo_tiene_permisos()
    procesar_archivo()
```

## ⚠️ Errores Comunes

### 1. Confundir = (asignación) con == (comparación)
```python
# ❌ Error común
if x = 5:  # SyntaxError
    pass

# ✅ Correcto
if x == 5:
    pass
```

### 2. División por cero
```python
# ❌ Error
resultado = 10 / 0  # ZeroDivisionError

# ✅ Validar antes
if divisor != 0:
    resultado = dividendo / divisor
else:
    print("Error: división por cero")
```

### 3. Usar / cuando necesitas //
```python
# ❌ Incorrecto para contar servidores
servidores = 1000 / 100  # 10.0 (float)

# ✅ Correcto
servidores = 1000 // 100  # 10 (int)
```

### 4. Olvidar paréntesis en expresiones complejas
```python
# ❌ Confuso y posiblemente incorrecto
resultado = a + b * c / d - e

# ✅ Claro
resultado = a + ((b * c) / d) - e
```

## 🎓 Ejemplo Completo con Buenas Prácticas

```python
"""
Monitor de Recursos del Servidor
Calcula métricas y determina estado de salud
"""

# Constantes de umbrales
CPU_WARNING = 70
CPU_CRITICAL = 90
MEMORIA_WARNING = 80
MEMORIA_CRITICAL = 95
DISCO_WARNING = 75

# Métricas actuales del servidor
cpu_uso_porcentaje = 85
memoria_uso_porcentaje = 78
disco_uso_porcentaje = 92
instancias_activas = 3
instancias_minimas = 2

# Cálculos
cpu_disponible = 100 - cpu_uso_porcentaje
memoria_disponible = 100 - memoria_uso_porcentaje

# Evaluaciones de estado
cpu_en_warning = cpu_uso_porcentaje >= CPU_WARNING
cpu_en_critical = cpu_uso_porcentaje >= CPU_CRITICAL
memoria_en_warning = memoria_uso_porcentaje >= MEMORIA_WARNING
disco_en_warning = disco_uso_porcentaje >= DISCO_WARNING

# Decisiones
servidor_saludable = not (cpu_en_critical or memoria_en_critical)
requiere_atencion = cpu_en_warning or memoria_en_warning or disco_en_warning
tiene_redundancia = instancias_activas > instancias_minimas

# Reportes
print("=== Estado del Servidor ===")
print(f"CPU: {cpu_uso_porcentaje}% (Disponible: {cpu_disponible}%)")
print(f"Memoria: {memoria_uso_porcentaje}%")
print(f"Disco: {disco_uso_porcentaje}%")
print(f"\n¿Servidor saludable? {servidor_saludable}")
print(f"¿Requiere atención? {requiere_atencion}")
print(f"¿Tiene redundancia? {tiene_redundancia}")

# Incrementar contador de checks (operador de asignación)
total_health_checks = 100
total_health_checks += 1
print(f"\nTotal health checks: {total_health_checks}")
```

## 🔗 Conexión con lo Aprendido

Los operadores trabajan con las **variables y tipos de datos** que aprendiste en la sección anterior:
- Aritméticos con `int` y `float`
- Comparación con cualquier tipo
- Lógicos con `bool`
- Asignación con todos los tipos

Próximamente usarás operadores en **condicionales** para tomar decisiones y en **loops** para controlar iteraciones.

## ✅ Checklist de Dominio

- [ ] Uso operadores aritméticos (+, -, *, /, //, %, **)
- [ ] Entiendo la diferencia entre / y //
- [ ] Uso operadores de comparación correctamente
- [ ] Combino condiciones con and, or, not
- [ ] Aplico operadores de asignación (+=, -=, etc.)
- [ ] Comprendo la precedencia de operadores
- [ ] Uso paréntesis para claridad
- [ ] Sigo PEP 8 en el espaciado de operadores

---

**¡Ahora es tu turno!** 🎤

Antes de pasar a los ejercicios, responde estas preguntas:

1. **¿Cuál es la diferencia entre `/` y `//`? ¿Cuándo usarías cada uno?**
2. **¿Qué devuelve el operador `%` y para qué podría ser útil en DevOps/Cloud?**
3. **Explica la diferencia entre `and` y `or`. Dame un ejemplo de cuándo usarías cada uno en monitoreo de servidores.**
4. **¿Por qué es importante usar paréntesis en expresiones con múltiples operadores?**