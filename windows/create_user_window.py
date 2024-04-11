from typing import Iterable, Callable

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget


from ui import UiCreateNewUser_Form
from database import get_session, User


class UserCreate(QWidget, UiCreateNewUser_Form):
    def __init__(self, callbacks: Iterable[Callable]):
        super().__init__()
        self.callbacks = callbacks
        self.setupUi(self)
        self.session = get_session()
        self.pushButton.clicked.connect(self.create_user)

    def create_user(self):
        username_input = self.lineEdit.text()
        new_user = User(nickname=username_input)
        self.session.add(new_user)
        self.session.commit()
        self.close()

    def custom_close(self):
        for callback in self.callbacks:
            callback()
        self.close()
