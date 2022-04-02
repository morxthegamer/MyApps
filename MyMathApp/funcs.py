from main import MyMathApp
from tkinter import *

class Addition_Wind:
    def __init__(self):
        self.new_window = Tk()
        self.backButton = Button(
            self.new_window,
            text="Back",
            font=("Times", 10, "bold"),
            command=self.callBackMainCls
        )
        self.new_button = Button(
            self.new_window,
            text="Submit",
            background="white",
            font=("Courier", 10, "bold"),
        )
        self.entry = Entry(
            self.new_window,
            font=("Times New Roman",10,"bold"),
            bd=3,
            bg="white",
            fg="black"
        )
        self.entry_button = Button(
            self.new_window,
            text="Submit",
            font=("Collins",10,"bold"),
        )

    def vamos(self):
        self.new_window.geometry("500x600")
        self.new_window.title("The Addition Game")
        self.new_button.pack()
        self.backButton.pack()
        self.new_window.resizable(False, False)

    def callBackMainCls(self):
        again = MyMathApp()
        self.new_window.destroy()
        again.run()
    

class Subtraction_Wind:
    def __init__(self):
        self.other_window = Tk()

    def ira(self):
        self.other_window.geometry("500x600")
        self.other_window.title("The Subtraction Game")

class Mul_Wind:
    def __init__(self):
        self.fine_window = Tk()

    def empezar(self):
        self.fine_window.geometry("500x600")
        self.fine_window.title("The Multiplication Game")

class Div_Wind:
    def __init__(self):
        self.go_window = Tk()

    def justovamos(self):
        self.go_window.geometry("500x600")
        self.go_window.title("The Division Game")

class Exponent_Wind:
    def __init__(self):
        self.bruh_window = Tk()

    def yoodioesta(self):
        self.bruh_window.geometry("500x600")
        self.bruh_window.title("The Exponent Game")

class FloorDiv_Wind:
    def __init__(self):
        self.idk_window = Tk()

    def soyhice(self):
        self.idk_window.geometry("500x600")
        self.idk_window.title("The Floor Division Game")