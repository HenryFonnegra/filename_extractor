# 📌 Proyecto: Buscador de Archivos con Interfaz Gráfica

## 📖 Descripción  
Este proyecto es una herramienta desarrollada en **Python** que permite buscar archivos en un directorio dado a partir de una palabra clave.  
Incluye una **interfaz gráfica con Tkinter** que facilita la interacción con el usuario.  
La aplicación muestra los resultados en una lista y ofrece opciones para **copiar archivos seleccionados** o **copiar todos los resultados automáticamente** a una carpeta de destino.

---

## ⚙️ Requisitos  

- **Python 3.8+**  
- Librerías estándar de Python:  
  - `os`  
  - `shutil`  
  - `tkinter`  

No requiere dependencias externas adicionales.

---

## 🚀 Instalación  

1. Clona este repositorio:  
   ```bash
   git clone https://github.com/HenryFonnegra/filename_extractor.git
   cd repositorio

Ejecuta el programa directamente con Python:

python main.py

🖥️ Uso

Al iniciar el programa, se abrirá una ventana principal con los siguientes campos:

Directorio de búsqueda (se puede escribir la ruta o seleccionar con explorador).

Palabra clave a buscar en los nombres de archivos.

Directorio de destino donde se copiarán los archivos seleccionados.

Botón Buscar → Ejecuta la búsqueda en el directorio indicado.

En la ventana de resultados:

Se listan los archivos encontrados.

Botón Copiar seleccionados → Copia únicamente los elementos marcados.

Botón Copiar todos → Copia automáticamente todos los archivos listados.

📂 Estructura del Proyecto
📦 repositorio
 ┣ 📜 main.py           # Script principal con la lógica y GUI
 ┣ 📜 README.md         # Documentación del proyecto
 ┗ 📂 docs              # (opcional) Documentación adicional

🔧 Funcionamiento Interno

Búsqueda: Se recorre el directorio de manera recursiva con os.walk().

Interfaz gráfica: Implementada con Tkinter:

Tk, Label, Entry, Button, Listbox, Scrollbar.

Copia de archivos: Se realiza con shutil.copy().

Gestión de selección: La Listbox permite seleccionar múltiples elementos.

📌 Próximas mejoras (To-Do List)

 Agregar filtros por extensión de archivo.

 Implementar barra de progreso para la copia de archivos.

 Soporte para múltiples palabras clave.

 Exportar listado de resultados a .csv.

🧑‍💻 Autor

Proyecto desarrollado por HenryFonnegra
📧 Contacto: henferfon@gmail.com