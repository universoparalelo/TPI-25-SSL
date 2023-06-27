from tkinter import *
from tkinter import ttk
from tkinter import filedialog

def submitFile():
    # Abrir el diálogo de selección de archivo
    archivo = filedialog.askopenfilename()
    
    # Mostrar el nombre del archivo seleccionado en la etiqueta
    print(archivo)

def submitText():
    pass

root = Tk()
root.title("PARSING DOCBOOK")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

title = ttk.Label(mainframe, text="Bienvenido! Quieres escribir un codigo xml o buscar un archivo?").grid(column=1, row=1, columnspan=4)

button1 = ttk.Button(mainframe, text="File", command=submitFile).grid(column=2, row=2, sticky=E)
button2 = ttk.Button(mainframe, text="Write", command=submitText).grid(column=3, row=2, sticky=W)

root.mainloop()

