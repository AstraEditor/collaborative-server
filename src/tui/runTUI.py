"""主TUI"""
from textual.app import App, ComposeResult
from textual.widgets import Footer, Header

from .i18n import i

class TUI(App):
    """A Textual app to manage websocket."""

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]
    
    def __init__(self):
        super().__init__()
        
        self.title = i("TITLE") 
        
    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )