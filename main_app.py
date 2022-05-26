# напиши здесь свое приложение

# Создать progress-bar на последнем экране

# как создавать MessageBox
# Переменные не перезаписываются

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.progressbar import ProgressBar
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image

from random import *

# Смена фона
from kivy.core.window import Window
from numpy import spacing

# MODULES
import instructions

# Variables
directions = ("right", "left", "down", "up")
name_user = None
age_user = 0
pulse_1st = 0
pulse_2nd = 0
pulse_3rd = 0


def check_integer(num):
    try:
        num = int(num)
        return True
    except:
        return False

class InfoScr(Screen):
    def __init__(self, name="info"): 
        super().__init__(name=name)

        lbl_insruction = Label(
            text=instructions.txt_instruction,
        )
        

        self.btn_begin = Button(
            text="Начать",
            size_hint=(1,.5),
        )

        self.btn_begin.on_press = self.next

        self.name_input = TextInput(multiline=False, 
                            hint_text="Напишите имя здесь:",
                            size_hint=(.3, 1),
                                )
        self.age_input = TextInput(multiline=False, 
                                hint_text="Введите ваш возраст:",
                                size_hint=(.3, 1),
                                )

        layout = BoxLayout(orientation="vertical")
        layout_horiz = BoxLayout(orientation="horizontal", spacing=10, padding=4)

        layout_horiz.add_widget(self.name_input)
        layout_horiz.add_widget(self.age_input)
        
        layout.add_widget(lbl_insruction)

        layout.add_widget(layout_horiz)
        
        layout.add_widget(self.btn_begin)

        self.add_widget(layout)


    def next(self):
        global name_user, age_user
        name_user = self.name_input.text
        age_user = self.age_input.text

        returning = check_integer(age_user)

        if returning:
            if not(name_user is "") and not(age_user is ""):
                print("NAME",name_user)
                print("AGE", age_user)
                self.manager.transition.direction = choice(directions)
                self.manager.current = "1_st_test" 
            else:
                print(not(name_user is ""))
                print(not(age_user is ""))
                print(not(name_user is "") and not(age_user is ""))

class Test_1st_Scr(Screen):
    def __init__(self, name="1_st_test"): 
        super().__init__(name=name)

        lbl_instruction = Label(
            text=instructions.txt_test1
        )

        self.pulse_1st_input = TextInput(multiline=False, 
                                hint_text="Введите пульс:",
                                size_hint=(.7, 1),
                                pos_hint={"center_x":.5},
                                )
        self.btn_continue = Button(
            text="Продолжить",
            size_hint=(1,.5),
            
        )
        self.btn_continue.on_press = self.next

        layout = BoxLayout(orientation="vertical", spacing = 5)

        layout.add_widget(lbl_instruction)
        layout.add_widget(self.pulse_1st_input)
        layout.add_widget(self.btn_continue)

        self.add_widget(layout)

    def next(self):
        global pulse_1st
        pulse_1st = self.pulse_1st_input.text

        returning = check_integer(pulse_1st)

        if returning:
            if not(pulse_1st is ""):
                print("PULSE_1ST", pulse_1st)
                self.manager.transition.direction = choice(directions)
                self.manager.current = "2_nd_test" 
            else:
                print(not(pulse_1st is ""))

class Test_2nd_Scr(Screen):
    def __init__(self, name="2_nd_test"): 
        super().__init__(name=name)

        lbl_instruction = Label(
            text=instructions.txt_test2,
            
        )

        self.btn_begin = Button(
            text="Начать отсчет",
            size_hint=(1,.5),
            
        )
        self.btn_begin.on_press = self.begin

        layout = BoxLayout(orientation="vertical")

        layout.add_widget(self.btn_begin)
        layout.add_widget(lbl_instruction)

        self.add_widget(layout)

    def begin(self):
        time = 30
        if time == 30:#прошло 30с 
            self.manager.transition.direction = choice(directions)
            self.manager.current = "3_rd_test" 

class Test_3rd_Scr(Screen):
    def __init__(self, name="3_rd_test"): 
        super().__init__(name=name)

        lbl_instruction = Label(
            text=instructions.txt_test3
        )

        self.pulse_2nd_input = TextInput(multiline=False, 
                                hint_text="Введите пульс, замеренные за первые 15с:",
                                size_hint=(.3, 1),
                                )

        self.pulse_3rd_input = TextInput(multiline=False, 
                                hint_text="Введите пульс, замеренный за последние 15с:",
                                size_hint=(.3, 1),
                                )
        self.btn_result = Button(
            text="Перейти к результатам",
            size_hint=(1,.5),
        )

        self.btn_result.on_press = self.next

        layout = BoxLayout(orientation="vertical", spacing=5)
        layout_vertical = BoxLayout(orientation="horizontal", spacing=10)

        layout_vertical.add_widget(self.pulse_2nd_input)
        layout_vertical.add_widget(self.pulse_3rd_input)

        layout.add_widget(lbl_instruction)
        layout.add_widget(layout_vertical)
        layout.add_widget(self.btn_result)

        self.add_widget(layout)



    def next(self):
        global pulse_2nd, pulse_3rd

        pulse_2nd = self.pulse_2nd_input.text
        pulse_3rd = self.pulse_3rd_input.text

        returning_1st = check_integer(pulse_2nd)
        returning_2nd = check_integer(pulse_3rd)
    
        if returning_1st and returning_2nd:
            if not(pulse_2nd is "") and not(pulse_3rd is ""):
                print("PULSE_2nd", pulse_2nd)
                print("PULSE_3rd", pulse_3rd)

                self.manager.transition.direction = choice(directions)
                self.manager.current = "result" 


class ResultScr(Screen):
    def __init__(self, name="result"): 
        super().__init__(name=name)
        global pulse_1st, pulse_2nd, pulse_3rd, name_user     
        result_rufie = (4*(int(pulse_1st)+int(pulse_2nd)+int(pulse_3rd)) - 200)/10

        result_rufie_lbl = Label(text = f"{name_user}, Ваш уровень работы сердца: {str(result_rufie)}")

        self.add_widget(result_rufie_lbl)


class RufieApp(App):
    def build(self):
    
        scr_manager = ScreenManager()
        # ДОбавление экранов
        scr_manager.add_widget(InfoScr(name="info"))
        
        scr_manager.add_widget(Test_1st_Scr(name="1_st_test"))
        scr_manager.add_widget(Test_2nd_Scr(name="2_nd_test"))
        scr_manager.add_widget(Test_3rd_Scr(name="3_rd_test"))

        scr_manager.add_widget(ResultScr(name="result"))

        # будет показан FirstScr, потому что он добавлен первым. Это можно поменять вот так:
        scr_manager.current = "info"

        return scr_manager

app = RufieApp()
app.run()

# a = 5

# def ch():
#     global a
#     a = 10
# ch()
# print(a)