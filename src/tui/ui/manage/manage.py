from textual.widgets import Input, Label
from textual.containers import VerticalGroup
from textual.app import ComposeResult
from textual import on

from ...i18n import i
from ....ids import SERVER_SETTING, SERVER_USERS
from .style import style
from ...base_screen import TUI_LAYOUT

from ....ws import __main__ as ws_main

class ManageScreen(TUI_LAYOUT):
    def content(self) -> ComposeResult: # type: ignore
        self.title = i("MANAGE_TITLE")
        
        yield Manage()

class Manage(VerticalGroup):
    """管理UI"""

    DEFAULT_CSS = style

    def on_mount(self) -> None:
        self._run_server()

    def _run_server(self) -> None:
        self.run_worker(
            ws_main.main(self),
            exclusive=True
        ) # 运行ws服务器

    def _refresh_users(self) -> None:
        self.refresh(recompose=True)
                
    def compose(self) -> ComposeResult:
        yield Label(content = i("MANAGE_LABEL"),id = 'manage-label')
        for user in SERVER_USERS:
            yield Label(content = user['name'],id = f"manage-users-{user['_id']}")
        
        
    @on(Input.Submitted, '#port-input')
    def handle_port_submitted(self, event: Input.Submitted) -> None:
        SERVER_SETTING["DEFAULTPORT"] = event.value
