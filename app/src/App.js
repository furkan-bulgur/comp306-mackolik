import './App.css';
import React, {useState, useEffect} from 'react';

function App() {
  const [initialData, setInitialData] = useState([{}])

  useEffect(() => {
    fetch("/api").then(
      response => response.json()
    ).then(data=>setInitialData(data))
  }, []);
  const teams = initialData.map((team) => team.name)
  return (
    <div className="App">
      <ul>{teams.map((team) => <li>{team}</li>)}</ul>
    </div>
  );
}

export default App;
