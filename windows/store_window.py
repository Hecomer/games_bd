from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QListWidget, QMainWindow, QListWidgetItem, QWidget


from ui import UiStore
from database import get_session, Game
from .create_user_window import UserCreate
from .purchase_window import Purchase


class Store(QMainWindow, UiStore):
    def __init__(self):
        super().__init__()
        self.create_window = None
        self.setupUi(self)
        self.session = get_session()
        self.update_table()
        self.game_list.itemClicked.connect(self.list_cell_clicked)
        self.buy_button.clicked.connect(self.passing_cell)
        self.purchase_window = Purchase()

    def open_user_create(self):
        self.create_window = UserCreate(self)
        self.create_window.show()

    def list_cell_clicked(self, item):
        self.currentItem = item
        print(self.currentItem.text()) #УРА БЬЛЯТЬ

    def update_table(self):
        games = self.session.query(Game).order_by(Game.id).all()
        for game in games:
            self.game_list.addItem(QListWidgetItem(str(game.title)))

    def passing_cell(self):
        self.purchase_window.item.setText(self.currentItem.text())
        self.purchase_window.display_window()

    def open_review(self):
        None

    def open_info(self):
        None
        #self.create_window = UserCreate(self)
        #self.create_window.show()

    def open_users(self):
        None
