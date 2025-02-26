from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.text_input = TextInput()
        copy_btn = Button(text="Copiar", on_press=self.copy_text)
        paste_btn = Button(text="Colar", on_press=self.paste_text)
        layout.add_widget(self.text_input)
        layout.add_widget(copy_btn)
        layout.add_widget(paste_btn)
        return layout

    def copy_text(self, instance):
        self.text_input.copy()

    def paste_text(self, instance):
        self.text_input.paste()

if __name__ == '__main__':
    MyApp().run()