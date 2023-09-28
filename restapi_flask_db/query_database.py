from app import app, db, Item

# Initialize the app and database
app.app_context().push()

with app.app_context():
    items = Item.query.all()
    for item in items:
        print(f"Item ID: {item.id}, Name: {item.name}")