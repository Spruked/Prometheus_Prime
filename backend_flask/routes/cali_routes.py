from flask import Flask
from routes import cali_routes

app = Flask(__name__)
app.register_blueprint(cali_routes.bp)

if __name__ == "__main__":
    app.run(debug=True)