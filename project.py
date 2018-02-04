from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem
app = Flask(__name__)

engine = create_engine('sqlite:///FullStackFoundations/restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/restaurants/<int:restaurant_id>/')
def reastaurantMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id = restaurant.id)
    output = ''
    for item in items:
        output += item.name
        output += '</br>'
        output += item.price
        output += '</br>'
        output += item.description
        output += '</br>'
       
    return output
@app.route('/restaurants/<int:restaurant_id>/new/')
def newMenuItem(restaurant_id):
    return "page to create new restaurant menu"

@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit/')
def editMenuItem(restaurant_id, menu_id):
    return "page to edit restaurant item"

@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete/')
def deleteMenuItem(restaurant_id, menu_id):
    return "page to del new restaurant item"


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=5000)