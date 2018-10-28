from tkinter import *
from tkinter import ttk, font
import getpass


class Aplicacion():
    def __init__(self):
        self.raiz = Tk()
        self.raiz.title("Acceso")
        self.raiz.resizable(0, 0)
        fuente = font.Font(weight='bold')

        # Define un widget de tipo 'Frame' (marco) que será el
        # contenedor del resto de widgets. El marco se situará
        # en la ventana 'self.raiz' ocupando toda su extensión.
        # El marco se define con un borde de 2 píxeles y la
        # opción 'relief' con el valor 'raised' (elevado) añade
        # un efecto 3D a su borde.
        # La opción 'relief' permite los siguientes valores:
        # FLAT (llano), RAISED (elevado), SUNKEN (hundido),
        # GROOVE (hendidura) y RIDGE (borde elevado).
        # La opción 'padding' añade espacio extra interior para
        # que los widgets no queden pegados al borde del marco.

        self.marco = ttk.Frame(self.raiz, borderwidth=2, relief="raised",
                               padding=(10, 10))
        self.etiq1 = ttk.Label(self.marco, text="Usuario:", font=fuente,
                               padding=(5, 5))
        self.etiq2 = ttk.Label(self.marco, text="Contraseña:", font=fuente,
                               padding=(5, 5))

        # Define variables para las opciones 'textvariable' de
        # cada caja de entrada 'ttk.Entry()'.

        self.usuario = StringVar()
        self.clave = StringVar()
        self.usuario.set(getpass.getuser())
        self.ctext1 = ttk.Entry(self.marco, textvariable=self.usuario,
                                width=30)
        self.ctext2 = ttk.Entry(self.marco, textvariable=self.clave, show="*",
                                width=30)
        self.separ1 = ttk.Separator(self.marco, orient=HORIZONTAL)
        self.boton1 = ttk.Button(self.marco, text="Aceptar", padding=(5, 5),
                                 command=self.aceptar)
        self.boton2 = ttk.Button(self.marco, text="Cancelar", padding=(5, 5),
                                 command=quit)

        # Define la ubicación de cada widget en el grid.
        # En este ejemplo en realidad hay dos grid (cuadrículas):
        # Una cuadrícula de 1fx1c que se encuentra en la ventana
        # que ocupará el Frame; y otra en el Frame de 5fx3c para
        # el resto de controles.
        # La primera fila y primera columna serán la número 0.
        # La opción 'column' indica el número de columna y la
        # opción 'row' indica el número de fila donde hay que
        # colocar un widget.
        # La opción 'columnspan' indica al gestor que el
        # widget ocupará en total un número determinado de
        # columnas. Las cajas para entradas 'self.ctext1' y
        # 'self.ctext2' ocuparán dos columnas y la barra
        # de separación 'self.separ1' tres.

        self.marco.grid(row=0, column=0)
        self.etiq1.grid(row=0, column=0)
        self.ctext1.grid(row=0, column=1, columnspan=2)
        self.etiq2.grid(row=1, column=0, )
        self.ctext2.grid(row=1, column=1, columnspan=2)
        self.separ1.grid(row=3, column=0, columnspan=3)
        self.boton1.grid(row=4, column=1)
        self.boton2.grid(row=4, column=2)

        # Establece el foco en la caja de entrada de la
        # contraseña.

        self.ctext2.focus_set()
        self.raiz.mainloop()

    def aceptar(self):
        if self.clave.get() == 'tkinter':
            print("Acceso permitido\n"
                  f"Usuario: {self.ctext1.get()}\n"
                  f"Contraseña: {self.ctext2.get()}")
        else:
            print("Acceso denegado")
            self.clave.set("")
            self.ctext2.focus_set()


def main():
    Aplicacion()
    return 0

if __name__ == '__main__':
    main()
