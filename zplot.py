#!/usr/bin/python3
# coding: utf-8



import numpy as np
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import seaborn
import tkinter
from tkinter import *
from tkinter.filedialog import askopenfilename
import tkinter.messagebox
import matplotlib.pyplot as plt
import os
import sys
import openpyxl


# In[2]:


global script_path
script_path = os.getcwd()  # define o local da onde o script esta sendo rodado
# print(script_path)


# In[3]:


window = tkinter.Tk()
window.geometry('640x480')  # window size
window.title("Welcome to GUI Plot App")  # window title


# In[4]:


lbl = tkinter.Label(window, text="Clique para abrir o arquivo...",
                    font=("Arial Bold", 11))  # Text inside window
lbl.grid(column=0, row=0)  # posição do label


def open_file():  # criar função para quando o botão for clicado
    tkinter.Tk().withdraw()
    global data_file  # criar variavel global, pode ser usada fora da função
    data_file = askopenfilename(initialdir=script_path, title="Select file",
                                filetypes=(("CSV Files", '*.csv'), ("Text Files", '*.txt'), ("all files", "*.*")))


btn = tkinter.Button(window, text="Abrir arquivo", bg="white", fg="blue",
                     command=open_file)  # criar botão/ command=função do botão
btn.grid(column=1, row=0)  # posição do botão


# In[5]:


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
    #writer = ExcelWriter(data_file.replace('.csv', '.xlsx'))
    from tkinter import filedialog
    file_to_save =  filedialog.asksaveasfilename(initialdir=script_path,
                                                 title="Select file", 
                                                 filetypes=(("XLSX Files", '*.xlsx'),("all files","*.*")))
    writer = ExcelWriter(file_to_save)
    ztest.to_excel(writer,'Sheet1',index=False)
    writer.save()

btnz = tkinter.Button(window, text="Gogogo", bg="white", fg="blue",
                     command=Ztest)  # criar botão/ command=função do botão
btnz.grid(column=1, row=1)  # posição do botão


# In[ ]:


def confirmExit():
    if tkinter.messagebox.askokcancel('Quit', 'Are you sure you want to exit?'):
        window.destroy()


window.protocol('WM_DELETE_WINDOW', confirmExit)

window.mainloop()  # need loop to maintain it open

