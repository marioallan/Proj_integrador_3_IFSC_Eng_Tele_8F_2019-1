from config import app
from routes import routes

# Add blueprints
app.register_blueprint(routes)

if __name__ == '__main__':
    app.run()
