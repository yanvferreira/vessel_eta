from datetime import datetime, timedelta

try:
    distancia = float(input("Digite a distância em MN (Milhas Náuticas), não use vígula: "))
    veloc = float(input("Digite a Velocidade Média em Nós, não use vígula: "))
    datahora_ultima_posicao = input("Digite a DATAHORA da última posição exemplo: 01/09/2023 12:30: ")

    datahora_ultima_posicao = datetime.strptime(datahora_ultima_posicao, "%d/%m/%Y %H:%M")
except ValueError:
    print("Digite os dados no formato correto!")
    print(ValueError)
except:
    print("Algo deu errado, tente novamente!")

try:
    horas = distancia / veloc
except ZeroDivisionError:
    print("Não se pode dividir pela velocidade zero!")

delta = timedelta(hours=horas)

print("O tempo estimado é de", delta)

print("Ultimo sinal emitido em: ", datahora_ultima_posicao.strftime("%d/%m/%Y às %H:%M"))

data_futura = datahora_ultima_posicao + delta

print("ETA:", data_futura.strftime("%d/%m/%Y às %H:%M"))