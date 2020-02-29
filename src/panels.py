
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserListView

sizing = {'size_hint_y': None, 'height': 40}

# TODO: Convert these panels/layouts into *.kv layout files

class LoginPanel(BoxLayout):
    """Setup the main login panel.
    """
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=40, spacing=40, **kwargs)

        # Default width of each element
        # Build the login form
        self.add_widget(Label(text='Git Server', **sizing))
        self.add_widget(TextInput(multiline=False, write_tab=False, **sizing))
        self.add_widget(Label(text='Username', **sizing))
        self.add_widget(TextInput(multiline=False, write_tab=False, **sizing))
        self.add_widget(Label(text='Password', **sizing))
        self.add_widget(TextInput(multiline=False, write_tab=False, **sizing))
        self.add_widget(Button(text='Connect', **sizing))

class FilePanel(BoxLayout):
    """Setup the main file panel.
    """
    def __init__(self, **kwargs):
        super().__init__(padding=40, spacing=40, **kwargs)

        # Setup the side panel
        stack = StackLayout(spacing=10, padding=10, size_hint=(0.4, 1))
        stack.add_widget(Label(text='Branch Name', **sizing))
        stack.add_widget(Button(text='Send Changes', **sizing))
        stack.add_widget(Button(text='Get Changes', **sizing))
        stack.add_widget(Button(text='Check for Changes', **sizing))
        self.add_widget(stack)

        self.add_widget(FileChooserListView())

