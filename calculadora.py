# Programa: Calculadora de Reajuste Salarial

# Entrada de dados
nome = input("Digite o nome do colaborador: ")
salario_atual = float(input("Digite o salário atual (R$): "))
porcentagem = float(input("Digite a porcentagem de aumento (%): "))

# Cálculo do aumento
valor_aumento = salario_atual * (porcentagem / 100)

# Cálculo do novo salário
novo_salario = salario_atual + valor_aumento

# Saída de dados
print("\n--- Resultado do Reajuste Salarial ---")
print(f"Colaborador: {nome}")
print(f"Valor do aumento: R$ {valor_aumento:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")