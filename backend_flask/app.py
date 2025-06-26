from flask import Flask
from flask_cors import CORS
from routes import cali_bp, nft_bp, symbol_bp, metrics_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(cali_bp)
app.register_blueprint(nft_bp)
app.register_blueprint(symbol_bp)
app.register_blueprint(metrics_bp)

@app.route("/heartbeat")
def heartbeat():
    from time import time
    return {"status": "alive", "ts": int(time())}

if __name__ == "__main__":
    app.run(port=5000, debug=True)
    print("Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)")