async function sendHelix() {
    const input = document.getElementById("input").value;
    const res = await fetch("/helix/run", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ input })
    });
    const data = await res.json();
    document.getElementById("response").textContent = JSON.stringify(data, null, 2);
}
