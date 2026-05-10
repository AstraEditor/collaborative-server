from textual.widgets import Input, Label
from textual.containers import VerticalGroup
from textual.app import ComposeResult
from textual import on

from ...i18n import i
from ....ids import server_setting
from .style import style
from ...base_screen import TUI_LAYOUT

from ....ws import __main__ as ws_main

class ManageScreen(TUI_LAYOUT):
    def content(self) -> ComposeResult:
        self.title = i("MANAGE_TITLE")
        
        yield Manage()

class Manage(VerticalGroup):
    """管理UI"""

    DEFAULT_CSS = style
    def __init__(self):
        super().__init__()
        self.run_worker(ws_main.main) # 运行ws服务器
                
    def compose(self) -> ComposeResult:
        yield Label(content = i("MANAGE_LABEL"),id = 'manage-label')
        
    @on(Input.Submitted, '#port-input')
    def handle_port_submitted(self, event: Input.Submitted) -> None:
        server_setting.SERVER_PORT = event.value
