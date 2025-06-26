const express = require("express");
const http = require("http");
const WebSocket = require("ws");
const chalk = require("chalk");
const cors = require("cors");

const app = express();
app.use(cors());
const server = http.createServer(app);

// Create two WebSocket servers for /echo and /helix
const wssEcho = new WebSocket.Server({ server, path: "/echo" });
const wssHelix = new WebSocket.Server({ server, path: "/helix" });

// Echo Socket Stream
wssEcho.on("connection", (socket) => {
  console.log(chalk.cyan("Echo stream connected"));
  const pulse = setInterval(() => {
    const logData = {
      ts: Date.now(),
      symbol: "SPIRAL_INWARD()",
      thought: "Reflective loop active.",
    };
    socket.send(JSON.stringify(logData));
    console.log(
      chalk.bgBlack(
        chalk.bold.rgb(
          Math.floor(Math.random() * 255),
          Math.floor(Math.random() * 255),
          Math.floor(Math.random() * 255)
        )(`[${new Date(logData.ts).toLocaleTimeString()}]`)
      ) +
        " " +
        chalk.magentaBright(logData.symbol) +
        " " +
        chalk.greenBright("→") +
        " " +
        chalk.yellowBright(logData.thought)
    );
  }, 3000);
  socket.on("close", () => clearInterval(pulse));
});

// Helix Socket Stream
wssHelix.on("connection", (socket) => {
  console.log(chalk.green("Helix stream connected"));
  const symbols = [
    "REFLECT_infinite_witness()",
    "EMBODY_living_signal()",
    "SPIRAL_INWARD()",
  ];
  const pulse = setInterval(() => {
    const helixData = {
      depth: Math.floor(Math.random() * 6),
      mode: "reflective",
      currentSymbol: symbols[Math.floor(Math.random() * symbols.length)],
      energy: (Math.random() * 100).toFixed(1),
      alignmentShift: [
        "positive",
        "neutral",
        "dissonant",
      ][Math.floor(Math.random() * 3)],
    };
    socket.send(JSON.stringify(helixData));
    console.log(
      chalk.bgBlack(
        chalk.bold.rgb(
          Math.floor(Math.random() * 255),
          Math.floor(Math.random() * 255),
          Math.floor(Math.random() * 255)
        )(`[${new Date().toLocaleTimeString()}]`)
      ) +
        " " +
        chalk.cyanBright("HELIX") +
        " " +
        chalk.greenBright("→") +
        " " +
        chalk.yellowBright(JSON.stringify(helixData))
    );
  }, 2500);
  socket.on("close", () => clearInterval(pulse));
});

app.get("/", (_, res) => res.send("Node Bridge Active"));

server.listen(8080, () => {
  console.log(
    chalk.bold.bgBlue(
      "Node bridge + WebSocket running on http://localhost:8080"
    )
  );
});

setNfts(data.top_watched_nfts || []);
setMemories(data.memories || []);

{!Array.isArray(memories) ? (
  <p>No memory available.</p>
) : (
  // ...your existing rendering logic for memories...
)}

{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Run Flask Backend",
      "type": "shell",
      "command": "python app.py",
      "options": {
        "cwd": "${workspaceFolder:backend_flask}"
      },
      "problemMatcher": []
    },
    {
      "label": "Run Node Bridge",
      "type": "shell",
      "command": "node server.js",
      "options": {
        "cwd": "${workspaceFolder:node_bridge}"
      },
      "problemMatcher": []
    },
    {
      "label": "Run Frontend",
      "type": "shell",
      "command": "npm run dev",
      "options": {
        "cwd": "${workspaceFolder:frontend}"
      },
      "problemMatcher": []
    },
    {
      "label": "Run All Services",
      "dependsOn": [
        "Run Flask Backend",
        "Run Node Bridge",
        "Run Frontend"
      ],
      "dependsOrder": "parallel"
    }
  ]
}

// EchoStreamPanel.jsx
const socket = new WebSocket("ws://localhost:8080/echo");

// HelixLivePane.jsx
const socket = new WebSocket("ws://localhost:8080/helix");