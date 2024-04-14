from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QListWidget, QMainWindow, QListWidgetItem, QWidget


from ui import UiStore
from database import get_session, Game, User, UserGame
from .create_user_window import UserCreate
from .purchase_window import Purchase
from .game_info_window import Gameinfo
from ui import UiUser_List


class UserList(QWidget, UiUser_List):
    def __init__(self):
        super().__init__()
        self.create_window = None
        self.item = QListWidgetItem()
        self.session = get_session()

    def display_window_user_list(self):
        self.setupUi(self)
        self.update_table()
        self.show()

    def update_table(self):
        all_users = self.session.query(User).all()
        all_games = self.session.query(Game).all()
        all_ugr = self.session.query(UserGame).all()
        all_nicknames = []
        for i in range(len(all_users)):
            user_check: User = self.session.query(User).get(i + 1)
            nick = user_check.nickname
            all_nicknames.append(nick)
        all_games_titles = []
        for i in range(len(all_games)):
            game_check: User = self.session.query(Game).get(i + 1)
            game_title = game_check.title
            all_games_titles.append(game_title)
        target_game_id = all_games_titles.index(self.item.text())+1
        for i in range(len(all_ugr)):
            if target_game_id == all_ugr[i].game_id:
                target_user_id = all_ugr[i].user_id
                user_write = self.session.query(UserGame, User).join(User).filter(UserGame.user_id == target_user_id).first()
                self.game_list.addItem(QListWidgetItem(str(user_write[1].nickname)))

