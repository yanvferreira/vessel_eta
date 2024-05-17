#Criado por 3ºSG-PD FERREIRA em 15ABR24
#DIVISÃO DE TELEMÁTICA

from tkinter import *
from tkinter import messagebox
import ttkbootstrap as ttk
from datetime import datetime, timedelta

def preencher_datahora_atual():
    # Obter a data e hora atuais
    datahora_atual = datetime.now()

    # Formatar a data e hora como uma string no formato desejado
    datahora_formatada = datahora_atual.strftime("%d/%m/%Y %H:%M")

    return datahora_formatada

def calcular_fuso_horario(data_futura, timezone_selecionado):
    if timezone_selecionado == "P":
        data_futura_fuso_atualizado = data_futura + timedelta(hours=3)
        timezone = "Z"
    else:
        data_futura_fuso_atualizado = data_futura - timedelta(hours=3)
        timezone = "P"
    
    eta_fuso_label.config(text="ETA: " + data_futura_fuso_atualizado.strftime("%d/%m/%Y às %H:%M") + timezone)


def calcular_tempo_estimado():
    try:
        distancia = float(entry_distancia.get())
        veloc = float(entry_velocidade.get())
        datahora_ultima_posicao = entry_datahora_ultima_posicao.get()
        
        # Obter o valor selecionado do Combobox
        timezone_selecionado = timezone_combobox.get()
        if timezone_selecionado == "Selecionar fuso horário":
            raise ValueError

        datahora_ultima_posicao = datetime.strptime(datahora_ultima_posicao, "%d/%m/%Y %H:%M")

        horas = distancia / veloc
        delta = timedelta(hours=horas)

        dias = delta.days
        horas_restantes = delta.seconds // 3600
        minutos_restantes = (delta.seconds % 3600) // 60

        tempo_estimado_label.config(text="Tempo estimado: {} dias, {} horas e {} minutos".format(dias, horas_restantes, minutos_restantes))

        datahora_ultima_posicao_label.config(text="Ultimo sinal emitido em: " + datahora_ultima_posicao.strftime("%d/%m/%Y às %H:%M") + timezone_selecionado)

        data_futura = datahora_ultima_posicao + delta

        eta_label.config(text="ETA: " + data_futura.strftime("%d/%m/%Y às %H:%M") + timezone_selecionado)

        #calcula em outro fuso horario
        calcular_fuso_horario(data_futura, timezone_selecionado)
        

    except ValueError:
        messagebox.showerror("Erro", "Digite os dados no formato correto!")
    except ZeroDivisionError:
        messagebox.showerror("Erro", "Não se pode dividir pela velocidade zero!")
    except Exception as e:
        messagebox.showerror("Erro", "Algo deu errado, tente novamente!")

def calcular_data():
    try:
        dt_inicial = datetime.strptime(entry_data_inicio.get(), "%d/%m/%Y %H:%M")
        dt_final = datetime.strptime(entry_data_fim.get(), "%d/%m/%Y %H:%M")

        data_result = dt_final - dt_inicial

        messagebox.showinfo("Teste", data_result.seconds // 3600)

    except Exception as e:
        messagebox.showerror("Erro", "Algo deu errado, tente novamente!")

def limpar_campos():
    entry_distancia.delete(0, END)
    entry_velocidade.delete(0, END)
    entry_datahora_ultima_posicao.delete(0, END)
    timezone_combobox.set("Selecionar fuso horário")
    tempo_estimado_label.config(text="")
    datahora_ultima_posicao_label.config(text="")
    eta_label.config(text="")
    eta_fuso_label.config(text="")

# Criando a tela
root = ttk.Window(themename="superhero")
#root = tk.Tk()
root.title("VESSEL ETA - Calculadora de Tempo Estimado")

notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

#frame = Frame(root)
#frame.pack(padx=10, pady=10)

frame_eta = Frame(notebook)
frame_eta.pack(fill='both', expand=True)

frame_data = Frame(notebook)
frame_data.pack(fill='both', expand=True)

frame_help = Frame(notebook)
frame_help.pack(fill='both', expand=True)

notebook.add(frame_eta, text="Cálculo ETA")
notebook.add(frame_data, text="Cálculo de Data")
notebook.add(frame_help, text="Ajuda")

label_distancia = Label(frame_eta, text="Distância em MN (Milhas Náuticas):")
label_distancia.grid(row=0, column=0, sticky="w")

entry_distancia = Entry(frame_eta)
entry_distancia.grid(row=0, column=1)
entry_distancia.focus_set() 

label_velocidade = Label(frame_eta, text="Velocidade Média em Nós:")
label_velocidade.grid(row=1, column=0, sticky="w")

entry_velocidade = Entry(frame_eta)
entry_velocidade.grid(row=1, column=1)

label_datahora_ultima_posicao = Label(frame_eta, text="DATAHORA da última posição (exemplo: 01/09/2023 12:30):")
label_datahora_ultima_posicao.grid(row=2, column=0, sticky="w")

entry_datahora_ultima_posicao = Entry(frame_eta)
entry_datahora_ultima_posicao.grid(row=2, column=1)
entry_datahora_ultima_posicao.insert(0, preencher_datahora_atual())

label_fuso_horario = Label(frame_eta, text="Selecione o fuso horário:")
label_fuso_horario.grid(row=3, column=0, sticky="w")

timezones = ["P", "Z", "Selecionar fuso horário"]
timezone_combobox = ttk.Combobox(frame_eta, values=timezones, state="readonly")
timezone_combobox.set("P")
timezone_combobox.grid(row=3, column=1)

calcular_button = Button(frame_eta, text="Calcular", command=calcular_tempo_estimado)
calcular_button.grid(row=4, column=0, sticky="e", padx=5, pady=5)

limpar_button = Button(frame_eta, text="Limpar", command=limpar_campos)
limpar_button.grid(row=4, column=1, sticky="e", padx=5, pady=5)

tempo_estimado_label = Label(frame_eta, text="")
tempo_estimado_label.grid(row=5, columnspan=2)

datahora_ultima_posicao_label = Label(frame_eta, text="")
datahora_ultima_posicao_label.grid(row=6, columnspan=2)

eta_label = Label(frame_eta, text="")
eta_label.grid(row=7, columnspan=2)

eta_fuso_label = Label(frame_eta, text="")
eta_fuso_label.grid(row=8, columnspan=2)

#frame Data
label_data_inicio = Label(frame_data, text="Data Inicial")
label_data_inicio.grid(row=0, column=0, sticky="w")

entry_data_inicio = Entry(frame_data)
entry_data_inicio.grid(row=0, column=1)
entry_data_inicio.insert(0, preencher_datahora_atual())

label_data_fim = Label(frame_data, text="Data Final")
label_data_fim.grid(row=1, column=0, sticky="w")

entry_data_fim = Entry(frame_data)
entry_data_fim.grid(row=1, column=1)
entry_data_fim.insert(0, preencher_datahora_atual())

calcular_button_data = Button(frame_data, text="Calcular", command=calcular_data)
calcular_button_data.grid(row=0, column=4, sticky="e", padx=15, pady=5)

#frame Ajuda
label_ajuda = Label(frame_help, text="Desenvolvido por 3ºSG-PD FERREIRA", bg="lightgray")
label_ajuda.grid(row=0, columnspan=2)

label_ajuda = Label(frame_help, text="Divisão de Telemática", bg="lightgray")
label_ajuda.grid(row=1, columnspan=2)

root.mainloop()
