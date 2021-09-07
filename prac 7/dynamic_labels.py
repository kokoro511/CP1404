from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class dynamiclabelsDemo(App):
    def build(self):
        self.title = "dynamic_labels Demo"
        self.root = Builder.load_file('dynamic_labels.kv')
        return self.root

dynamiclabelsDemo().run()