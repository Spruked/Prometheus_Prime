from flask import Flask
from routes import nft_routes, symbol_routes

app = Flask(__name__)

app.register_blueprint(nft_routes.bp)
app.register_blueprint(symbol_routes.bp)

if __name__ == "__main__":
    app.run(debug=True)
