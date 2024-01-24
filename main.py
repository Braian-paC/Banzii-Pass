import kivy
kivy.require('2.1.0')

import random as rd 
from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

def randomizar_senha():
    pass_old = str(input('Digite sua senha atual: '))
    pass_new = ''.join(rd.sample(pass_old, len(pass_old)))
    print(f'Senha randomizada: {pass_new}')

class GerPass(GridLayout):
    def __init__(self, **kwargs):
        super(GerPass, self).__init__(**kwargs)
        self.cols = 2

        btn1 = Button(text='Gerar senha aleatória')
        btn2 = Button(text='Randomizar senha')
        self.output1 = TextInput(text='SENHA')
        self.output2 = TextInput(text='SENHA')

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
        self.output2.text = "FUNÇÃO EM ANDAMENTO"

class MyApp(App):

    def build(self):
        return GerPass()

if __name__ == '__main__':
    MyApp().run()
