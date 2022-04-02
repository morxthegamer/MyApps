from tkinter import *
from customtkinter import *

class CalcApp:
    def __init__(self):
        self.wind = Tk()
        self.icon = PhotoImage(file="icon.png")
        self.message = Message(
            self.wind,
            text="Hello",
            font=("Times New Roman", 10, "bold")
        )
        self.num1 = Button(
            self.wind,
            text="1 abc",
            relief=RIDGE,
            bd=3,   
            font=("Times New Roman",10,"bold"),
            fg="black",
            bg="white",
            activeforeground="white",
            activebackground="black",
            width=6,
            height=3
        )
        self.num2 = Button(
            self.wind,
            text="2 def",
            relief=RIDGE,
            bd=3,   
            font=("Times New Roman",10,"bold"),
            fg="black",
            bg="white",
            activeforeground="white",
            activebackground="black",
            width=6,
            height=3
        )
        self.num3 = Button(
            self.wind,
            text="3 ghi",
            relief=RIDGE,
            bd=3,   
            font=("Times New Roman",10,"bold"),
            fg="black",
            bg="white",
            activeforeground="white",
            activebackground="black",
            width=6,
            height=3
        )
        self.plus_button = Button(
            self.wind
        )
        self.num4 = Button(
            self.wind,
            text="4 jkl",
            relief=RIDGE,
            bd=3,   
            font=("Times New Roman",10,"bold"),
            fg="black",
            bg="white",
            activeforeground="white",
            activebackground="black",
            width=6,
            height=3
        )
        self.num5 = Button(
            self.wind,
            text="5 mno",
            relief=RIDGE,
            bd=3,   
            font=("Times New Roman",10,"bold"),
            fg="black",
            bg="white",
            activeforeground="white",
            activebackground="black",
            width=6,
            height=3
        )
        self.num6 = Button(
            self.wind,
            text="6 pqr",
            relief=RIDGE,
            bd=3,   
            font=("Times New Roman",10,"bold"),
            fg="black",
            bg="white",
            activeforeground="white",
            activebackground="black",
            width=6,
            height=3
        )
        self.minus_button = Button(
            self.wind,
            text="",
            
        )
        self.num7 = Button(
            self.wind,
            text="7 stu",
            relief=RIDGE,
            bd=3,   
            font=("Times New Roman",10,"bold"),
            fg="black",
            bg="white",
            activeforeground="white",
            activebackground="black",
            width=6,
            height=3
        )
        self.num8 = Button(
            self.wind,
            text="8 vwx",
            relief=RIDGE,
            bd=3,
            font=("Times New Roman",10,"bold"),
            fg="black",
            bg="white",
            activeforeground="white",
            activebackground="black",
            width=6,
            height=3
        )
        self.num9 = Button(
            self.wind,
            text="9 yz",
            relief=RIDGE,
            bd=3,   
            font=("Times New Roman",10,"bold"),
            fg="black",
            bg="white",
            activeforeground="white",
            activebackground="black",
            width=6,
            height=3
        )
        self.times_button = Button(
            self.wind,
        )

    def run(self):
        self.wind.geometry("500x500")
        self.wind.title("Calculator App! | Zamar Wint")
        self.wind.iconphoto(True,self.icon)
        self.message.pack()
        # self.num1.pack()
        # self.num2.pack()
        # self.num3.pack()
        # self.num4.pack()
        # self.num5.pack()
        # self.num6.pack()
        # self.num7.pack()
        # self.num8.pack()
        # self.num9.pack()
        self.wind.mainloop()

App = CalcApp()

if __name__ == "__main__":
    App.run()