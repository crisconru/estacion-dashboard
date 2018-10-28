from tkinter import *
from tkinter import ttk


class Aplicacion():
    ventana = 0
    posx_y = 0

    def __init__(self):
        self.raiz = Tk()
        self.raiz.geometry('500x300+500+50')
        self.raiz.resizable(0, 0)
        self.raiz.title("Ventana de aplicación")
        boton = ttk.Button(self.raiz, text='Abrir', command=self.abrir)
        boton.pack(side=BOTTOM, padx=20, pady=20)
        self.raiz.mainloop()

    def abrir(self):
        ''' Construye una ventana de diálogo '''
        self.dialogo = Toplevel()
        Aplicacion.ventana += 1
        Aplicacion.posx_y += 50
        tamypos = f'400x200+{Aplicacion.posx_y}+{Aplicacion.posx_y}'
        self.dialogo.geometry(tamypos)
        self.dialogo.resizable(0, 0)
        ident = self.dialogo.winfo_id()
        titulo = f'{Aplicacion.ventana}: {ident}'
        self.dialogo.title(titulo)
        boton = ttk.Button(self.dialogo, text='Cerrar',
                           command=self.dialogo.destroy)
        boton.pack(side=BOTTOM, padx=20, pady=20)
        # Convierte la ventana 'self.dialogo' en
        # transitoria con respecto a su ventana maestra
        # 'self.raiz'.
        # Una ventana transitoria siempre se dibuja sobre
        # su maestra y se ocultará cuando la maestra sea
        # minimizada. Si el argumento 'master' es
        # omitido el valor, por defecto, será la ventana
        # madre.
        self.dialogo.transient(master=self.raiz)
        # El método grab_set() asegura que no haya eventos
        # de ratón o teclado que se envíen a otra ventana
        # diferente a 'self.dialogo'. Se utiliza para
        # crear una ventana de tipo modal que será
        # necesario cerrar para poder trabajar con otra
        # diferente. Con ello, también se impide que la
        # misma ventana se abra varias veces.
        self.dialogo.grab_set()
        self.raiz.wait_window(self.dialogo)


def main():
    Aplicacion()
    return(0)

if __name__ == '__main__':
    main()
