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

width = float(input("Please, enter the rectangle widht in cm(can be decimal): "))
height = float(input ("Please, enter the rectangle height in cm(can be decimal): "))

area =  width * height
perimeter = 2 * (width + height)

print (f"Rectangle area is : {area:.2f} cm²")
print (f"Rectangle perimeter is: {perimeter:.2f} cm")