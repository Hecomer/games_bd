from database import Game, Category, get_session

session = get_session()
games = [
    ["The Witcher 3: Wild Hunt", 30, 18, "NVIDIA GeForce GTX 660 / AMD Radeon HD 7870", "Intel CPU Core i5-2500K 3.3GHz / AMD CPU Phenom II X4 940", 6, 35, "Windows 7/8/10 (64-bit)", 13, 92, 2015, 1],
    ["Counter-Strike: Global Offensive", 0, 18, "NVIDIA GeForce 8600/9600GT / ATI/AMD Radeon HD2600/3600", "Intel Core 2 Duo E6600 / AMD Phenom X3 8750", 2, 15, "Windows® 7/Vista/XP", 11, 88, 2012, 2],
    ["Minecraft", 27, 10, "NVIDIA GeForce 9600GT / AMD Radeon HD 2400", "Intel Core i3-3210 3.2 GHz / AMD A8-7600 APU 3.1 GHz or equivalent", 4, 1, "Windows 7 and up", 14, 91, 2011, 3],
    ["League of Legends", 0.0, 10, "N/A", "2 GHz processor (supporting SSE2 instruction set or higher)", 2, 8, "Windows 7 (64-bit) or newer", 15, 80, 2009, 4],
    ["Fortnite", 0, 12, "Intel HD 4000", "Core i3 2.4 GHz", 4, 19.76, "Windows 7/8/10 64-bit", 12, 82, 2017, 5]
]
for i in range(len(games)):
    new_game = Game(title=(games[i][0]), price=(games[i][1]), pg=(games[i][2]), gpu=(games[i][3]), cpu=(games[i][4]), ram=(games[i][5]), disc_space=(games[i][6]), os=(games[i][7]), category_id=(games[i][8]), user_rating=(games[i][9]), year=(games[i][10]), dev_id=(games[i][11]))
    session.add(new_game)
session.commit()
devs = session.query(Game).all()
print(devs)
session.commit()

session.close()
