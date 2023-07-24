from flask_migrate import Migrate
from routes import app
from models import db

migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(debug=True)
