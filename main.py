
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


# Crea y establece el valor por defecto a 3 en el archivo de cifrado si no existe #
def create_config_file():
    config_file = "config.cfg"
    if not os.path.exists(config_file):
        with open(config_file, "w") as file:
            file.write("cesar = 3\n")
        messagebox.showinfo("Configuración creada", "Archivo de configuración de cifrado creado.")


# Funcion principal y aspecto gráfico #
def main_window():
    root = tk.Tk()
    root.iconbitmap('icono.png')
    root.geometry("475x350")
    logo_image = tk.PhotoImage(file='cifrado.png')
    logo_image = logo_image.subsample(2, 2)
    logo_label = tk.Label(root, image=logo_image)
    logo_label.image = logo_image
    logo_label.pack(pady=15)
    root.title("Menú Principal - Cifrado Caesar")
 
    cesar_label = tk.Label(root,  font='Helvetica 18 bold' ,text='Cifrado César')
    cesar_label.pack(pady=10)

# Cifrar
    cifrar_button = tk.Button(root, text="Cifrar", height=1, width=20, command=open_cifrar)
    cifrar_button.pack(pady=10)

# Descifrar
    descifrar_button = tk.Button(root, text="Descifrar", height=1, width=20, command=open_descifrar)
    descifrar_button.pack(pady=10)

    root.mainloop()


# Funciones principales #
if __name__ == "__main__":
    create_config_file()
    main_window()
