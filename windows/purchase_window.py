from PyQt5.QtWidgets import QWidget, QListWidgetItem

from ui import UiPurchase
from database import get_session, User, Game, UserGame
from .purchase_error_window import PurchaseError


class Purchase(QWidget, UiPurchase):
    def __init__(self):
        super().__init__()
        self.create_window = None
        self.setupUi(self)
        self.session = get_session()
        self.item = QListWidgetItem()
        self.pushButton.clicked.connect(self.add_user_game_rel)

    def purchase_error_open(self):
        self.create_window = PurchaseError()
        self.create_window.show()

    def add_user_game_rel(self):
        username_input = self.lineEdit.text()
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
        if username_input in all_nicknames:
            user_ind = all_nicknames.index(username_input)
            game_ind = all_games_titles.index(self.item.text())
            flag = 0
            for ugr in all_ugr:
                if (ugr.game_id != game_ind+1) or (ugr.user_id != user_ind+1):
                    pass
                else:
                    flag = 1
            if flag != 1:
                new_ugr = UserGame(user_id=user_ind+1, game_id=game_ind+1)
                self.session.add(new_ugr)
                self.session.commit()
                self.close()
            else:
                self.purchase_error_open()

    def display_window_purchase(self):
        self.show()
