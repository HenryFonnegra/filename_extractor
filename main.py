import os
import tkinter as tk
from tkinter import filedialog, messagebox

def seleccionar_carpeta():
    """Permite seleccionar la carpeta y guarda la ruta en la variable global."""
    folder = filedialog.askdirectory()
    if folder:
        carpeta_var.set(os.path.basename(folder))
        ruta_var.set(folder)
        btn_buscar.config(state="normal")  # Habilitar botón buscar
    else:
        carpeta_var.set("(ninguna seleccionada)")
        ruta_var.set("")
        btn_buscar.config(state="disabled")  # Deshabilitar si no hay carpeta


def analizar_carpeta():
    """Analiza la carpeta seleccionada y crea botones de extensiones."""
    folder = ruta_var.get()
    if not folder or not os.path.isdir(folder):
        messagebox.showerror("Error", "Seleccione una carpeta válida antes de buscar.")
        return

    # Listar archivos
    files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    extensions = sorted({os.path.splitext(f)[1] for f in files if os.path.splitext(f)[1]})

    # Limpiar botones anteriores
    for widget in frame_extensiones.winfo_children():
        widget.destroy()

    if not files:
        messagebox.showinfo("Sin archivos", "La carpeta no contiene archivos.")
        return

    if not extensions:
        messagebox.showinfo("Sin extensiones", "La carpeta no contiene archivos con extensiones reconocibles.")
        return

    # Crear botones dinámicos
    for ext in extensions:
        btn = tk.Button(frame_extensiones, text=ext, width=5, 
                        command=lambda e=ext: mostrar_archivos(folder, e))
        btn.pack(side="left", padx=5, pady=5)


def mostrar_archivos(folder, extension):
    """Muestra en una nueva ventana los archivos con la extensión seleccionada."""
    files = [f for f in os.listdir(folder) if f.endswith(extension)]

    if not files:
        messagebox.showwarning("Vacío", f"No se encontraron archivos con {extension}")
        return

    # Nueva ventana (independiente de la principal)
    win = tk.Toplevel(root)
    win.title(f"Archivos {extension}")
    win.geometry("400x350")

    # Cuadro de lista con scrollbar
    scrollbar = tk.Scrollbar(win)
    scrollbar.pack(side="right", fill="y")

    listbox = tk.Listbox(win, selectmode="extended", yscrollcommand=scrollbar.set)
    for file in files:
        listbox.insert(tk.END, file)
    listbox.pack(expand=True, fill="both", padx=10, pady=10)

    scrollbar.config(command=listbox.yview)

    # --- Funciones de copiado ---
    def copiar_seleccion():
        seleccion = listbox.curselection()
        if not seleccion:
            messagebox.showwarning("Sin selección", "Seleccione al menos un archivo.")
            return
        nombres = "\n".join([listbox.get(i) for i in seleccion])
        root.clipboard_clear()
        root.clipboard_append(nombres)
        messagebox.showinfo("Copiado", "Los nombres seleccionados fueron copiados al portapapeles.")

    def copiar_todo():
        nombres = "\n".join(files)
        root.clipboard_clear()
        root.clipboard_append(nombres)
        messagebox.showinfo("Copiado", "Todos los nombres de archivos fueron copiados al portapapeles.")

    # Frame para botones
    frame_botones = tk.Frame(win)
    frame_botones.pack(pady=5)

    btn_copiar_sel = tk.Button(frame_botones, text="Copiar selección", command=copiar_seleccion)
    btn_copiar_sel.pack(side="left", padx=5)

    btn_copiar_todo = tk.Button(frame_botones, text="Copiar todo", command=copiar_todo)
    btn_copiar_todo.pack(side="left", padx=5)



# --- Ventana principal ---
root = tk.Tk()
root.title("Filename Extractor")
root.geometry("400x250")

# Variables dinámicas
carpeta_var = tk.StringVar(value="(ninguna seleccionada)")
ruta_var = tk.StringVar(value="")

# Selección de carpeta
frame_top = tk.Frame(root)
frame_top.pack(pady=10)

btn_carpeta = tk.Button(frame_top, text="Seleccionar carpeta", command=seleccionar_carpeta)
btn_carpeta.pack(side="left", padx=10)

label_carpeta = tk.Label(frame_top, textvariable=carpeta_var, fg="blue")
label_carpeta.pack(side="left")

# Botón buscar (deshabilitado hasta seleccionar carpeta)
btn_buscar = tk.Button(root, text="Buscar", command=analizar_carpeta, state="disabled")
btn_buscar.pack(pady=10)

# Frame para botones de extensiones
frame_extensiones = tk.Frame(root)
frame_extensiones.pack(pady=20)

root.mainloop()
