# Librerias #
# Thinter para entorno gráfico #

import tkinter as tk
from tkinter import Entry, filedialog, messagebox, simpledialog
import os
import base64

# Parámetro de cifrado #
def cesar_key():
    try:
        with open("config.cfg", "r") as file:
            for line in file:
                if line.startswith("cesar"):
                    _, value = line.split("=")
                    return int(value.strip())
    except FileNotFoundError:
        messagebox.showerror("Error", "Archivo de configuración no encontrado.")
        return 0

# Funcion principal #
def cifrar_cesar(texto, desplazamiento):
    resultado = ""
    for caracter in texto:
        if caracter.isalpha():
            ascii_offset = 65 if caracter.isupper() else 97
            resultado += chr((ord(caracter) - ascii_offset + desplazamiento) % 26 + ascii_offset)
        else:
            resultado += caracter
    return resultado

# Conversión a binario #
def to_binario(text):
    return ' '.join(format(ord(char), '08b') for char in text)

# Conversión a hexadecimal #
def to_hexadecimal(text):
    return ' '.join(format(ord(char), '02x') for char in text)

# Conversión a Base64 #
def to_base64(text):
   return base64.b64encode(text.encode()).decode()

# Almacenamiento en archivo (ASCII, BIN, HEXADECIMAL) #
def save_message(ascii, binary, hexa, b64):
    with open("archivo.db", "w") as file:
        file.write(f"Cesar-ASCII:\"{ascii}\";\n")
        file.write(f"Cesar-BIN:\"{binary}\";\n")
        file.write(f"Cesar-HEXADECIMAL:\"{hexa}\";\n")
        file.write(f"Cesar-Base64:\"{b64}\";\n")

# Mostrar las conversiones #
def process_message():
    desplazamiento = cesar_key()
    mensaje = message_entry.get()
    if mensaje:
        mensaje_cifrado = cifrar_cesar(mensaje, desplazamiento)
        mensaje_binario = to_binario(mensaje_cifrado)
        mensaje_hexadecimal = to_hexadecimal(mensaje_cifrado)
        mensaje_base64 = to_base64(mensaje_cifrado)

        save_message(mensaje_cifrado, mensaje_binario, mensaje_hexadecimal, mensaje_base64)
        #ascii_text.config(state=tk.NORMAL)
        #ascii_text.delete("1.0", tk.END)
        #ascii_text.insert(tk.END, mensaje_cifrado)
        #ascii_text.config(state=tk.DISABLED)
        ascii_text_label.config(text=f"ASCII: {mensaje_cifrado}")
        binary_label.config(text=f"Binario: {mensaje_binario}")
        hex_label.config(text=f"Hexadecimal: {mensaje_hexadecimal}")
        base64_label.config(text=f"Base64: {mensaje_base64}")

# Verificamos si mensaje.db existe #
def mensaje_db_exists():
    return os.path.exists("archivo.db")

# Guardamos el mensaje cifrado #
def save_encrypted():
    source_file = "archivo.db"

    # Solicitar ubicación y el nombre del archivo de destino #
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", 
                                             filetypes=[("Text files", "*.txt")])
    if file_path:
        try:
            # Read contenido de mensaje.db #
            with open(source_file, "rb") as file:
                content = file.read()

            # Guardar el contenido #
            with open(file_path, "w") as file:
                file.write(content.decode("utf-8"))

            messagebox.showinfo("Guardado", "La copia del mensaje cifrado ha sido guardado.")
        except Exception as e:
            messagebox.showerror("Error", f"Ha ocurrido un error al guardar el archivo: {e}")


# Proceso principal de cifrado #
def cifrar_windows():
    global message_entry, binary_label, hex_label, ascii_text_label, base64_label

    root = tk.Tk()
    root.geometry('475x350') 
    root.iconbitmap('icono.png')
    root.title("Cifrado")

    # primera funcion # 
    label = tk.Label(root, text="INGRESE EL MENSAJE A CIFRAR:")
    label.pack(pady=5)

    # Entrada de mensaje a cifrar #
    message_entry = Entry(root, width=50)
    message_entry.pack(pady=10)

    # Cifrado #
    cifrado_button = tk.Button(root, text="CIFRAR MENSAJE", command=process_message)
    cifrado_button.pack(pady=10)

    # ASCII #
    #ascii_label = tk.Label(root, text="ASCII: ", wraplength=500)
    #ascii_label.pack(pady=5)
    
    # ASCII #
    ascii_text_label = tk.Label(root, text="ASCII: ", wraplength=500)
    ascii_text_label.pack(pady=5)


    # Mensaje en ASCII #
    #ascii_text = tk.Text(root, height=3, width=30)
    #ascii_text.pack(pady=5)
    #scii_text.config(state=tk.DISABLED)

    # Mensaje en Binario #
    binary_label = tk.Label(root, text="BINARIO: ", wraplength=500)
    binary_label.pack(pady=5)

    # Mensaje en hexadecimal #
    hex_label = tk.Label(root, text="HEXADECIMAL: ", wraplength=500)
    hex_label.pack(pady=5)

    # Mensaje en base64 #
    base64_label = tk.Label(root, text="BASE64: ", wraplength=500)
    base64_label.pack(pady=5)

    # Botón de guardar #
    save_button = tk.Button(root, text="💾", command=save_encrypted)
    save_button.pack(pady=10)

    # Botón solo si mensaje.db existe #
    save_button['state'] = 'normal' if mensaje_db_exists() else 'disabled'

    root.mainloop()


# Cambio de parámetro de cifrado #
def change_cesar():
    new_value_message = f" Ingrese el nuevo valor de desplazamiento para César [0-25], esto es necesario para descifrar el mensaje:"
    new_value = simpledialog.askinteger("Valor de César", new_value_message, minvalue=0, maxvalue=25)
    if new_value is not None:
        with open("config.cfg", "w") as file:
            file.write(f"cesar = {new_value}\n")
        cifrar_windows()

# Funciones principales #
if __name__ == "__main__":
    change_cesar()
