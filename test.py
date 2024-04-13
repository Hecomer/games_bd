from database import get_session, Game, Dev

session = get_session()

game_with_dev = session.query(Game, Dev).join(Dev).filter(Game.id == 1).first()
if game_with_dev:
    game, developer = game_with_dev
    print(f"Game: {game.title}, Developer: {developer.title}")
else:
    print("Game not found")
