from database import User, Game, Category, get_session

session = get_session()
all_users: User = session.query(User).get(1)
print("11111 ", all_users.nickname)

session.close()
