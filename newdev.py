from database import Dev, Game, Category, get_session

session = get_session()
devs = [
    ["CD Projekt Red", "Poland", 1000],
    ["Valve", "USA", 360],
    ["Mojang Studios", "Sweden", 70],
    ["Riot Games", "USA", 2500],
    ["Epic Games", "USA", 2200]
]
for i in range(len(devs)):
    new_dev = Dev(title=(devs[i][0]), country=(devs[i][1]), state=(devs[i][2]))
    session.add(new_dev)
session.commit()
devs = session.query(Dev).all()
print(devs)
session.commit()

session.close()
