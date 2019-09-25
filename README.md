# Zplot

Kit para trabalhar com RNGs, montar Z-score, Coletar dados e LivePlot

No raspberry pi além das bibliotecas normais, tb instalar: sudo apt-get install python-dev libatlas-base-dev
sudo apt-get install python3-pil.imagetk

To make executable with pyinstaller:
/usr/bin/python3 -m PyInstaller --hidden-import=PIL._tkinter_finder zplot.py

Then copy pictures to the Zplot folder and the bash scripts too (bbla mbbla rng)

Installation:
1- Open Terminal inside the RngKit Folder
2- Type: chmod 755 bbla mbbla rng rngkit
3- Double click rngkit or type in Terminal: ./rngkit
4- Wait a few seconds to open the app
