from kivy.app import App
from kivy.uix.widget import Widget

from kivy.properties import StringProperty
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path

from random import randint
# resource_add_path('C:\Windows\Fonts')
# LabelBase.register(DEFAULT_FONT, 'HGRGE.TTC')

class ImageWidget(Widget):
    source = StringProperty('./images/box.jpg')

    def __init__(self, **kwargs):
        super(ImageWidget, self).__init__(**kwargs)
        pass

    def buttonOrigin(self):
        self.source = './images/box.jpg'

    def buttonRandom(self):
        num = randint(0,1)
        if num == 0:
            self.source = './images/sleepcat.jpg'
        else:
            self.source = './images/livecat.jpg'

class TestApp(App):
    def __init__(self, **kwargs):
        super(TestApp, self).__init__(**kwargs)
        # self.title = 'シュレーディンガーの猫'

if __name__ == '__main__':
    TestApp().run()