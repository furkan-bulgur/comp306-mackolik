import './App.css';
import React from 'react';
import Home from './pages/Home'
import LeagueStandings from './pages/LeagueStandings';
import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";

function App() {

  return (
    <Router>
      <Routes>
        <Route exact path="/" element={<Home />} />
        <Route path="/league/standings/:lid" element={<LeagueStandings />} />
      </Routes>
    </Router>
  );




  
}

export default App;
