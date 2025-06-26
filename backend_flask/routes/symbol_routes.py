from flask import Flask
from routes import nft_routes, symbol_routes

app = Flask(__name__)
app.register_blueprint(nft_routes.bp)
app.register_blueprint(symbol_routes.bp)

from flask import Blueprint, jsonify, request

bp = Blueprint('symbol', __name__)

@bp.route("/api/symbol/feed", methods=["GET"])
def symbol_feed():
    # Example: Replace with your actual symbol feed logic
    feed = [
        {"symbol": "BTC", "price": 67000, "change": "+2.1%"},
        {"symbol": "ETH", "price": 3500, "change": "-0.5%"}
    ]
    return jsonify({"feed": feed})

@bp.route("/api/symbol/inject", methods=["POST"])
def symbol_inject():
    data = request.get_json()
    symbol = data.get("symbol")
    meaning = data.get("meaning")
    # Example: Replace with your actual injection logic
    return jsonify({
        "status": "success",
        "message": "Symbol injected.",
        "symbol": symbol,
        "meaning": meaning
    })