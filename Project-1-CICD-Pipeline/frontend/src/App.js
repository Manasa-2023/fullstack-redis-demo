import React, { useState, useEffect } from "react";
import axios from "axios";


const API_BASE = "http://localhost:5000"; 


function App() {
  const [health, setHealth] = useState("loading...");
  const [counter, setCounter] = useState(0);

 useEffect(() => {
  axios.get(`${API_BASE}/health`)
    .then(res => setHealth(res.data.status))
    .catch(() => setHealth("unhealthy"));
}, []);

const handleClick = async () => {
  const res = await axios.get(`${API_BASE}/counter`);
  setCounter(res.data.counter);
};


  return (
    <div style={{ textAlign: "center", marginTop: "50px", fontFamily: "Arial" }}>
      <h1> Fullstack Redis Demo</h1>
      <p><b>Health Status:</b> {health}</p>
      <button
        onClick={handleClick}
        style={{ padding: "10px 20px", fontSize: "18px", cursor: "pointer" }}
      >
        Increment Counter
      </button>
      <p>Counter Value: <b>{counter}</b></p>
    </div>
  );
}

export default App;

