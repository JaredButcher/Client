"""Multimedia Extensible Git (MEG) Client Application

Git client for multimedia tasks and activities
"""

# SDL2 image processing seems to fail so use PIL
import os
os.environ['KIVY_IMAGE'] = 'pil'

# Import Kivy and set the minimum required version
import kivy
kivy.require('1.11.0')

# Import Kivy app
from kivy.app import App
from kivy.uix.label import Label

# Import MEG runtime
from internal.meg_runtime import Config
from internal.meg_runtime.plugins import Plugin, PluginManager

# MEG app
class MEGApp(App):
    """Multimedia Extensible Git (MEG) Client Application"""

    # Constructor
    def __init__(self, config = Config(), plugins = PluginManager()):
        """Application constructor"""
        # Initialize super class constructor
        super().__init__()
        # Create configuration
        self.config = config
        # Create plugin manager
        self.plugins = plugins

    # Build the application UI
    def build(self):
        """Build the application UI"""
        # Set the application title
        self.title = 'Multimedia Extensible Git'
        # Build the UI
        return Label(text='Multimedia Extensible Git')

# Run MEG app when executed directly
if __name__ == '__main__':
    MEGApp().run()
