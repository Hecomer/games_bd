from database import Category, get_session

session = get_session()
categories = session.query(Category).all()
print(categories)
session.commit()

session.close()
