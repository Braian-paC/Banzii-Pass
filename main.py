import kivy
kivy.require('2.1.0')

import random as rd
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

class GerPass(GridLayout):
    def __init__(self, **kwargs):
        super(GerPass, self).__init__(**kwargs)
        self.cols = 2
    def btn1_click(self):
        random_characters = "0123456789AaBbCcDdEeFfGgHhJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzçÇ]}[{?!#$%&*"
        caracteres, pass_origin = 15, ""
        for c in range(0, caracteres):
            pass_add = rd.choice(random_characters)
            pass_origin = pass_add + pass_origin
        self.ids.output1.text = pass_origin
    def btn2_click(self):
        pass_new = ''.join(rd.sample(self.ids.output2.text, len(self.ids.output2.text)))
        self.ids.output2.text = pass_new

class Banzii_Pass(App):

    def build(self):
        self.title= 'Banzii Pass'
        Window.size = (800, 200)
        Builder.load_file('banzii_pass.kv')

if __name__ == '__main__':
    Banzii_Pass().run()
