import kivy, utils
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.app import App

funcs = utils.Utils()

class BibleApp(App):

    def build(self):
        self.window = BoxLayout()

        # Initialization

        self.label = Label(
            text="Pick the scripture verse to view:"
        )

        self.choiceButton1 = Button(
            text="Isiah 54:17",
            size_hint=(0.5, 0.5)
        )

        self.choiceButton2 = Button(
            text="Psalms 119:38"
        )

        self.textInput = TextInput(
            font_size=100
        )

        

        # Addings

        self.window.add_widget(self.label)
        self.window.add_widget(self.choiceButton1)
        self.window.add_widget(self.choiceButton2)
        self.window.add_widget(self.textInput)

        return self.window

if __name__ == "__main__":
    bibleApp = BibleApp()
    bibleApp.run()