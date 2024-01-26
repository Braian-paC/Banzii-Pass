import kivy
kivy.require('2.1.0')

import random as rd
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

class GerPass(GridLayout):
    def __init__(self, **kwargs):
        super(GerPass, self).__init__(**kwargs)
        self.cols = 2

        btn1 = Button(text='Gerar senha aleatória')
        btn2 = Button(text='Randomizar senha')
        self.output1 = TextInput(text='CLIQUE NO BOTÃO')
        self.output2 = TextInput(text='DIGITE SUA SENHA E CLIQUE NO BOTÃO')

        self.add_widget(btn1)
        self.add_widget(self.output1)
        self.add_widget(btn2)
        self.add_widget(self.output2)

        btn1.bind(on_press=self.btn1_click)
        btn2.bind(on_press=self.btn2_click)

    def btn1_click(self, instance):
        random_characters = "0123456789AaBbCcDdEeFfGgHhJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzçÇ]}[{?!#$%&*"
        caracteres, pass_origin = 15, ""
        for c in range(0, caracteres):
            pass_add = rd.choice(random_characters)
            pass_origin = pass_add + pass_origin
        self.output1.text = pass_origin
    def btn2_click(self, instance):
        pass_new = ''.join(rd.sample(self.output2.text, len(self.output2.text)))
        self.output2.text = pass_new

class Banzii_Pass(App):

    def build(self):
        self.title= 'Banzii Pass'
        Window.size = (800, 200)
        return GerPass()

if __name__ == '__main__':
    Banzii_Pass().run()
