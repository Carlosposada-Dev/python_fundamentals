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

EXCELLENT_SERVICE_TIP = 0.20
GOOD_SERVICE_TIP = 0.15
REGULAR_SERVICE_TIP = 0.10

print("TIP CALCULATOR\n")
bill_amount = float(input("Please enter the total bill amount: "))
service_level = int(input("Please enter the service level (1 = regular, 2 = good, 3 = excellent): "))

if service_level == 3:
    tip_percentage = EXCELLENT_SERVICE_TIP
elif service_level == 2:
    tip_percentage = GOOD_SERVICE_TIP
elif service_level == 1:
    tip_percentage = REGULAR_SERVICE_TIP
else:
    print("Invalid service level. Please enter 1, 2, or 3.")
    exit()

tip_amount = bill_amount * tip_percentage
total_amount = bill_amount + tip_amount

print(f"Billing data:")
print(f" - Bill amount: ${bill_amount:.2f}")
print(f" - Tip percentage applied: {tip_percentage:.0%}")
print(f" - Tip amount: {tip_amount:.2f}")
print(f" - Total amount to pay: ${total_amount:.2f}")