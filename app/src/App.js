import './App.css';
import React from 'react';
import Home from './pages/Home'
import LeagueStandings from './pages/LeagueStandings';
import LeagueGoalLeadership from './pages/LeagueGoalLeadership';
import TeamSquad from "./pages/TeamSquad.js"
import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";
import LeagueAssistLeadership from './pages/LeagueAssistLeadership';

function App() {

  return (
    <Router>
      <Routes>
        <Route exact path="/" element={<Home />} />
        <Route path="/league/standings/:lid" element={<LeagueStandings />} />
        <Route path="/league/goalleadership/:lid" element={<LeagueGoalLeadership />} />
        <Route path="/league/assistleadership/:lid" element={<LeagueAssistLeadership />} />
        <Route path="/team/squad/:tid" element={<TeamSquad />} />
      </Routes>
    </Router>
  );




  
}

export default App;
