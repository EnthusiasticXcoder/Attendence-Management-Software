
try :
    from views.widgets import (
        ToggelMenu as ToggelMenu,
        CreateSheet as CreateSheet,
        CreateNewUser as CreateNewUser,
        EnterAttendence as EnterAttendence,
        DeleteUser as DeleteUser,
        ChangePassword as ChangePassword,
        AttendenceListView as AttendenceListView,
        DownloadListView as DownloadListView,)
except ModuleNotFoundError :
    from widgets import (
        ToggelMenu as ToggelMenu,
        CreateSheet as CreateSheet,
        CreateNewUser as CreateNewUser,
        EnterAttendence as EnterAttendence,
        DeleteUser as DeleteUser,
        ChangePassword as ChangePassword,
        AttendenceListView as AttendenceListView,
        DownloadListView as DownloadListView,)