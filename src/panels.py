
from kivy.uix.boxlayout import BoxLayout

class LoginPanel(BoxLayout):
    """Setup the main login panel.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # TODO: Add event handlers


class FilePanel(BoxLayout):
    """Setup the main file panel.
    """
    def __init__(self, **kwargs):
        super().__init__(padding=40, spacing=40, **kwargs)

    # TODO: Add event handlers

