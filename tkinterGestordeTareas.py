import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import PhotoImage

# Función para mover tareas entre listas
def move_task(source, target):
    selected_task = source.curselection()
    if selected_task:
        task = source.get(selected_task)
        source.delete(selected_task)
        target.insert(tk.END, task)
    else:
        messagebox.showwarning("Advertencia", "Por favor selecciona una tarea para mover.")

# Función para eliminar tareas
def delete_task(listbox):
    selected_task = listbox.curselection()
    if selected_task:
        listbox.delete(selected_task)
    else:
        messagebox.showwarning("Advertencia", "Por favor selecciona una tarea para eliminar.")

# Función para agregar tareas
def add_task():
    task = task_entry.get()
    if task.strip():
        pending_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "La tarea no puede estar vacía.")

# Función para editar una tarea seleccionada
def edit_task(listbox):
    selected_task = listbox.curselection()
    if selected_task:
        current_task = listbox.get(selected_task)
        new_task = simpledialog.askstring("Editar Tarea", "Modifica la tarea:", initialvalue=current_task)
        if new_task and new_task.strip():
            listbox.delete(selected_task)
            listbox.insert(selected_task, new_task)
    else:
        messagebox.showwarning("Advertencia", "Por favor selecciona una tarea para editar.")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Gestor de Tareas")
root.geometry("900x600")
root.minsize(700, 500)

# Configuración de colores
root.configure(bg="#f0f8ff")
section_bg_color = "#d6eaf8"
button_color = "#85c1e9"
font_color = "#154360"

# Cargar íconos
add_icon = PhotoImage(file="add.png")  # Usa un archivo .png para el botón "Agregar"
delete_icon = PhotoImage(file="delete.png")  # Archivo para el botón "Eliminar"
edit_icon = PhotoImage(file="edit.png")  # Archivo para el botón "Editar"

# Entrada para nuevas tareas
task_entry = tk.Entry(root, width=40, font=("Arial", 12))
task_entry.grid(row=0, column=0, padx=10, pady=10, sticky="we", columnspan=2)

add_button = tk.Button(root, text="Agregar",image=add_icon, compound="left", command=add_task, bg=button_color, fg="white", font=("Arial", 10, "bold"))
add_button.grid(row=0, column=2, padx=10, pady=10, sticky="e")

# Sección de tareas pendientes
tk.Label(root, text="Pendientes", font=("Courier", 14, "bold"), bg=section_bg_color).grid(row=1, column=0, pady=5)
pending_listbox = tk.Listbox(root, selectmode=tk.SINGLE, bg="#33ecff", font=("Arial", 12))
pending_listbox.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

# Sección de tareas en proceso
tk.Label(root, text="En Proceso", font=("Courier", 14, "bold"), bg=section_bg_color).grid(row=1, column=1, pady=5)
in_process_listbox = tk.Listbox(root, selectmode=tk.SINGLE, bg="#33ceff", font=("Arial", 12))
in_process_listbox.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

# Sección de tareas finalizadas
tk.Label(root, text="Finalizado", font=("Courier", 14, "bold"), bg=section_bg_color).grid(row=1, column=2, pady=5)
completed_listbox = tk.Listbox(root, selectmode=tk.SINGLE, bg="#339fff", font=("Arial", 12))
completed_listbox.grid(row=2, column=2, padx=10, pady=10, sticky="nsew")

# Botones para mover tareas
move_to_process_button = tk.Button(root, text="Mover a 'En Proceso'", command=lambda: move_task(pending_listbox, in_process_listbox), bg=button_color, fg="white", font=("Arial", 10, "bold"))
move_to_process_button.grid(row=3, column=0, padx=10, pady=10, sticky="we")

move_to_completed_button = tk.Button(root, text="Mover a 'Finalizado'", command=lambda: move_task(in_process_listbox, completed_listbox), bg=button_color, fg="white", font=("Arial", 10, "bold"))
move_to_completed_button.grid(row=3, column=1, padx=10, pady=10, sticky="we")

# Botones para eliminar tareas
delete_pending_button = tk.Button(root, text="Eliminar", image=delete_icon, compound="left", command=lambda: delete_task(pending_listbox), bg=button_color, fg="white", font=("Arial", 10, "bold"))
delete_pending_button.grid(row=4, column=0, padx=10, pady=10, sticky="we")

delete_process_button = tk.Button(root, text="Eliminar", image=delete_icon, compound="left", command=lambda: delete_task(in_process_listbox), bg=button_color, fg="white", font=("Arial", 10, "bold"))
delete_process_button.grid(row=4, column=1, padx=10, pady=10, sticky="we")

delete_completed_button = tk.Button(root, text="Eliminar", image=delete_icon, compound="left", command=lambda: delete_task(completed_listbox), bg=button_color, fg="white", font=("Arial", 10, "bold"))
delete_completed_button.grid(row=4, column=2, padx=10, pady=10, sticky="we")

# Botones para editar tareas
edit_pending_button = tk.Button(root, text="Editar", image=edit_icon, compound="left", command=lambda: edit_task(pending_listbox), bg=button_color, fg="white", font=("Arial", 10, "bold"))
edit_pending_button.grid(row=5, column=0, padx=10, pady=10, sticky="we")

edit_process_button = tk.Button(root, text="Editar", image=edit_icon, compound="left", command=lambda: edit_task(in_process_listbox), bg=button_color, fg="white", font=("Arial", 10, "bold"))
edit_process_button.grid(row=5, column=1, padx=10, pady=10, sticky="we")

edit_completed_button = tk.Button(root, text="Editar", image=edit_icon,  compound="left", command=lambda: edit_task(completed_listbox), bg=button_color, fg="white", font=("Arial", 10, "bold"))
edit_completed_button.grid(row=5, column=2, padx=10, pady=10, sticky="we")

# Configuración adicional para la adaptabilidad
for col in range(3):
    root.grid_columnconfigure(col, weight=1)
root.grid_rowconfigure(2, weight=1)

# Ejecutar la aplicación
root.mainloop()
