from kivy.lang import Builder
from kivymd.app import MDApp

KV = """
Screen:
    MDFlatButton:
        text: 'Hello world'
        pos_hint: {'center_x':.5, 'center_y': .5}

"""


class MyApp(MDApp):

    def build(self):
        return Builder.load_string(KV)


if __name__ == '__main__':
    MyApp().run()
