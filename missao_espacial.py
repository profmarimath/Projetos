# missao_espacial.py

nome = input("Digite seu nome completo (astronauta da missão): ")
distancia = float(input("Digite a distância da viagem em km: "))
velocidade = float(input("Digite a velocidade média da nave em km/h: "))

tempo_horas = distancia / velocidade
tempo_dias = tempo_horas / 24

print("\nAstronauta", nome + ", bem-vindo à simulação!")
print("A viagem terá uma distância de", distancia, "km.")
print("Com velocidade média de", velocidade, "km/h, o tempo estimado é:")
print(f"{tempo_horas:.2f} horas ({tempo_dias:.2f} dias).")
print("Boa sorte na missão!")