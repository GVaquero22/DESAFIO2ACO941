
# INTEGRANTES #

#ESAÚ CRUZ
#ALEJANDRO CAMPOS
#GERARDO CABEZAS

# Librerias #
# Thinter para entorno gráfico #
import tkinter as tk
from tkinter import simpledialog, messagebox
import subprocess
import os


# validamos script de configuración #
def open_config():
    if os.path.exists("config.py"):
        subprocess.run(["python", "config.py"])
    else:
        messagebox.showerror("Error", "El script de configuración no existe")


# Abrimos los script de cifrado y descifrado #
def open_cifrar():
    subprocess.run(["python", "cifrar.py"])

def open_descifrar():
    subprocess.run(["python", "descifrar.py"])


