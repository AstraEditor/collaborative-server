from textual.widgets import Input, Label
from textual.containers import VerticalGroup
from textual.app import ComposeResult
from textual import on

from ...i18n import i
from ....ids import server_setting
from .style import style
from ...base_screen import TUI_LAYOUT

class PortScreen(TUI_LAYOUT):
    def content(self) -> ComposeResult: # type: ignore
        yield Port_input()

class Port_input(VerticalGroup):
    """端口输入UI"""
    
    DEFAULT_CSS = style
    def compose(self) -> ComposeResult:
        yield Label(content = i("PORT_LABEL"),id = 'port-label')
        yield Input(value=str(server_setting.SERVER_PORT),id = 'port-input')

    @on(Input.Submitted, '#port-input')
    def handle_port_submitted(self, event: Input.Submitted) -> None:
        server_setting.SERVER_PORT = event.value
