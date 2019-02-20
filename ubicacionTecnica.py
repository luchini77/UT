from tkinter import *
from tkinter import messagebox
import sqlite3

# FUNCIONES

def conexionBBDD():

    conexion=sqlite3.connect("Ubicaciones Tecnicas")

    cursor=conexion.cursor()

    try:

        cursor.execute('''
            CREATE TABLE ubicaciones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            buzon VARCHAR(50),
            ubicacion VARCHAR(50))
            ''')

        messagebox.showinfo("BBDD", "BBDD creada con éxito.")

    except:

        messagebox.showwarning("Atencion!!", "La BBDD ya existe.")


def salirAplicacion():

    valor=messagebox.askquestion("Salir", "Deseas salir de la aplicacion?")

    if valor == "yes":
        raiz.destroy()


def borrarCampos():

    nBuzon.set("")
    nUbicacion.set("")

    txtBuzon.focus()


def insertar():

    conexion=sqlite3.connect("Ubicaciones Tecnicas")

    cursor=conexion.cursor()


    datos=nBuzon.get(),nUbicacion.get()

    cursor.execute("INSERT INTO ubicaciones VALUES (NULL,?,?)",(datos))

    conexion.commit()

    messagebox.showinfo("BBDD", "Registro insertado con exito.")




def leer():

    conexion=sqlite3.connect("Ubicaciones Tecnicas")

    cursor=conexion.cursor()

    b=nBuzon.get()

    elBuzon=cursor.execute(f"SELECT * FROM ubicaciones WHERE buzon='{b}'").fetchall()



    for bzn in elBuzon:

        nId.set(bzn[0])
        nBuzon.set(bzn[1])
        nUbicacion.set(bzn[2])

    conexion.commit()


def actualizar():

    conexion=sqlite3.connect("Ubicaciones Tecnicas")

    cursor=conexion.cursor()

    try:

        datos=nBuzon.get(),nUbicacion.get()

        cursor.execute("UPDATE ubicaciones SET buzon=?, ubicacion=?")

        conexion.commit()

        messagebox.showinfo("BBDD", "La BBDD fue actualizada con exito." + "WHERE buzon=" + nBuzon.get(),(datos))

    except:

        messagebox.showwarning("BBDD", "No se pudo actualizar la BBDD.")


def eliminar():

    conexion=sqlite3.connect("Ubicaciones Tecnicas")

    cursor=conexion.cursor()

    try:
        cursor.execute("DELETE FROM ubicaciones WHERE buzon=" + nBuzon.get())

        conexion.commit()

        messagebox.showinfo("BBDD", "Fue borrado con exito.")

    except:

        messagebox.showwarning("BBDD", "No se pudo borrar.")



raiz=Tk()
raiz.title("Ubicaciones")

barraMenu=Menu(raiz)
raiz.config(menu=barraMenu, width=300, height=300)

bbddMenu=Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=conexionBBDD)
bbddMenu.add_command(label="Salir", command=salirAplicacion)

borrarMenu=Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos", command=borrarCampos)

ayudaMenu=Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Acerca de...")

barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

# COMIENZO DE campos

frame=Frame(raiz)
frame.pack()

nId=IntVar()
nBuzon=StringVar()
nUbicacion=StringVar()

lblBuzon=Label(frame, text="N° Buzon")
lblBuzon.grid(row=0, column=0, padx=10, pady=10)

txtBuzon=Entry(frame, textvariable=nBuzon)
txtBuzon.grid(row=1, column=0, padx=10, pady=10)
txtBuzon.config(justify="center")
txtBuzon.focus()

lblUbicacion=Label(frame, text="Ubicacion Tecnica")
lblUbicacion.grid(row=0, column=1, padx=10, pady=10)

txtUbicacion=Entry(frame, textvariable=nUbicacion)
txtUbicacion.grid(row=1, column=1, padx=10, pady=10)
txtUbicacion.config(justify="center")


# AQUI COMIENZAN LOD BOTONES

frame1=Frame(raiz)
frame1.pack()

btnCrear=Button(frame1, text="Insertar", command=insertar)
btnCrear.grid(row=0, column=0, padx=10, pady=10)

btnLeer=Button(frame1, text="Consultar", command=leer)
btnLeer.grid(row=0, column=1, padx=10, pady=10)

btnActualizar=Button(frame1, text="Actualizar", command=actualizar)
btnActualizar.grid(row=0, column=2, padx=10,pady=10)

btnBorrar=Button(frame1, text="Borrar", command=eliminar)
btnBorrar.grid(row=0, column=3, padx=10, pady=10)





raiz.mainloop()
