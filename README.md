# Zplot

Kit para trabalhar com RNGs, montar Z-score, Coletar dados e LivePlot

No raspberry pi além das bibliotecas normais, tb instalar: sudo apt-get install python-dev libatlas-base-dev
sudo apt-get install python3-pil.imagetk

To make executable:
/usr/bin/python3 -m PyInstaller --hidden-import=PIL._tkinter_finder zplot.py

then copy pictures to the Zplot folder and the bash scripts too
