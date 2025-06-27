import tkinter as tk
import requests

def obtener_usuarios():
    response = requests.get("http://localhost:3000/api/usuarios")
    usuarios = response.json()
    salida.delete("1.0", tk.END)
    for u in usuarios:
        salida.insert(tk.END, f"Nombre: {u['nombre']}, Correo: {u['correo']}\n")

app = tk.Tk()
app.title("Usuarios Registrados")

boton = tk.Button(app, text="Cargar Usuarios", command=obtener_usuarios)
boton.pack()

salida = tk.Text(app)
salida.pack()

app.mainloop()