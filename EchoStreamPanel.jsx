import React, { useEffect, useState } from "react";

export default function EchoStreamPanel() {
  const [stream, setStream] = useState([]);

  useEffect(() => {
    const socket = new WebSocket("ws://localhost:8080/echo");
    socket.onmessage = (event) => {
      try {
        const payload = JSON.parse(event.data);
        setStream((prev) => [payload, ...prev.slice(0, 49)]);
      } catch (e) {
        // Optionally handle malformed messages
      }
    };
    return () => socket.close();
  }, []);

  return (
    <div className="bg-black p-4 rounded-md border border-indigo-800 shadow-lg max-h-[400px] overflow-y-auto">
      <h2 className="text-indigo-300 font-bold text-lg mb-3">Helix Echo Stream</h2>
      <ul className="font-mono text-sm text-green-300 space-y-2">
        {stream.map((item, i) => (
          <li key={i}>
            <span className="text-purple-400">
              {item.ts ? new Date(item.ts).toLocaleTimeString() : "--:--:--"}
            </span>{" "}
            • <span className="text-emerald-300">{item.symbol}</span> →
            <span className="ml-2 text-gray-400">{item.thought}</span>
          </li>
        ))}
      </ul>
    </div>
  );
}