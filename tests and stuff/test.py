from database import get_session, Game, Dev, User, UserGame

session = get_session()

all_users = session.query(User).all()
all_games = session.query(Game).all()
all_ugr = session.query(UserGame).all()
all_nicknames = []
for i in range(len(all_users)):
    user_check: User = session.query(User).get(i + 1)
    nick = user_check.nickname
    all_nicknames.append(nick)
all_games_titles = []
for i in range(len(all_games)):
    game_check: User = session.query(Game).get(i + 1)
    game_title = game_check.title
    all_games_titles.append(game_title)

target_game_id = 2
for i in range(len(all_ugr)):
    if target_game_id == all_ugr[i].game_id:
        target_user_id = all_ugr[i].user_id
        user_write = session.query(UserGame, User).join(User).filter(UserGame.user_id == target_user_id).first()
        print(user_write[1].nickname, "111111111111111")
