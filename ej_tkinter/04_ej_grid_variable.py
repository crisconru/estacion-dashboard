from tkinter import *
from tkinter import ttk, font
import getpass

# Gestor de geometría (grid). Ventana dimensionable


class Aplicacion():
    def __init__(self):
        self.raiz = Tk()
        self.raiz.title("Acceso")
        fuente = font.Font(weight='bold')
        self.marco = ttk.Frame(self.raiz, borderwidth=2,
                               relief="raised", padding=(10, 10))
        self.etiq1 = ttk.Label(self.marco, text="Usuario:", font=fuente,
                               padding=(5, 5))
        self.etiq2 = ttk.Label(self.marco, text="Contraseña:", font=fuente,
                               padding=(5, 5))
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

        # Para conseguir que la cuadricula y los widgets se
        # adapten al contenedor, si se amplia o reduce el tamaño
        # de la ventana, es necesario definir la opción 'sticky'.
        # Cuando un widget se ubica en el grid se coloca en el
        # centro de su celda o cuadro. Con 'sticky' se
        # establece el comportamiendo 'pegajoso' que tendrá el
        # widget dentro de su celda, cuando se modifique la
        # dimensión de la ventana. Para ello, se utilizan para
        # expresar sus valores los puntos cardinales: N (Norte),
        # S (Sur), (E) Este y (W) Oeste, que incluso se pueden
        # utilizar de forma combinada. El widget se quedará
        # 'pegado' a los lados de su celda en las direcciones
        # que se indiquen. cuando la ventana cambie de tamaño.
        # Pero con definir la opción 'sticky' no es suficiente:
        # hay activar esta propiedad más adelante.

        self.marco.grid(row=0, column=0, padx=5, pady=5, sticky=(N, S, E, W))
        self.etiq1.grid(row=0, column=0, sticky=(N, S, E, W))
        self.ctext1.grid(row=0, column=1, columnspan=2, sticky=(E, W))
        self.etiq2.grid(row=1, column=0, sticky=(N, S, E, W))
        self.ctext2.grid(row=1, column=1, columnspan=2, sticky=(E, W))
        self.separ1.grid(row=3, column=0, columnspan=3, pady=5,
                         sticky=(N, S, E, W))
        self.boton1.grid(row=4, column=1, padx=5, sticky=(E))
        self.boton2.grid(row=4, column=2, padx=5, sticky=(W))

        # A continuación, se activa la propiedad de expandirse
        # o contraerse definida antes con la opción
        # 'sticky' del método grid().
        # La activación se hace por contenedores y por filas
        # y columnas asignando un peso a la opción 'weight'.
        # Esta opción asigna un peso (relativo) que se utiliza
        # para distribuir el espacio adicional entre columnas
        # y/o filas. Cuando se expanda la ventana, una columna
        # o fila con un peso 2 crecerá dos veces más rápido
        # que una columna (o fila) con peso 1. El valor
        # predeterminado es 0 que significa que la columna o
        # o fila no crecerá nada en absoluto.
        # Lo habitual es asignar pesos a filas o columnas donde
        # hay celdas con widgets.

        self.raiz.columnconfigure(0, weight=1)
        self.raiz.rowconfigure(0, weight=1)
        self.marco.columnconfigure(0, weight=1)
        self.marco.columnconfigure(1, weight=1)
        self.marco.columnconfigure(2, weight=1)
        self.marco.rowconfigure(0, weight=1)
        self.marco.rowconfigure(1, weight=1)
        self.marco.rowconfigure(4, weight=1)

        # Establece el foco en la caja de entrada de la
        # contraseña.

        self.ctext2.focus_set()
        self.raiz.mainloop()

    def aceptar(self):
        if self.clave.get() == 'tkinter':
            print("Acceso permitido")
            print("Usuario:   ", self.ctext1.get())
            print("Contraseña:", self.ctext2.get())
        else:
            print("Acceso denegado")
            self.clave.set("")
            self.ctext2.focus_set()


def main():
    Aplicacion()
    return 0

if __name__ == '__main__':
    main()
