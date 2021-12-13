from tkinter import Tk, ttk
from tkinter import *
from tkinter.font import Font
from tkinter.messagebox import *
import sys
import threading
# a remplacer âr le repertoire /usr/share/osm au moment du deploiement
sys.path.append("/usr/share/osm")

import codebar 
import core

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
        self.getCode = lambda code : str(code[0])[2:-1]

        self.donneeRetrait = {
            'code': StringVar(),
            'designation': StringVar(),
            'descriptions': StringVar(),
            'quantite' : StringVar()
        }
        self.donneeDepot = {
            'code': StringVar(),
            'designation': StringVar(),
            'descriptions': StringVar(),
            'quantite' : StringVar(),
        }

        self.onglet_deposer = ttk.Frame(self.onglet_control)
        self.onglet_retirer = ttk.Frame(self.onglet_control)

        self.onglet_control.add(self.onglet_deposer, text='Depot')
        self.onglet_control.add(self.onglet_retirer, text='Retirer')

        self.onglet_control.pack(expand=1, fill="both")
        t = threading.Thread(target=codebar.BarcodeReader, args=(self,))
        t.setDaemon(True)
        t.start()

        self.showDepotForm((b'test interface', 'generic'))
        #self.showRetraitForm((b'test interface', 'generic'))

    def showDepotForm(self, code):# a remplacer par la bonne configuration
        self.donneeDepot['code'].set(self.getCode(code))
        codeLabel = Label(self.onglet_deposer, text="Barcode: " + self.getCode(code), font="Arial 70")
        codeLabel.grid(row=1, column=2)


        designationLabel = Label(self.onglet_deposer, text="Desigation :", font="Arial 50")
        designationLabel.grid(row=2, column=1, sticky=W)

        designationEntry = Entry(self.onglet_deposer, textvariable=self.donneeDepot['designation'], width=80)
        designationEntry.grid(row=2, column=2, columnspan=2)


        descriptionLabel = Label(self.onglet_deposer, text="Descriptions :", font="Arial 50")
        descriptionLabel.grid(row=3, column=1, sticky=W)

        descriptionEntry = Entry(self.onglet_deposer, textvariable=self.donneeDepot['descriptions'], width=80)
        descriptionEntry.grid(row=3, column=2, columnspan=2)


        quantiteLabel = Label(self.onglet_deposer, text="Quantite :", font="Arial 50")
        quantiteLabel.grid(row=4, column=1, sticky=W)

        quantiteEntry = Entry(self.onglet_deposer, textvariable=self.donneeDepot['quantite'], width=80)
        quantiteEntry.grid(row=4, column=2, columnspan=2)

        ajouterButton = Button(self.onglet_deposer, text="Deposer", command=self.deposer)
        ajouterButton.grid(row=5, column=3, sticky=E)


    def showRetraitForm(self, code):# a remplacer par la bonne configuration
        self.donneeDepot['code'].set(self.getCode(code))
        codeLabel = Label(self.onglet_retirer, text="Barcode: " + self.getCode(code), font="Arial 70")
        codeLabel.grid(row=1, column=2)


        designationLabel = Label(self.onglet_retirer, text="Desigation :", font="Arial 50")
        designationLabel.grid(row=2, column=1, sticky=W)

        designationEntry = Entry(self.onglet_retirer, textvariable=self.donneeRetrait['designation'], width=80)
        designationEntry.grid(row=2, column=2, columnspan=2)


        descriptionLabel = Label(self.onglet_retirer, text="Descriptions :", font="Arial 50")
        descriptionLabel.grid(row=3, column=1, sticky=W)

        designationEntry = Entry(self.onglet_retirer, textvariable=self.donneeRetrait['descriptions'], width=80)
        designationEntry.grid(row=3, column=2, columnspan=2)


        quantiteLabel = Label(self.onglet_retirer, text="Quantite :", font="Arial 50")
        quantiteLabel.grid(row=4, column=1, sticky=W)

        quantiteEntry = Entry(self.onglet_retirer, textvariable=self.donneeRetrait['quantite'], width=80)
        quantiteEntry.grid(row=4, column=2, columnspan=2)

        ajouterButton = Button(self.onglet_retirer, text="Deposer", command=self.retirer)
        ajouterButton.grid(row=5, column=3, sticky=E)

    def procede(self, code):
        self.dispo =False
        if self.onglet_control.select()[-1] == '2':
            print("on effectue un retrait")
            self.showRetraitForm(code)
        else:
            print("on effectue un depot")
            self.showDepotForm(code)

    def correctSaisieDepot(self):
       
        for i in self.donneeDepot.values():
            print(i.get())
        if len(self.donneeDepot['code'].get()) == 0:
            return False
        
        if len(self.donneeDepot['designation'].get()) == 0:
            return False
        
        if not self.donneeDepot['quantite'].get().isnumeric() or len(self.donneeDepot['quantite'].get()) == 0:
            return False
        
        return True

    def correctSaisieRetrait(self):
       
        for i in self.donneeDepot.values():
            print(i.get())
        if len(self.donneeDepot['code'].get()) == 0:
            return False
        
        if len(self.donneeDepot['designation'].get()) == 0:
            return False
        
        if not self.donneeDepot['quantite'].get().isnumeric() or len(self.donneeDepot['quantite'].get()) == 0:
            return False
        
        return True

    def deposer(self):
        if self.correctSaisieDepot():
            if core.deposer(self.donneeRetrait['code'].get(),
                         self.donneeRetrait['designation'].get(),
                         self.donneeRetrait['descriptions'].get(),
                         self.donneeRetrait['quantite'].get()
                         ) == -1:
                showwarning("Erreur", "L'article scannee n'est pas enregistrer dans e stock")
            
        else:
             showwarning("Erreur de Saisie", "Les informations saisies sont incorrect")
             return

        for element in self.onglet_deposer.winfo_children():
            element.destroy()
        
    def retirer(self):
        if self.correctSaisieRetrait():
            if core.retirer(self.donneeRetrait['code'].get(),
                         self.donneeRetrait['designation'].get(),
                         self.donneeRetrait['descriptions'].get(),
                         self.donneeRetrait['quantite'].get()
                         ) == -1:
                showwarning("Erreur", "L'article scannee n'est pas enregistrer dans le stock")
            
        else:
             showwarning("Erreur de Saisie", "Les informations saisies sont incorrect")
             return
        for element in self.onglet_retirer.winfo_children():
            element.destroy()
        
        self.dispo = True