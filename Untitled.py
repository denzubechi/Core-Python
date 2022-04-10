# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 22:25:04 2020

@author: Sah Meey
"""

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button

class WormApp(App):
     def build(self):
        self.but = Button()
        self.but.pos = (100, 100)
        self.but.size = (200, 200)
        self.but.text = "Hello, cruel world"
        self.form = Widget()
        self.form.add_widget(self.but)
        return self.form

if __name__ == '__main__':
    WormApp().run()
    
    
    
    
    
    
    
    
    
    
    
    
    