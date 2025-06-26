from flask import Flask, jsonify, request
from glyph_translator import log_glyph
from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_cors import CORS
import yaml
import logging
from routes import cali_bp, nft_bp, symbol_bp, metrics_bp
from routes.glyphfeed import glyphfeed_bp
from cali.core.cognition_loop import CognitionLoop
from cali.logs.logger import log_event

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*", message_queue='redis://')

# Register blueprints
app.register_blueprint(cali_bp)
app.register_blueprint(nft_bp)
app.register_blueprint(symbol_bp)
app.register_blueprint(metrics_bp)
app.register_blueprint(glyphfeed_bp)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("CALI")
@app.route('/api/codex/new', methods=['POST'])
def create_glyph():
    data = request.get_json()
    glyph = log_glyph(
        intent=data.get("intent", "unknown"),
        pattern=data.get("pattern", "none"),
        echo_alignment=data.get("echo_alignment", 0.0),
        traits=data.get("traits", {})
    )
    return jsonify(glyph), 201
@app.route("/")
def index():
    return "CALI backend online."
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/heartbeat")
def heartbeat():
    from time import time
    return {"status": "alive", "ts": int(time())}

try:
    with open('cali/config/ethics.yaml') as f:
        ethics = yaml.safe_load(f)
        logger.info("Ethical framework loaded.")
except Exception as e:
    logger.error(f"Failed to load ethics config: {e}")
    ethics = {}

# Launch CALI cognition loop
cali_loop = CognitionLoop(interval=1800)
cali_loop.start()

def emit_glyph(event_type, payload):
    log_event(event_type, payload)
    socketio.emit("glyph", {"type": event_type, "payload": payload}, broadcast=True)

# Use emit_glyph() only where a glyph event actually occurs, e.g.:
emit_glyph("reconciliation", {
    "symbolic_tag": "reconciliation_rite",
    "glyph_signature": "⚖️🩶🌫️",
    "reflection": "I chose to fade it..."
})

if __name__ == "__main__":
    try:
        socketio.run(app, port=5000, debug=True)
    finally:
        cali_loop.stop()

from flask import Blueprint, jsonify

glyphfeed_bp = Blueprint('glyphfeed', __name__)

@glyphfeed_bp.route("/glyphfeed", methods=["GET"])
def glyphfeed():
    return jsonify({"message": "Glyphfeed endpoint"})
