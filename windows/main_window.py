from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


from ui import UiMainWindow, UiCreateNewUser_Form
from database import get_session
from .create_user_window import UserCreate


class MainWindow(QMainWindow, UiMainWindow):
    def __init__(self):
        super().__init__()
        self.create_window = None
        self.setupUi(self)
        self.session = get_session()
        self.new_user_button.clicked.connect(self.open_user_create)

    def open_user_create(self):
        self.create_window = UserCreate(self)
        self.create_window.show()
