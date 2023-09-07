from datetime import datetime, timedelta

distancia = float(input("Digite a distância em MN (Milhas Náuticas): "))
veloc = float(input("Digite a Velocidade Média em Nós: "))
datahora_ultima_posicao = input("Digite a DATAHORA da última posição exemplo: 01/09/2023 12:30: ")

datahora_ultima_posicao = datetime.strptime(datahora_ultima_posicao, "%d/%m/%Y %H:%M")
horas = distancia / veloc

delta = timedelta(hours=horas)

print("O tempo estimado é de", delta)

print("Ultimo sinal emitido em: ", datahora_ultima_posicao.strftime("%d/%m/%Y às %H:%M"))

data_futura = datahora_ultima_posicao + delta

print("ETA:", data_futura.strftime("%d/%m/%Y às %H:%M"))