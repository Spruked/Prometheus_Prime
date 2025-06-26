import React, { useEffect, useState } from "react";

const API_ROOT = "/api";

export const fetchMetrics = async () => {
  const res = await fetch(`${API_ROOT}/metrics`);
  return res.json();
};

export default function CaliMemory() {
  const [memories, setMemories] = useState([]);

  useEffect(() => {
    fetch("/api/cali/memory")
      .then((res) => res.json())
      .then((data) => setMemories(data.memories || []));
  }, []);

  return (
    <div className="bg-neutral-900 p-4 rounded border border-indigo-500 text-white shadow-md overflow-y-auto max-h-80">
      <h2 className="text-lg text-indigo-300 font-semibold mb-2">
        CALI Memory Trace
      </h2>
      <ul className="space-y-1 text-sm">
        {memories.map((entry, idx) => (
          <li key={idx} className="text-gray-300">
            <span className="text-indigo-400">
              {entry.ts
                ? new Date(entry.ts).toLocaleTimeString()
                : "--:--:--"}
            </span>
            : {entry.message || entry.content || JSON.stringify(entry)}
            {entry.pinned && <span className="ml-2 text-yellow-400">★</span>}
          </li>
        ))}
      </ul>
    </div>
  );
}

export function HelixLivePane() {
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
          Mode:{" "}
          <span className="text-blue-400">{loopState.mode}</span>
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

// Example usage in your dashboard component (e.g., MasterDashboard.jsx)
<section className="grid grid-cols-2 gap-6 mb-6">
  <SymbolFeed />
  <NFTPanel />
</section>