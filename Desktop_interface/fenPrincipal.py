from tkinter import Tk, ttk
from tkinter import *
from tkinter.messagebox import *
import sys, os
# a remplacer âr le repertoire /lib/bin-cgi/oms au moment du deploiement
sys.path.append("/home/talibe/Bureau/Open_Stock_Manager-OMS/web_UI")

import core

core.database()
class MainWindow(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.minsize(700, 400)
        self.maxsize(800, 400)
        self.onglet_control = ttk.Notebook(self)


        self.onglet_deposer = ttk.Frame(self.onglet_control)
        self.onglet_retirer = ttk.Frame(self.onglet_control)

        self.onglet_control.add(self.onglet_deposer, text='Depot')
        self.onglet_control.add(self.onglet_retirer, text='Retirer')


        self.onglet_control.pack(expand=1, fill="both")
        