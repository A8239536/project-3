from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
import Long
import Long_back
import Pick
import Pick_back
import Small
import Small_back

class SecondWindow(Screen):
    def Long_ball(self):
        Long.long()
        kv.current = "second"

    def Long_ball_back(self):
        Long_back.long_back()
        kv.current = "second"

    def Pick_ball(self):
        Pick.pick()
        kv.current = "second"

    def Pick_ball_back(self):
        Pick_back.pick_back()
        kv.current = "second"
    def Small_ball(self):
        Small.small()
        kv.current = "second"
    def Small_ball_back(self):
        Small_back.small_back()
        kv.current = "second"

class WindowManager(ScreenManager):
    pass
kv = Builder.load_file("test.kv")

#sm = WindowManager()
class MyMainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyMainApp().run()
