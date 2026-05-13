from textual.widgets import Input, Label, DataTable
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
            work=ws_main.main(tui=self),
            exclusive=True
        ) # 运行ws服务器

    def _refresh_users(self) -> None:
        self.call_after_refresh(self._loadAllMember)
        
    def _notice_addANewUser(self) -> None:
        self.action_notify(message=i('a user is added!'))
    
    # 加载成员列表到DataTable
    def _loadAllMember(self) -> None:
        table = self.query_one("#manage-members", DataTable)
        table.add_column(i('USERNAME'), width=99999)
        table.add_column(i('USERID'), width=14) #时间戳一般是13位，这里用14位吧

        for user in SERVER_USERS:
            table.add_row(
                user['name'],
                user['_id']
            )
            # yield Label(content = user['name'],id = f"manage-users-{user['_id']}")
        
    def compose(self) -> ComposeResult:
        yield DataTable(id = 'manage-members')
        
    @on(Input.Submitted, '#port-input')
    def handle_port_submitted(self, event: Input.Submitted) -> None:
        SERVER_SETTING["DEFAULTPORT"] = event.value
