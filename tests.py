from database import Category, get_session

session = get_session()
new_category = Category(title="Rockstar")
session.add(new_category)
categories = session.query(Category).all()
print(categories)
session.commit()

session.close()
