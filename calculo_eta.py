#Criado por 3ºSG-PD FERREIRA em 15ABR24
#DIVISÃO DE TELEMÁTICA

from tkinter import *
from tkinter import messagebox
from datetime import datetime, timedelta

def calcular_tempo_estimado():
    try:
        distancia = float(entry_distancia.get())
        veloc = float(entry_velocidade.get())
        datahora_ultima_posicao = entry_datahora_ultima_posicao.get()

        datahora_ultima_posicao = datetime.strptime(datahora_ultima_posicao, "%d/%m/%Y %H:%M")

        horas = distancia / veloc
        delta = timedelta(hours=horas)

        tempo_estimado_label.config(text="Tempo estimado: " + str(delta))

        datahora_ultima_posicao_label.config(text="Ultimo sinal emitido em: " + datahora_ultima_posicao.strftime("%d/%m/%Y às %H:%M"))

        data_futura = datahora_ultima_posicao + delta

        eta_label.config(text="ETA: " + data_futura.strftime("%d/%m/%Y às %H:%M"))

    except ValueError:
        messagebox.showerror("Erro", "Digite os dados no formato correto!")
    except ZeroDivisionError:
        messagebox.showerror("Erro", "Não se pode dividir pela velocidade zero!")
    except Exception as e:
        messagebox.showerror("Erro", "Algo deu errado, tente novamente!")

root = Tk()
root.title("Calculadora de Tempo Estimado")

frame = Frame(root)
frame.pack(padx=10, pady=10)

label_distancia = Label(frame, text="Distância em MN (Milhas Náuticas):")
label_distancia.grid(row=0, column=0, sticky="w")

entry_distancia = Entry(frame)
entry_distancia.grid(row=0, column=1)

label_velocidade = Label(frame, text="Velocidade Média em Nós:")
label_velocidade.grid(row=1, column=0, sticky="w")

entry_velocidade = Entry(frame)
entry_velocidade.grid(row=1, column=1)

label_datahora_ultima_posicao = Label(frame, text="DATAHORA da última posição (exemplo: 01/04/2024 12:30):")
label_datahora_ultima_posicao.grid(row=2, column=0, sticky="w")

entry_datahora_ultima_posicao = Entry(frame)
entry_datahora_ultima_posicao.grid(row=2, column=1)

calcular_button = Button(frame, text="Calcular", command=calcular_tempo_estimado)
calcular_button.grid(row=3, columnspan=2, pady=10)

tempo_estimado_label = Label(frame, text="")
tempo_estimado_label.grid(row=4, columnspan=2)

datahora_ultima_posicao_label = Label(frame, text="")
datahora_ultima_posicao_label.grid(row=5, columnspan=2)

eta_label = Label(frame, text="")
eta_label.grid(row=6, columnspan=2)

root.mainloop()
