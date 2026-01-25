"""
Sección 3: Operators
Ejercicios Prácticos - DevOps & Cloud Engineering

Instrucciones Generales:
- Sigue las convenciones de PEP 8 (espaciado correcto alrededor de operadores)
- Usa nombres de variables descriptivos en snake_case
- Define constantes en UPPER_SNAKE_CASE
- Evita números mágicos
- Usa paréntesis para claridad en expresiones complejas
- Crea tu archivo 'soluciones.py' con tus respuestas
"""

# ============================================
# Ejercicio 1: Calculadora de Costos de AWS EC2
# ============================================
# Dificultad: Fácil
# Objetivo: Practicar operadores aritméticos básicos
# Contexto: Calcular el costo mensual de instancias EC2
#
# TODO:
# 1. Define constantes:
#    - Horas por mes: 730
#    - Costo por hora de instancia t3.medium: $0.0416
# 2. Solicita al usuario el número de instancias que desea desplegar
# 3. Calcula:
#    - Costo mensual por instancia
#    - Costo total mensual (todas las instancias)
#    - Costo anual (12 meses)
# 4. Imprime los resultados con 2 decimales
#    Formato sugerido: "Costo mensual por instancia: $30.37"
#
# Escribe tu solución en soluciones.py


# ============================================
# Ejercicio 2: Monitor de CPU - Sistema de Alertas
# ============================================
# Dificultad: Fácil-Medio
# Objetivo: Practicar operadores de comparación y lógicos
# Contexto: Determinar el nivel de alerta según uso de CPU
#
# TODO:
# 1. Define constantes para umbrales:
#    - CPU_WARNING: 70%
#    - CPU_CRITICAL: 90%
# 2. Solicita al usuario el porcentaje de uso de CPU actual
# 3. Calcula el porcentaje disponible de CPU
# 4. Determina el estado usando operadores de comparación:
#    - estado_normal: CPU < 70%
#    - estado_warning: CPU >= 70% pero < 90%
#    - estado_critical: CPU >= 90%
# 5. Imprime:
#    - Uso y disponibilidad de CPU
#    - Estado actual (Normal, Warning, o Critical)
#
# PISTA: Usa operadores lógicos (and) para rangos
#
# Escribe tu solución en soluciones.py


# ============================================
# Ejercicio 3: Balanceador de Carga Round-Robin
# ============================================
# Dificultad: Medio
# Objetivo: Practicar operador módulo (%)
# Contexto: Distribuir requests entre servidores usando round-robin
#
# TODO:
# 1. Define constante:
#    - TOTAL_SERVIDORES: 4
# 2. Simula 15 requests entrantes (usa un loop manual o simula con números)
# 3. Para cada request, calcula a qué servidor debe ir usando módulo:
#    servidor_asignado = numero_request % TOTAL_SERVIDORES
# 4. Imprime la distribución de los primeros 10 requests
#    Formato: "Request #1 → Servidor 1"
#            "Request #2 → Servidor 2"
#            etc.
#
# NOTA: Esto simula un algoritmo de load balancing simple
# EXTRA: Cuenta cuántos requests va a cada servidor
#
# Escribe tu solución en soluciones.py


# ============================================
# Ejercicio 4: Calculadora de Subnetting - Hosts Disponibles
# ============================================
# Dificultad: Medio
# Objetivo: Practicar operador potencia (**) y división entera (//)
# Contexto: Calcular hosts disponibles en una subnet
#
# TODO:
# 1. Solicita al usuario la máscara de subred (ejemplo: 24 para /24)
# 2. Calcula:
#    - Total de direcciones IP = 2 ** (32 - mascara)
#    - Hosts utilizables = total_direcciones - 2 (red y broadcast)
# 3. Si el usuario quiere distribuir hosts en múltiples subnets:
#    - Solicita número de subnets deseadas
#    - Calcula hosts por subnet usando división entera (//)
# 4. Imprime todos los resultados
#
# Ejemplo:
#   Máscara: /24
#   Total IPs: 256
#   Hosts utilizables: 254
#   Si divides en 2 subnets: 127 hosts por subnet
#
# Escribe tu solución en soluciones.py


# ============================================
# Ejercicio 5: Health Check Aggregator
# ============================================
# Dificultad: Medio
# Objetivo: Practicar múltiples operadores lógicos (and, or, not)
# Contexto: Determinar si un servidor está completamente saludable
#
# TODO:
# 1. Define constantes para umbrales:
#    - CPU_MAX: 85
#    - MEMORIA_MAX: 90
#    - DISCO_MAX: 80
#    - LATENCIA_MAX_MS: 200
# 2. Solicita al usuario las métricas actuales:
#    - Uso de CPU (%)
#    - Uso de memoria (%)
#    - Uso de disco (%)
#    - Latencia (ms)
#    - ¿Backup completado? (True/False - usa input y convierte)
# 3. Evalúa condiciones:
#    - recursos_ok: CPU, memoria y disco bajo umbral (usa and)
#    - red_ok: latencia bajo umbral
#    - servidor_saludable: recursos_ok AND red_ok AND backup_completado
#    - requiere_atencion_inmediata: CPU > 95 OR memoria > 95
# 4. Imprime el resultado de todas las evaluaciones
#
# NOTA: Esto simula un health check agregado de múltiples métricas
#
# Escribe tu solución en soluciones.py


# ============================================
# Ejercicio 6: Auto-Scaling Decision Engine
# ============================================
# Dificultad: Medio-Difícil
# Objetivo: Combinar todos los operadores aprendidos
# Contexto: Decidir si escalar instancias basado en múltiples métricas
#
# TODO:
# 1. Define constantes:
#    - INSTANCIAS_MIN: 2
#    - INSTANCIAS_MAX: 10
#    - CPU_SCALE_UP: 75
#    - CPU_SCALE_DOWN: 30
#    - REQUESTS_POR_INSTANCIA: 1000
# 2. Solicita datos actuales:
#    - Número de instancias activas
#    - CPU promedio (%)
#    - Total de requests actuales
# 3. Calcula:
#    - Requests por instancia actual = total_requests // instancias
#    - ¿Necesita scale up? (CPU > 75 OR requests_por_instancia > 1000)
#    - ¿Puede scale down? (CPU < 30 AND requests_por_instancia < 500 AND instancias > MIN)
#    - ¿Está en límite máximo? (instancias >= MAX)
#    - ¿Está en límite mínimo? (instancias <= MIN)
# 4. Determina acción recomendada:
#    - "Scale Up" si necesita y no está en máximo
#    - "Scale Down" si puede y no está en mínimo
#    - "Mantener" si está en equilibrio
#    - "En límite" si no puede escalar más
# 5. Imprime análisis completo y recomendación
#
# EXTRA: Calcula cuántas instancias agregar/quitar (±1 o ±2 según severidad)
#
# Escribe tu solución en soluciones.py


# ============================================
# Ejercicio 7: Verificador de Direcciones IP Pares/Impares
# ============================================
# Dificultad: Medio
# Objetivo: Practicar operador módulo para verificar paridad
# Contexto: Clasificar IPs para diferentes pools (pares/impares)
#
# TODO:
# 1. Solicita al usuario el último octeto de una IP (0-255)
#    Ejemplo: Para 192.168.1.100, ingresa 100
# 2. Verifica:
#    - ¿Es par o impar? (usa módulo %)
#    - ¿Es múltiplo de 5? (útil para crear pools cada 5 IPs)
#    - ¿Es divisible entre 10?
# 3. Basado en paridad, asigna a un pool:
#    - IPs pares → Pool A (servidores web)
#    - IPs impares → Pool B (servidores de aplicación)
# 4. Imprime:
#    - IP completa (asume red 192.168.1.X)
#    - Paridad (Par/Impar)
#    - Pool asignado
#    - Si es múltiplo de 5 o 10
#
# NOTA: En redes reales esto se usa para segmentación y organización
#
# Escribe tu solución en soluciones.py


# ============================================
# IMPORTANTE:
# ============================================
# 1. Crea un archivo 'soluciones.py' en la misma carpeta
# 2. Resuelve cada ejercicio aplicando PEP 8 y Clean Code
# 3. Prueba tu código con diferentes valores de entrada
# 4. Piensa en casos edge (CPU 0%, 100%, valores negativos, etc.)
# 5. Cuando termines, comparte tu código para revisión
#
# ¡Éxito! 🚀
# ============================================