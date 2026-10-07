from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class SpartanApp(App):
    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=20
        )

        title = Label(
            text="اسپارتان",
            font_size=40
        )

        menu = Label(
            text="به برنامه اسپارتان خوش آمدید",
            font_size=22
        )

        start_button = Button(
            text="شروع",
            font_size=24,
            size_hint_y=None,
            height=70
        )

        layout.add_widget(title)
        layout.add_widget(menu)
        layout.add_widget(start_button)

        return layout


SpartanApp().run()
