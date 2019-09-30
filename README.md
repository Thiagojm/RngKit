# RngKit
Thiagojm  
tjm.plastica@gmail.com    
Written in Python 3.7.4  
-----------------------

# ABSTRACT

This project represents my puttering around with hardware entropy sources and
random number generation in Linux/GNU, to help to our project of mind matter interaction.    

Kit for working with TRNGs (True Random Number Generators), creating Z-score tables, acquiring data and LivePlot!    

# Installation  

Raspberry Pi:
In addition to the normal libraries, also install:  
sudo apt-get install python-dev   
sudo apt-get install libatlas-base-dev  
sudo apt-get install python3-pil.imagetk

Ubuntu:
sudo apt install python3-pip  
sudo apt-get install python3-tk  
sudo apt-get install python3-pil.imagetk  
pip3 install bitstring  
pip3 install pandas  
pip3 install matplotlib  
pip3 install xlsxwriter    

1- Open Terminal inside the RngKit Folder  
2- Type: chmod 755 bbla mbbla rng rngkit.py  
3- Open a Terminal inside RngKit folder and type: "./rngkit.py" or "python3 rngkit.py" (without the "")    

# PyInstaller  

To make executable with pyinstaller:
/usr/bin/python3 -m PyInstaller --hidden-import=PIL._tkinter_finder zplot.py  

Then copy the pictures to the RngKit folder and the bash scripts (bbla, mbbla, rng)  
