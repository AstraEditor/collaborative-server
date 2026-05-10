from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer

from .i18n import i


class TUI_LAYOUT(Screen):
    def __init__(self):
        super().__init__()
        self.title = i("TITLE")
        
    def compose(self) -> ComposeResult:
        yield Header()
        yield from self.content()
        yield Footer()
        
    def content(self):
        return []
