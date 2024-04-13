from PyQt5.QtWidgets import QWidget, QListWidgetItem, QTableWidgetItem

from ui import UiReview_Form
from database import get_session, User, Game, Category, Dev, Review


class Review_Class(QWidget, UiReview_Form):
    def __init__(self):
        super().__init__()
        self.create_window = None
        self.setupUi(self)
        self.session = get_session()
        self.item = QTableWidgetItem()
        self.pushButton.clicked.connect(self.send_review)

    def display_window_review(self):
        self.show()

    def send_review(self):
        text = self.textEdit.toPlainText()
        print(text)
        self.close()
        username_input = self.lineEdit.text()
        print(username_input)
        all_users = self.session.query(User).all()
        all_games = self.session.query(Game).all()
        user_target_id = 0
        for i in range(len(all_users)):
            user_check: User = self.session.query(User).get(i + 1)
            if user_check.nickname == username_input:
                user_target_id = i+1
        if user_target_id == 0:
            print("говна поешь")
        all_games_titles = []
        for i in range(len(all_games)):
            game_check: User = self.session.query(Game).get(i + 1)
            game_title = game_check.title
            all_games_titles.append(game_title)
        target_game_id = all_games_titles.index(self.item.text()) + 1
        last_review = self.session.query(Review).order_by(Review.id.desc()).first()
        new_review = Review(id=last_review.id+1, content=text, user_id=user_target_id, game_id=target_game_id)
        self.session.add(new_review)
        self.session.commit()
        self.session.close()


