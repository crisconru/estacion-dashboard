from tkinter import *
from tkinter import ttk


class Aplicacion():
    ''' Clase Aplicacion '''
    # Declara una variable de clase para contar ventanas
    ventana = 0
    # Declara una variable de clase para usar en el
    # cálculo de la posición de una ventana
    posx_y = 0

    def __init__(self):
        ''' Construye ventana de aplicación '''
        # Declara ventana de aplicación
        self.raiz = Tk()
        # Define dimensión de la ventana 800x700
        # que se situará en la coordenada x=500,y=50
        self.raiz.geometry('800x700+500+50')

        self.raiz.resizable(0, 0)
        self.raiz.title("Ventana de aplicación")
        # Define botón 'Abrir' que se utilizará para
        # abrir las ventanas de diálogo. El botón
        # está vinculado con el método 'self.abrir'
        boton = ttk.Button(self.raiz, text='Abrir', command=self.abrir)
        boton.pack(side=BOTTOM, padx=20, pady=20)
        self.raiz.mainloop()

    def abrir(self):
        ''' Construye una ventana de diálogo '''
        # Define una nueva ventana de diálogo
        self.dialogo = Toplevel()
        # Incrementa en 1 el contador de ventanas
        Aplicacion.ventana += 1
        # Recalcula posición de la ventana
        Aplicacion.posx_y += 50
        tamypos = f'400x200+{Aplicacion.posx_y}+{Aplicacion.posx_y}'
        self.dialogo.geometry(tamypos)
        self.dialogo.resizable(0, 0)
        # Obtiene identicador de la nueva ventana
        ident = self.dialogo.winfo_id()
        # Construye mensaje de la barra de título
        titulo = f'{Aplicacion.ventana}: {ident}'
        self.dialogo.title(titulo)
        # Define el botón 'Cerrar' que cuando sea
        # presionado cerrará (destruirá) la ventana
        # 'self.dialogo' llamando al método
        # 'self.dialogo.destroy'
        boton = ttk.Button(self.dialogo, text='Cerrar',
                           command=self.dialogo.destroy)
        boton.pack(side=BOTTOM, padx=20, pady=20)
        # Cuando la ejecución del programa llega a este
        # punto se utiliza el método wait_window() para
        # esperar que la ventana 'self.dialogo' sea
        # destruida.
        # Mientras tanto se atiende a los eventos locales
        # que se produzcan, por lo que otras partes de la
        # aplicación seguirán funcionando con normalidad.
        # Si hay código después de esta línea se ejecutará
        # cuando la ventana 'self.dialogo' sea cerrada.
        self.raiz.wait_window(self.dialogo)


def main():
    Aplicacion()
    return(0)

if __name__ == '__main__':
    main()
