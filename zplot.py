#!/usr/bin/python3
# coding: utf-8


import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import tkinter
from tkinter import filedialog
from tkinter import ttk
import tkinter.messagebox
import matplotlib.pyplot as plt
import os
import xlsxwriter


# define o local da onde o script esta sendo rodado
global script_path
script_path = os.getcwd()  

# Parametros tkinter
window = tkinter.Tk()
# window.geometry('800x520')  # window size
window.title("Welcome to Z-Plot App")  # window title

# Adicionando tabs
tab_control = ttk.Notebook(window) 
tab1 = ttk.Frame(tab_control) 
tab2 = ttk.Frame(tab_control) 
tab_control.add(tab1, text='Gerar arquivos') 
tab_control.add(tab2, text='Coletar dados')

# ------------------------- TAB1---------------------------------------

# Linha 1 - Abrir arquivo coletado para trabalhar e transformar em .xlsx
lbl1 = tkinter.Label(tab1, text="Clique para abrir o arquivo...",
                     font=("Arial Bold", 11),
                     padx=5, pady=5)  # Text inside window
lbl1.grid(column=0, row=0)  # posição do label


def open_file():  # criar função para quando o botão for clicado
    global data_file  # criar variavel global, pode ser usada fora da função
    data_file = filedialog.askopenfilename(initialdir=script_path, title="Select file",
                                filetypes=(("CSV Files", '*.csv'), ("Text Files", '*.txt'), ("all files", "*.*")))
    lbl1.configure(text=data_file)
    btn1.configure(text="Selecionar outro arquivo")



btn1 = tkinter.Button(tab1, text="Selecionar arquivo", bg="white", fg="blue",
                     command=open_file,
                     padx=5, pady=5)  # criar botão/ command=função do botão
btn1.grid(column=1, row=0)  # posição do botão

# Linha 2 - Salvar arquivo para xlxs direto
lbl2 = tkinter.Label(tab1, text="Gerar arquivo .xlsx",
                    font=("Arial Bold", 11),
                     padx=5, pady=5)  # Text inside window
lbl2.grid(column=0, row=1)  # posição do label

def Ztesta(): 
    ztest = pd.read_csv(data_file, sep=' ', names=["Time", "Ones"])
    ztest.dropna(inplace = True)
    ztest = ztest.reset_index()
    ztest['index'] = ztest['index'] + 1
    ztest['Sum'] = ztest['Ones'].cumsum()
    ztest['Average'] = ztest['Sum']/(ztest['index'])
    ztest['Zscore'] = (ztest['Average']-1024)/(22.62741699796/(ztest['index']**0.5))
    file_to_save =  data_file.replace(".csv", ".xlsx")
    data_file2 = os.path.basename(data_file)
    data_file2 = data_file2.replace(".csv", "")
    number_rows = len(ztest.index)
    writer = pd.ExcelWriter(file_to_save, engine='xlsxwriter')
    ztest.to_excel(writer,sheet_name='Z-Test',index=False)
    workbook = writer.book
    worksheet = writer.sheets['Z-Test']
    chart = workbook.add_chart({'type': 'line'})
    chart.set_title({
    'name': 'Z-Score: ' + data_file2,
    'name_font': {
        'name': 'Calibri',
        'color': 'black',
        },
    })

    chart.set_x_axis({
    'name': 'Time',
    'name_font': {
        'name': 'Calibri',
        'color': 'black'
        },
    'num_font': {
        'name': 'Calibri',
        'color': 'black',
        },
    })

    chart.set_y_axis({
    'name': 'Z-Score',
    'name_font': {
        'name': 'Calibri',
        'color': 'black'
        },
    'num_font': {
        'color': 'black',
        },
    })

    chart.set_legend({'position': 'none'})
    chart.add_series({'values': ['Z-Test', 1, 5, number_rows, 5],
                      'categories': ['Z-Test', 1, 1, number_rows, 1]})
    worksheet.insert_chart('G2', chart)
    writer.save()
    tkinter.messagebox.showinfo('File Saved','Salvo em ' + file_to_save)
    

btn2 = tkinter.Button(tab1, text="Gerar", bg="white", fg="blue",
                     command=Ztesta,
                     padx=5, pady=5)  # criar botão/ command=função do botão
btn2.grid(column=1, row=1)  # posição do botão

# Linha 3 - Salvar as arquivo para xlxs
lbl3 = tkinter.Label(tab1, text="Gerar e salvar em...",
                    font=("Arial Bold", 11),
                     padx=5, pady=5)  # Text inside window
lbl3.grid(column=0, row=2)  # posição do label

def Ztest(): 
    ztest = pd.read_csv(data_file, sep=' ', names=["Time", "Ones"])
    ztest.dropna(inplace = True)
    ztest = ztest.reset_index()
    ztest['index'] = ztest['index'] + 1
    ztest['Sum'] = ztest['Ones'].cumsum()
    ztest['Average'] = ztest['Sum']/(ztest['index'])
    ztest['Zscore'] = (ztest['Average']-1024)/(22.62741699796/(ztest['index']**0.5))
    data_file2 = os.path.basename(data_file)
    data_file2 = data_file2.replace(".csv", "")
    file_to_save =  filedialog.asksaveasfilename(initialdir=script_path,
                                                 initialfile=data_file2,
                                                 title="Select file", 
                                                 filetypes=(("XLSX Files", '*.xlsx'),("all files","*.*")))
    number_rows = len(ztest.index)
    writer = pd.ExcelWriter(file_to_save, engine='xlsxwriter')
    ztest.to_excel(writer,sheet_name='Z-Test',index=False)
    workbook = writer.book
    worksheet = writer.sheets['Z-Test']
    chart = workbook.add_chart({'type': 'line'})
    chart.set_title({
    'name': 'Z-Score: ' + data_file2,
    'name_font': {
        'name': 'Calibri',
        'color': 'black',
        },
    })

    chart.set_x_axis({
    'name': 'Time',
    'name_font': {
        'name': 'Calibri',
        'color': 'black'
        },
    'num_font': {
        'name': 'Calibri',
        'color': 'black',
        },
    })

    chart.set_y_axis({
    'name': 'Z-Score',
    'name_font': {
        'name': 'Calibri',
        'color': 'black'
        },
    'num_font': {
        'color': 'black',
        },
    })

    chart.set_legend({'position': 'none'})
    chart.add_series({'values': ['Z-Test', 1, 5, number_rows, 5],
                      'categories': ['Z-Test', 1, 1, number_rows, 1]})
    worksheet.insert_chart('G2', chart)
    writer.save()
    tkinter.messagebox.showinfo('File Saved','Salvo em ' + file_to_save)
    

btn3 = tkinter.Button(tab1, text="Savar em...", bg="white", fg="blue",
                     command=Ztest,
                     padx=5, pady=5)  # criar botão/ command=função do botão
btn3.grid(column=1, row=2)  # posição do botão

# ------------------------------TAB2 -----------------------------------
lbl21 = tkinter.Label(tab2, text="Coletar dados",
                     font=("Arial Bold", 11),
                     padx=5, pady=5)  # Text inside window
lbl21.grid(column=0, row=0)  # posição do label

lbl22 = tkinter.Label(tab2, text="Finalizar coleta",
                     font=("Arial Bold", 11),
                     padx=5, pady=5)  # Text inside window
lbl22.grid(column=0, row=1)  # posição do label


def bbla():  # criar função para quando o botão for clicado
    import subprocess
    f_status = "f0"
    subprocess.run(["./bbla {}".format(f_status)], shell=True)


def stopBbla():
    import subprocess
    subprocess.run(["ps -ef | awk '/bbla/{print$2}' | sudo xargs kill 2>/dev/null"], shell=True)



btn21 = tkinter.Button(tab2, text="Iniciar coleta", bg="white", fg="blue",
                     command=bbla,
                     padx=5, pady=5)  # criar botão/ command=função do botão
btn21.grid(column=1, row=0)  # posição do botão

btn22 = tkinter.Button(tab2, text="Parar coleta", bg="white", fg="blue",
                     command=stopBbla,
                     padx=5, pady=5)  # criar botão/ command=função do botão
btn22.grid(column=1, row=1)  # posição do botão


# Confirma saída do programa e fecha de vez
def confirmExit():
    if tkinter.messagebox.askokcancel('Quit', 'Are you sure you want to exit?'):
        window.destroy()


window.protocol('WM_DELETE_WINDOW', confirmExit)


# need loop to maintain it open - Abre o tkinter e mantem em loop
tab_control.pack(expand=1, fill='both')
window.mainloop()  


