# ⚡ Calculadora de Consumo Elétrico Inteligente

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![GitHub](https://img.shields.io/badge/GitHub-Repositório-black?logo=github)
![Energia](https://img.shields.io/badge/Energia-Elétrica-yellow)

##  🎯 Objetivo

Este projeto foi desenvolvido para calcular o consumo mensal de energia elétrica de aparelhos domésticos.

O usuário deverá informar:

- Nome do aparelho
- Potência em watts (W)
- Tempo médio de uso diário

O sistema calcula automaticamente:

- Consumo mensal em kWh
- Custo estimado em reais

---

##  🧠 Linguagem Utilizada

 **Python**

---

##  📐 Fórmula Utilizada
consumoMensal = (potencia * horas_dia * 30) / 1000
Onde:

- potencia → potência do aparelho (W)
- horasDia → horas usadas por dia
- 30 → dias do mês
- 1000 → conversão para kWh

---

##  ▶️ Como Executar

1. Abra o terminal
2. Navegue até a pasta do projeto:  projetos/consumo-energia
3. Execute o programa: python app.py
4. Digite os dados solicitados e veja o resultado.

---

##  💡 Exemplo de Uso: Digite o nome do aparelho: televisão
Digite a potência do aparelho (em watts - W): 150
Digite o tempo médio de uso diário (em horas): 10

=== Resultado ===

Aparelho: televisão
Consumo estimado: 45.00 kWh/mês
Custo estimado: R$ 33.75

## 📂 Estrutura do Projeto


consumo-energia
│
├── app.py
└── README.md


---

##  👩‍💻 Autor

Projeto desenvolvido por Mariane Castro, como atividade de Desenvolvimento de Sistemas I.