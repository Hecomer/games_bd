from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QListWidget, QMainWindow, QListWidgetItem, QWidget


from ui import UiStore
from database import get_session, Game
from .create_user_window import UserCreate
from .purchase_window import Purchase
from .game_info_window import Gameinfo
from .user_list import UserList


class Store(QMainWindow, UiStore):
    def __init__(self):
        super().__init__()
        self.create_window = None
        self.setupUi(self)
        self.session = get_session()
        self.update_table()
        self.game_list.itemClicked.connect(self.list_cell_clicked)
        self.buy_button.clicked.connect(self.passing_cell_purchase)
        self.info_button.clicked.connect(self.passing_cell_game_info)
        self.users_button.clicked.connect(self.passing_cell_user_list)
        self.purchase_window_pass = Purchase()
        self.game_info_window_pass = Gameinfo()
        self.user_list_pass = UserList()

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

    def passing_cell_purchase(self):
        self.purchase_window_pass.item.setText(self.currentItem.text())
        self.purchase_window_pass.display_window_purchase()

    def passing_cell_game_info(self):
        self.game_info_window_pass.item.setText(self.currentItem.text())
        self.game_info_window_pass.display_window_info()

    def passing_cell_user_list(self):
        self.user_list_pass.item.setText(self.currentItem.text())
        self.user_list_pass.display_window_user_list()

    def open_review(self):
        None

    def open_info(self):
        None
        #self.create_window = UserCreate(self)
        #self.create_window.show()

    def open_users(self):
        None
