import React from 'react';
import logo from './logo.svg';
import './App.css';


const bridgeIP = "192.168.1.162";
const userId = "APIKEYHERE";
const lightId = "3"

const toggleLight = () => {
    const data = {
        "on":true,
        "sat": Math.floor(Math.random() * 254),
        "bri": Math.floor(Math.random() * 254),
        "hue": Math.floor(Math.random() * 10000)
    }

    fetch(`http://${bridgeIP}/api/${userId}/lights/${lightId}/state`, {
    method: 'PUT',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
})
}

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
	<button onClick={toggleLight}>Toggle Light</button>
      </header>
    </div>
  );
}

export default App;
