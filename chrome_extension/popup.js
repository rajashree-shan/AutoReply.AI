document.getElementById("run-btn").addEventListener("click", async () => {
    const statusEl = document.getElementById("status");
    statusEl.innerText = "Processing...";
  
    try {
      const res = await fetch("https://autoreply-ai.onrender.com/process-emails", {
        method: "GET",
        headers: {
          "x-token": "your-secret-token"
        }
      });
  
      const data = await res.json();
      statusEl.innerText = "✅ " + data.status;
    } catch (err) {
      console.error(err);
      statusEl.innerText = "❌ Error contacting backend";
    }
  });
  