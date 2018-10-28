from tkinter import Tk
from tkinter import ttk, BOTTOM


class Aplicacion():
    def __init__(self):
        self.root = Tk()
        self.root.geometry('1000x1000')
        self.root.resizable(False, False)
        self.root.configure(bg='beige')
        self.root.title('Ver info')
        ttk.Button(self.root, text='Salir', command=quit).pack(side=BOTTOM)
        self.root.mainloop()


def main():
    Aplicacion()
    return 0


if __name__ == '__main__':
    main()
