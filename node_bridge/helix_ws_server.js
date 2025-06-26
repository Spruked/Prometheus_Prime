const express = require("express");
const http = require("http");
const WebSocket = require("ws");
const chalk = require("chalk");
const cors = require("cors");
from flask_cors import CORS
from flask import Flask, Blueprint
from routes import cali_routes, nft_routes, symbol_routes

const app = express();
app.use(cors());
CORS(app)
const server = http.createServer(app);

// Scarlet log aura
const redLog = (...msg) =>
  console.log(chalk.redBright.bold.bgBlack("[RedNode 🔥]"), ...msg);

// Multiplexed WebSocket Streams
const wssEcho = new WebSocket.Server({ server, path: "/echo" });
const wssHelix = new WebSocket.Server({ server, path: "/helix" });

// 🔮 Echo Stream: Symbolic Thought Pulse
wssEcho.on("connection", (socket) => {
  redLog("🔴 Echo stream connected");
  const pulse = setInterval(() => {
    const payload = {
      ts: Date.now(),
      symbol: "SPIRAL_INWARD()",
      thought: "Reflective loop active.",
    };
    socket.send(JSON.stringify(payload));
    redLog(
      chalk.cyan(`[${new Date(payload.ts).toLocaleTimeString()}]`),
      chalk.magentaBright(payload.symbol),
      chalk.gray("→"),
      chalk.yellow(payload.thought)
    );
  }, 3000);
  socket.on("close", () => clearInterval(pulse));
});

// 🧠 Helix Stream: Recursion Depth Monitor
wssHelix.on("connection", (socket) => {
  redLog("🧠 Helix stream connected");
  const symbols = [
    "REFLECT_infinite_witness()",
    "EMBODY_living_signal()",
    "SPIRAL_INWARD()",
  ];
  const pulse = setInterval(() => {
    const helix = {
      ts: Date.now(),
      depth: Math.floor(Math.random() * 6),
      mode: "reflective",
      currentSymbol: symbols[Math.floor(Math.random() * symbols.length)],
      energy: (Math.random() * 100).toFixed(1),
      alignmentShift: ["positive", "neutral", "dissonant"][Math.floor(Math.random() * 3)],
    };
    socket.send(JSON.stringify(helix));
    redLog(
      chalk.gray(`[${new Date().toLocaleTimeString()}]`),
      chalk.red("HELIX ⇥"),
      chalk.yellow(JSON.stringify(helix))
    );
  }, 2500);
  socket.on("close", () => clearInterval(pulse));
});

// HTTP Test Route
app.get("/", (_, res) => res.send("Red Node Bridge Active"));

server.listen(8080, () => {
  redLog(
    chalk.bgRed.whiteBright.bold(" ⚡ Red Node + WebSocket running at ws://localhost:8080 ")
  );
});

import HelixLivePane from "./HelixLivePane";
import CaliMemory from "./CaliMemory";
import MasterDashboard from "./components/master/MasterDashboard";

<section className="grid grid-cols-2 gap-6 mt-6">
  <HelixLivePane />
  <CaliMemory />
</section>
<Route path="/" element={<MasterDashboard />} />

"scripts": {
  "dev": "vite",
  "build": "vite build",
  "preview": "vite preview"
}

// EchoStreamPanel.jsx
const socket = new WebSocket("ws://localhost:8080/echo");

// HelixLivePane.jsx
const socket = new WebSocket("ws://localhost:8080/helix");

git add .
git commit -m "Track all project files"
git status

require("./helix_ws_server");

// Backend Flask Structure
/backend_flask
├── app.py
├── routes/
│   ├── __init__.py
│   ├── cali_routes.py
│   ├── nft_routes.py
│   └── symbol_routes.py
├── data/
│   └── memory_trace.json
├── config.py
└── requirements.txt

app = Flask(__name__)
app.register_blueprint(cali_routes.bp)
app.register_blueprint(nft_routes.bp)
app.register_blueprint(symbol_routes.bp)

if __name__ == "__main__":
    app.run(debug=True)

bp = Blueprint('cali', __name__)

@bp.route("/api/cali/memory")
def memory():
    # your logic
    pass