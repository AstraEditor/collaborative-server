from textual.widgets import Input, Label, DataTable
from textual.containers import VerticalGroup
from textual.app import ComposeResult
from textual import on, events

from ...i18n import i
from ....ids import SERVER_SETTING, SERVER_USERS
from .style import style
from ...base_screen import TUI_LAYOUT

from ....ws import __main__ as ws_main

class ManageScreen(TUI_LAYOUT):
    def content(self) -> ComposeResult: # type: ignore
        self.title = i("TITLE")
        
        yield Manage()

class Manage(VerticalGroup):
    """管理UI"""

    DEFAULT_CSS = style

    def __init__ (self):
        super().__init__()
        self.table = None
        self.tableColumnUSERNAME = None
        self.tableColumnUSERID = None
        
    def on_mount(self) -> None:
        self.__initTable()
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
    
    def __initTable(self) -> None:
        if not self.table: 
            self.table = self.query_one("#manage-members", DataTable)
        if not self.tableColumnUSERNAME: 
            self.tableColumnUSERNAME = self.table.add_column(i('USERNAME'))
            self.table.columns[self.tableColumnUSERNAME].auto_width = False
        if not self.tableColumnUSERID: 
            self.tableColumnUSERID = self.table.add_column(i('USERID'), width=14) #时间戳一般是13位，这里用14位吧
            self.table.columns[self.tableColumnUSERID].auto_width = False
            
    # 加载成员列表到DataTable
    def _loadAllMember(self) -> None:
        self.__initTable()
        self.table.clear() # type: ignore
        for user in SERVER_USERS:
            self.table.add_row( # type: ignore
                user['name'],
                user['_id']
            )
        self._refresh_width()
         
    def on_resize(self) -> None:
        self._refresh_width()
        
    def _refresh_width(self) -> None:
        if self.tableColumnUSERID and self.tableColumnUSERNAME and self.table:
            totalWidth = self.table.container_size.width
            # 设置USERNAME的宽度为 总宽度-20（ID的宽度14 + padding 6）
            self.table.columns[self.tableColumnUSERNAME].width = totalWidth - 20
            self.table.refresh()
            
    def on_data_table_cell_selected(self, event: DataTable.CellSelected) -> None:
        """当单元格被选中时调用"""
        # event.coordinate 包含了行和列的坐标
        self.action_notify (f"你点击了 [{event.coordinate.row}, {event.coordinate.column}]，值为：{event.value}")

    def compose(self) -> ComposeResult:
        yield DataTable(id = 'manage-members')
        
    @on(Input.Submitted, '#port-input')
    def handle_port_submitted(self, event: Input.Submitted) -> None:
        SERVER_SETTING["DEFAULTPORT"] = event.value
