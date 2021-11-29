from tkinter import Tk, ttk
from tkinter import *
from tkinter.font import Font
from tkinter.messagebox import *
import sys
import threading
# a remplacer âr le repertoire /usr/share/osm au moment du deploiement
sys.path.append("/run/media/talibe/4ec026c5-bbb6-4ca0-94b0-f9dc7a1028e2/home/talibe/Bureau/Open_Stock_Manager-OMS/web_UI")
sys.path.append("/run/media/talibe/4ec026c5-bbb6-4ca0-94b0-f9dc7a1028e2/home/talibe/Bureau/Open_Stock_Manager-OMS/web_UI")

import core
import codebar 


class GuiThread(threading.Thread):
    def ___init__(self):
        threading.Thread.__init__(self)

    def run(self):
        self.window = MainWindow()
        self.window.mainloop()


class MainWindow(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.minsize(700, 400)
        self.maxsize(800, 400)
        self.dispo = True
        self.onglet_control = ttk.Notebook(self)
        self.donnees = {
            'designationDepot': StringVar(),
            'designationRetrait': StringVar(),
            'descriptionsDepot': StringVar(),
            'descriptionsRetrait': StringVar(),
            'quantiteDepot' : StringVar(),
            'quantiteRetrait' : StringVar()
        }

        self.onglet_deposer = ttk.Frame(self.onglet_control)
        self.onglet_retirer = ttk.Frame(self.onglet_control)

        self.onglet_control.add(self.onglet_deposer, text='Depot')
        self.onglet_control.add(self.onglet_retirer, text='Retirer')

        self.onglet_control.pack(expand=1, fill="both")
        t = threading.Thread(target=codebar.BarcodeReader, args=(self,))
        t.setDaemon(True)
        t.start()

    def showDepotForm(self, code):# a remplacer par la bonne configuration
        l = Label(self.onglet_deposer, text="Barcode: " + str(code[0])[2:-1], font="Arial 50")
        l.pack()
        e = Entry(self.onglet_deposer)
        e.pack(fill=BOTH)
        b = Button(self.onglet_deposer, text="ajouter", command=self.ajouter)
        b.pack(fill=BOTH)
    
    def showRetraitForm(self, code):# a remplacer par la bonne configuration
        l = Label(self.onglet_retirer, text="Barcode: " + str(code[0][2:-1]), font="Arial 50")
        l.pack()
        e = Entry(self.onglet_retirer)
        e.pack(fill=BOTH)
        b = Button(self.onglet_retirer, text="ajouter", command=self.ajouter)
        b.pack(fill=BOTH)

    def procede(self, code):
        self.dispo =False
        if self.onglet_control.select()[-1] == '2':
            print("on effectue un retrait")
            self.showRetraitForm(code)
        else:
            print("on effectue un depot")
            self.showDepotForm(code)


    def ajouter(self):
        # recuperer le code barre et l'ajouter dans la base de donnees
        if self.onglet_control.select()[-1] == '2':
            for i in self.onglet_retirer.winfo_children():
                i.destroy()
        else:
            for i in self.onglet_deposer.winfo_children():
                i.destroy()
        
        self.dispo = True