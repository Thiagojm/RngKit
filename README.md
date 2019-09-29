# Zplot

Written in Python 3.7.4

Kit para trabalhar com RNGs, montar Z-score, Coletar dados e LivePlot

Raspberry Pi:
Além das bibliotecas normais, tb instalar: sudo apt-get install python-dev libatlas-base-dev
sudo apt-get install python3-pil.imagetk

Ubuntu:
sudo apt install python3-pip
sudo apt-get install python3-tk
sudo apt-get install python3-pil.imagetk
pip3 install bitstring
pip3 install pandas
pip3 install matplotlib
pip3 install xlsxwriter


To make executable with pyinstaller:
/usr/bin/python3 -m PyInstaller --hidden-import=PIL._tkinter_finder zplot.py

Then copy pictures to the Zplot folder and the bash scripts too (bbla mbbla rng)

Installation:
1- Open Terminal inside the RngKit Folder
2- Type: chmod 755 bbla mbbla rng rngkit
3- Double click rngkit or type in Terminal: ./rngkit
4- Wait a few seconds to open the app
