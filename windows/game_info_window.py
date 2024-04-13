from PyQt5.QtWidgets import QWidget, QListWidgetItem, QTableWidgetItem

from ui import UiGame_info
from database import get_session, User, Game, Category, Dev


class Gameinfo(QWidget, UiGame_info):
    def __init__(self):
        super().__init__()
        self.create_window = None
        self.setupUi(self)
        self.session = get_session()
        self.item = QListWidgetItem()


    def display_window_info(self):
        self.update_table()
        self.show()

    def update_table(self):
        all_games = self.session.query(Game).order_by(Game.id).all()
        all_games_titles = []
        for i in range(len(all_games)):
            game_check: User = self.session.query(Game).get(i + 1)
            game_title = game_check.title
            all_games_titles.append(game_title)
        target_game_id = all_games_titles.index(self.item.text())+1
        target_game = self.session.query(Game).get(target_game_id)
        column_position = 1

        game_with_dev = self.session.query(Game, Dev).join(Dev).filter(Game.id == target_game_id).first()
        game_with_cat = self.session.query(Game, Category).join(Category).filter(Game.id == target_game_id).first()

        self.tableWidget.setItem(0, column_position, QTableWidgetItem(str(target_game.title)))
        self.tableWidget.setItem(1, column_position, QTableWidgetItem(str(target_game.price)))
        self.tableWidget.setItem(2, column_position, QTableWidgetItem(str(target_game.pg)))
        self.tableWidget.setItem(3, column_position, QTableWidgetItem(str(target_game.gpu)))
        self.tableWidget.setItem(4, column_position, QTableWidgetItem(str(target_game.cpu)))
        self.tableWidget.setItem(5, column_position, QTableWidgetItem(str(target_game.ram)))
        self.tableWidget.setItem(6, column_position, QTableWidgetItem(str(target_game.disc_space)))
        self.tableWidget.setItem(7, column_position, QTableWidgetItem(str(target_game.os)))
        self.tableWidget.setItem(8, column_position, QTableWidgetItem(str(game_with_cat[1].title)))
        self.tableWidget.setItem(9, column_position, QTableWidgetItem(str(target_game.user_rating)))
        self.tableWidget.setItem(10, column_position, QTableWidgetItem(str(target_game.year)))
        self.tableWidget.setItem(11, column_position, QTableWidgetItem(str(game_with_dev[1].title)))
