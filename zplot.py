#!/usr/bin/python3
# coding: utf-8


import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import tkinter
from tkinter import filedialog
import tkinter.messagebox
import matplotlib.pyplot as plt
import os
import xlsxwriter


# define o local da onde o script esta sendo rodado
global script_path
script_path = os.getcwd()  

# Parametros tkinter
window = tkinter.Tk()
window.geometry('640x480')  # window size
window.title("Welcome to Z-Plot App")  # window title

# Linha 1 - Abrir arquivo coletado para trabalhar e transformar em .xlsx
lbl = tkinter.Label(window, text="Clique para abrir o arquivo...",
                    font=("Arial Bold", 11))  # Text inside window
lbl.grid(column=0, row=0)  # posição do label


def open_file():  # criar função para quando o botão for clicado
    tkinter.Tk().withdraw()
    global data_file  # criar variavel global, pode ser usada fora da função
    data_file = filedialog.askopenfilename(initialdir=script_path, title="Select file",
                                filetypes=(("CSV Files", '*.csv'), ("Text Files", '*.txt'), ("all files", "*.*")))


btn = tkinter.Button(window, text="Abrir arquivo", bg="white", fg="blue",
                     command=open_file)  # criar botão/ command=função do botão
btn.grid(column=1, row=0)  # posição do botão

# Linha 2 - Salvar arquivo para xlxs
lblz = tkinter.Label(window, text="Clique para calcular o Z e salvar em Excel",
                    font=("Arial Bold", 11))  # Text inside window
lblz.grid(column=0, row=1)  # posição do label

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
    worksheet.insert_chart('G7', chart)
    writer.save()
    tkinter.messagebox.showinfo('File Saved','Salvo em ' + file_to_save)
    

btnz = tkinter.Button(window, text="Gogogo", bg="white", fg="blue",
                     command=Ztest)  # criar botão/ command=função do botão
btnz.grid(column=1, row=1)  # posição do botão

# Confirma saída do programa e fecha de vez
def confirmExit():
    if tkinter.messagebox.askokcancel('Quit', 'Are you sure you want to exit?'):
        window.destroy()


window.protocol('WM_DELETE_WINDOW', confirmExit)

# need loop to maintain it open - Abre o tkinter e mantem em loop
window.mainloop()  


