"""主TUI"""
from textual.app import App
from textual.widgets import Input
from textual import on

from .i18n import i

from .ui.port.port import PortScreen
from .ui.manage.manage import ManageScreen

from . import page

class TUI(App):
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]
    
    def __init__(self):
        super().__init__()
        self.current_page = page.PAGE

    async def on_mount(self) -> None:
        self._update_tab()
      
    def _update_tab(self) -> None:
        match self.current_page:
            case "port":
                self.push_screen(PortScreen())
            case "manage":
                self.push_screen(ManageScreen())
            case _:
                self.pop_screen()
        
    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )
        
    @on(Input.Submitted, '#port-input')
    def handle_port_submitted(self) -> None:
        page.PAGE = "manage"
        self.current_page = page.PAGE
        self._update_tab()
