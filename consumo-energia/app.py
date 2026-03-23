# Calculadora de Consumo Elétrico Inteligente 

print("=== Calculadora de Consumo Elétrico ===")

# Entrada de dados
aparelho = input("Digite o nome do aparelho: ")

potencia = float(input("Digite a potência do aparelho (em watts - W): "))

horas_dia = float(input("Digite o tempo médio de uso diário (em horas): "))

# Cálculo do consumo mensal
consumo_mensal = (potencia * horas_dia * 30) / 1000

# Cálculo do custo estimado
valor_kwh = 0.75  # valor fixo por kWh (pode alterar depois)
custo_estimado = consumo_mensal * valor_kwh

# Saída formatada
print("\n=== Resultado ===")

print(f"Aparelho: {aparelho}")

print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")

print(f"Custo estimado: R$ {custo_estimado:.2f}")