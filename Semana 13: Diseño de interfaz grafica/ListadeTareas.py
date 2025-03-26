import tkinter as tk
from tkinter import messagebox

def agregar_tarea():
    tarea = entrada.get()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        entrada.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Ingresa una tarea para continua.")

def eliminar_tarea():
    try:
        seleccion = lista_tareas.curselection()[0]
        lista_tareas.delete(seleccion)
    except IndexError:
        messagebox.showwarning("Advertencia", "Seleccione una tarea para eliminar.")

def limpiar_lista():
    lista_tareas.delete(0, tk.END)


ventana = tk.Tk()
ventana.title("Lista de Tareas")
ventana.geometry("300x300")

tk.Label(ventana, text="Agrega una tarea:").pack(pady=5)
entrada = tk.Entry(ventana, width=40)
entrada.pack(pady=5)

# Botones
tk.Button(ventana, text="Agregar", command=agregar_tarea).pack(pady=5)
tk.Button(ventana, text="Eliminar", command=eliminar_tarea).pack(pady=5)
tk.Button(ventana, text="Borrar todo", command=limpiar_lista).pack(pady=5)

# Lista de tareas
lista_tareas = tk.Listbox(ventana, width=50, height=15)
lista_tareas.pack(pady=10)

# Ejecutar la aplicación
ventana.mainloop()
