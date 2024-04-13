from database import Game, Category, get_session

session = get_session()
cats = [
    "Battle Royal",
    "Action-RPG",
    "Sandbox",
    "MOBA"
]
for i in range(len(cats)):
    new_category = Category(title=(cats[i]))
    session.add(new_category)
session.commit()
categories = session.query(Category).all()
print(categories)
session.commit()

session.close()
