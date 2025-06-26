import React, { useEffect, useState } from "react";

export default function HelixLivePane() {
  const [loopState, setLoopState] = useState({
    depth: 0,
    mode: "standby",
    energy: 0,
    currentSymbol: "",
    alignmentShift: "neutral",
  });

  useEffect(() => {
    const socket = new WebSocket("ws://localhost:8080/helix");
    socket.onmessage = (event) => {
      try {
        const data = JSON.parse(event.data);
        setLoopState(data);
      } catch (e) {
        // Optionally handle malformed messages
      }
    };
    return () => socket.close();
  }, []);

  return (
    <div className="bg-neutral-950 text-white p-4 rounded border border-cyan-700 shadow-lg">
      <h2 className="text-cyan-300 font-bold mb-2">Recursive Loop Monitor</h2>
      <div className="grid grid-cols-2 gap-4 text-sm font-mono">
        <p>
          Loop Depth:{" "}
          <span className="text-emerald-400">{loopState.depth}</span>
        </p>
        <p>
          Mode: <span className="text-blue-400">{loopState.mode}</span>
        </p>
        <p>
          Symbol:{" "}
          <span className="text-yellow-400">{loopState.currentSymbol}</span>
        </p>
        <p>
          Alignment:{" "}
          <span className="text-pink-400">{loopState.alignmentShift}</span>
        </p>
        <p>
          Energy Level:{" "}
          <span className="text-orange-400">{loopState.energy}</span>
        </p>
      </div>
    </div>
  );
}