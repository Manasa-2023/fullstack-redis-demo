const express = require("express");
const Redis = require("redis");
const cors = require("cors");

const app = express();
app.use(cors());

const redisClient = Redis.createClient({
  url: "redis://redis:6379"   // service name = redis
});

redisClient.connect().catch(console.error);

// Health check
app.get("/health", (req, res) => {
  if (redisClient.isOpen) {
    res.json({ status: "ok" });
  } else {
    res.status(500).json({ status: "error" });
  }
});

// Counter endpoint
app.get("/counter", async (req, res) => {
  try {
    let value = await redisClient.get("counter");
    if (!value) value = 0;
    value = parseInt(value) + 1;
    await redisClient.set("counter", value);
    res.json({ counter: value });
  } catch (err) {
    res.status(500).json({ error: "Failed to connect to Redis", details: err.message });
  }
});

// Start server
app.listen(3000, () => console.log("Backend running on port 3000"));
