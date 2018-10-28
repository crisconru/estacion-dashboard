from tkinter import *
from tkinter import ttk, font
import getpass


# Gestor de geometría (place)
class Aplicacion():
    def __init__(self):
        self.raiz = Tk()

        # Define la dimensión de la ventana

        self.raiz.geometry("800x400")

        # Establece que no se pueda cambiar el tamaño de la
        # ventana

        self.raiz.resizable(0, 0)
        self.raiz.title("Acceso")
        self.fuente = font.Font(weight='bold')
        self.etiq1 = ttk.Label(self.raiz, text="Usuario:", font=self.fuente)
        self.etiq2 = ttk.Label(self.raiz, text="Contraseña:", font=self.fuente)

        # Declara una variable de cadena que se asigna a
        # la opción 'textvariable' de un widget 'Label' para
        # mostrar mensajes en la ventana. Se asigna el color
        # azul a la opción 'foreground' para el mensaje

        self.mensa = StringVar()
        self.etiq3 = ttk.Label(self.raiz, textvariable=self.mensa,
                               font=self.fuente, foreground='blue')

        self.usuario = StringVar()
        self.clave = StringVar()
        self.usuario.set(getpass.getuser())
        self.ctext1 = ttk.Entry(self.raiz, textvariable=self.usuario, width=30)
        self.ctext2 = ttk.Entry(self.raiz, textvariable=self.clave, width=30,
                                show="*")
        self.separ1 = ttk.Separator(self.raiz, orient=HORIZONTAL)
        self.boton1 = ttk.Button(self.raiz, text="Aceptar", padding=(5, 5),
                                 command=self.aceptar)
        self.boton2 = ttk.Button(self.raiz, text="Cancelar", padding=(5, 5),
                                 command=quit)

        # Se definen las ubicaciones de los widgets en la
        # ventana asignando los valores de las opciones 'x' e 'y'
        # en píxeles.

        self.etiq1.place(x=30, y=40)
        self.etiq2.place(x=30, y=80)
        self.etiq3.place(x=150, y=120)
        self.ctext1.place(x=150, y=42)
        self.ctext2.place(x=150, y=82)
        self.separ1.place(x=5, y=145, bordermode=OUTSIDE, height=10, width=420)
        self.boton1.place(x=170, y=160)
        self.boton2.place(x=290, y=160)
        self.ctext2.focus_set()

        # El método 'bind()' asocia el evento de 'hacer clic
        # con el botón izquierdo del ratón en la caja de entrada
        # de la contraseña' expresado con '<button-1>' con el
        # método 'self.borrar_mensa' que borra el mensaje y la
        # contraseña y devuelve el foco al mismo control.
        # Otros ejemplos de acciones que se pueden capturar:
        # <double-button-1>, <buttonrelease-1>, <enter>, <leave>,
        # <focusin>, <focusout>, <return>, <shift-up>, <key-f10>,
        # <key-space>, <key-print>, <keypress-h>, etc.

        self.ctext2.bind('<Button-1>', self.borrar_mensa,)
        self.raiz.mainloop()

    # Declara método para validar la contraseña y mostrar
    # un mensaje en la propia ventana, utilizando la etiqueta
    # 'self.mensa'. Cuando la contraseña es correcta se
    # asigna el color azul a la etiqueta 'self.etiq3' y
    # cuando es incorrecta el color rojo. Para ello. se emplea
    # el método 'configure()' que permite cambiar los valores
    # de las opciones de los widgets.

    def aceptar(self):
        if self.clave.get() == 'tkinter':
            self.etiq3.configure(foreground='blue')
            self.mensa.set("Acceso permitido")
        else:
            self.etiq3.configure(foreground='red')
            self.mensa.set("Acceso denegado")

    # Declara un método para borrar el mensaje anterior y
    # la caja de entrada de la contraseña

    def borrar_mensa(self, evento):
        self.clave.set("")
        self.mensa.set("")


def main():
    Aplicacion()
    return 0

if __name__ == '__main__':
    main()
