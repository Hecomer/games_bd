from PyQt5.QtWidgets import QWidget
from ui import UiPurchaseError


class PurchaseError(QWidget, UiPurchaseError):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda: self.close())
