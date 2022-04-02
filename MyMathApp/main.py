from tkinter import *
from funcs import *
from items import click

class MyMathApp:
    def __init__(self):
        self.window = Tk()
        self.icon = PhotoImage(file="logo.png")
        self.lblIcon = PhotoImage(file="math2.png")
        self.label = Label(
            self.window,
            text="Welcome to the Math Games!",
            font=("Times",12,"bold"),
            fg="black",
            bg="white",
            relief=RIDGE,
            bd=5,
            padx=5,
            pady=5,
            compound="top"
        )
        self.next_label = Label(
            self.window,
            text="Please choose a math game to play:",
            font=("Times",12,"bold"),
            fg="black",
            bg="white",
            relief=RIDGE,
            bd=5,
            padx=5,
            pady=5,
            compound="top"
        )
        self.button = Button(
            self.window,
            text="Click to Play the Addition Game",
            command=self.new_wind,
            relief=RIDGE,
            bd=3,   
            font=("Times",10,"bold"),
            fg="black",
            bg="white",
            activeforeground="white",
            activebackground="black"
        )
        self.sec_button = Button(
            self.window,
            text="Click to Play the Subtraction Game",
            command=self.other_wind,
            relief=RIDGE,
            bd=3,   
            font=("Times",10,"bold"),
            fg="black",
            bg="white",
            activeforeground="white",
            activebackground="black"
        )
        self.thr_button = Button(
            self.window,
            text="Click to Play the Multiplication Game",
            command=self.more_wind,
            relief=RIDGE,
            bd=3,   
            font=("Times",10,"bold"),
            fg="black",
            bg="white",
            activeforeground="white",
            activebackground="black"
        )
        self.four_button = Button(
            self.window,
            text="Click to Play the Division Game",
            command=self.another_wind,
            relief=RIDGE,
            bd=3,   
            font=("Times",10,"bold"),
            fg="black",
            bg="white",
            activeforeground="white",
            activebackground="black"
        )
        self.fif_button = Button(
            self.window,
            text="Click to Play the Exponent Game",
            command=self.crying_wind,
            relief=RIDGE,
            bd=3,   
            font=("Times",10,"bold"),
            fg="black",
            bg="white",
            activeforeground="white",
            activebackground="black"
        )
        self.sixt_button = Button(
            self.window,
            text="Click to Play the Floor Division Game",
            command=self.last_wind,
            relief=RIDGE,
            bd=3,   
            font=("Times",10,"bold"),
            fg="black",
            bg="white",
            activeforeground="white",
            activebackground="black"
        )
    
    def run(self):
        self.window.geometry("500x600")
        self.window.title("Math Games")
        self.window.config(background="white")
        self.label.place(x=143,y=50)
        self.next_label.place(x=125,y=320)
        self.button.place(x=160,y=380)
        self.sec_button.place(x=151,y=410)
        self.thr_button.place(x=143,y=440)
        self.four_button.place(x=160,y=470)
        self.fif_button.place(x=158,y=500)
        self.sixt_button.place(x=144,y=530)
        self.window.resizable(False, False)
        self.dm_button()

        self.window.mainloop()

    def entry_click(self):
        print(f"Hello! {self.entry.get()}")

    def new_wind(self):
        next_window = Addition_Wind()
        self.window.destroy()
        next_window.vamos()

    def other_wind(self):
        other_wind = Subtraction_Wind()
        self.window.destroy()
        other_wind.ira()

    def more_wind(self):
        more_wind = Mul_Wind()
        self.window.destroy()
        more_wind.empezar()

    def another_wind(self):
        another_wind = Div_Wind()
        self.window.destroy()
        another_wind.justovamos()

    def crying_wind(self):
        crying_wind = Exponent_Wind()
        self.window.destroy()
        crying_wind.yoodioesta()

    def last_wind(self):
        last_wind = FloorDiv_Wind()
        self.window.destroy()
        last_wind.soyhice()

    def dark_mode(self):
        self.window.config(background="black")
        self.dm_button(destroy=True)
        self.wm_button()

    def white_mode(self):
        self.window.config(background="white")
        self.wm_button(destroy=True)
        self.dm_button()

    def dm_button(self, destroy=False):
        dm_button = Button(
            self.window,
            text="Turn on Dark Mode",
            command=self.dark_mode,
            bd=3,
            relief=RIDGE,
            font=("Times",10,"bold"),
            fg="black",
            bg="white",
            activeforeground="white",
            activebackground="black"
        )
        dm_button.place(x=190,y=0)

        if destroy:
            dm_button.destroy()

    def wm_button(self, destroy=False):
        wm_button = Button(
            self.window,
            text="Turn off Dark Mode",
            command=self.white_mode,
            bd=3,
            relief=RIDGE,
            font=("Times",10,"bold"),
            fg="black",
            bg="white",
            activeforeground="white",
            activebackground="black"
        )
        wm_button.place(x=190,y=0)

        if destroy:
            wm_button.destroy()

theApp = MyMathApp()

if __name__ == "__main__":
    theApp.run()