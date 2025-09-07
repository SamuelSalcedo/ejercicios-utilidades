import tkinter as tk

from tkinter import ttk, messagebox

#inicilaizar la vista general que tendra el proyecto
root = tk.Tk()
root.title("Seguimiento de Gastos!")

#agregar estilo
root.tk.call('source', 'forest-dark.tcl')
ttk.Style().theme_use('forest-dark')
root.option_add("*tearOff", False) # This is always a good idea

#tamanio de la ventana
root.geometry("950x600")


#Hacer la app responsiva
root.columnconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=1)
root.columnconfigure(index=2, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=1)
root.rowconfigure(index=2, weight=1)

#primer utilidad 
#el notebook delimita el contenido
# Notebook
notebook = ttk.Notebook(root)

"""

# CONTENIDO DEL TAB #1

"""

tab_1 = ttk.Frame(notebook)
notebook.add(tab_1, text="Pagina 1")

entry = ttk.Entry(tab_1)
entry.insert(0,"")
entry.grid(row=0, column=0, padx=5, pady=(0, 10), sticky="ew")

notebook.pack(expand=True, fill="both", padx=25, pady=25)


#Hacer que aparezca en el centro
root.update()
root.minsize(root.winfo_width(), root.winfo_height())
x_cordinate = int((root.winfo_screenwidth()/4) - (root.winfo_width()/3))
y_cordinate = int((root.winfo_screenheight()/3) - (root.winfo_height()/4))
root.geometry("+{}+{}".format(x_cordinate, y_cordinate))


root.mainloop()