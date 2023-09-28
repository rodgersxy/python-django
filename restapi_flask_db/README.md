# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'
db = SQLAlchemy(app)

```
pip install Flask-SQLAlchemy
```
We create the database tables with ```db.create_all()``` inside the app context. You should run this line once to create the database schema. After running it, you can comment it out to prevent it from running again.
```
curl -X POST -H "Content-Type: application/json" -d '{"name": "New Item"}' http://127.0.0.1:5000/items
curl http://127.0.0.1:5000/items
curl -X PUT -H "Content-Type: application/json" -d '{"name": "Updated Item"}' http://127.0.0.1:5000/items/1
curl -X DELETE http://127.0.0.1:5000/items/1
```

### Python Script:

### You can write a Python script that uses SQLAlchemy to query and display the content of your SQLite database. Here's an example script that prints the items in your database

```
from app import app, db, Item

# Initialize the app and database
app.app_context().push()

with app.app_context():
    items = Item.query.all()
    for item in items:
        print(f"Item ID: {item.id}, Name: {item.name}")

```