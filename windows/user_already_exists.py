from PyQt5.QtWidgets import QWidget
from ui import UiUserAlreadyExists_Form


class UserAlreadyExists(QWidget, UiUserAlreadyExists_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda: self.close())
