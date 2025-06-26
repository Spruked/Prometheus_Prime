import React from "react";

export default function EchoStreamPanel({ stream = [] }) {
  return (
    <div className="panel echo-stream-panel">
      <h2>Echo Stream</h2>
      {stream.length === 0 ? (
        <div>No echo events yet.</div>
      ) : (
        <ul>
          {stream.map((echo, idx) => (
            <li key={idx}>
              <strong>{echo.context || `Event #${idx + 1}`}</strong>: {echo.output || echo}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}