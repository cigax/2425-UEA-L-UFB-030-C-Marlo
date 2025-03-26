import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry


def agregar_evento():
    fecha = entrada_fecha.get()
    hora = entrada_hora.get()
    descripcion = entrada_descripcion.get()

    if fecha and hora and descripcion:
        tree.insert("", tk.END, values=(fecha, hora, descripcion))
        entrada_fecha.set_date('')
        entrada_hora.delete(0, tk.END)
        entrada_descripcion.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Completa todos los campos para guardar.")


def eliminar_evento():
    try:
        seleccion = tree.selection()[0]
        if messagebox.askyesno("Advertencia", "¿Seguro que desea eliminar este evento?"):
            tree.delete(seleccion)
    except IndexError:
        messagebox.showwarning("Advertencia", "Seleccione un evento para eliminar.")


def salir():
    ventana.quit()


#Menu principal GUI
ventana = tk.Tk()
ventana.title("Agenda Personal")
ventana.geometry("500x400")

# Frame recopila todos los datos que son puestos
frame_entrada = tk.Frame(ventana)
frame_entrada.pack(pady=10)

tk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
entrada_fecha = DateEntry(frame_entrada, width=12, background='darkblue', foreground='white', borderwidth=2)
entrada_fecha.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_entrada, text="Hora:").grid(row=1, column=0, padx=5, pady=5)
entrada_hora = tk.Entry(frame_entrada, width=15)
entrada_hora.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_entrada, text="Descripción:").grid(row=2, column=0, padx=5, pady=5)
entrada_descripcion = tk.Entry(frame_entrada, width=30)
entrada_descripcion.grid(row=2, column=1, padx=5, pady=5)

# Frame de cada boton
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento).grid(row=0, column=0, padx=5)
tk.Button(frame_botones, text="Eliminar Evento", command=eliminar_evento).grid(row=0, column=1, padx=5)
tk.Button(frame_botones, text="Salir", command=salir).grid(row=0, column=2, padx=5)

# Frame de la lista de eventos
frame_lista = tk.Frame(ventana)
frame_lista.pack(pady=10)

tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción")
tree.pack()

ventana.mainloop()
