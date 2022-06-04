import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import "./App.css";
import React from "react";
import Home from "./pages/Home";
import LeagueStandings from "./pages/League/LeagueStandings";
import LeagueGoalLeadership from "./pages/League/LeagueGoalLeadership";
import LeagueAssistLeadership from "./pages/League/LeagueAssistLeadership";
import LeagueMatches from "./pages/League/LeagueMatches";
import LeagueDisciplineTable from "./pages/League/LeagueDisciplineTable";
import TeamSquad from "./pages/Team/TeamSquad.js";
import MatchStatistics from "./pages/Match/MatchStatistics";

function App() {
  return (
    <Router>
      <Routes>
        <Route exact path="/" element={<Home />} />
        <Route path="/league/standings/:lid" element={<LeagueStandings />} />
        <Route
          path="/league/goalleadership/:lid"
          element={<LeagueGoalLeadership />}
        />
        <Route
          path="/league/assistleadership/:lid"
          element={<LeagueAssistLeadership />}
        />
        <Route path="/league/matches/:lid/:week" element={<LeagueMatches />} />
        <Route
          path="/league/disciplinetable/:lid"
          element={<LeagueDisciplineTable />}
        />
        <Route path="/team/squad/:tid" element={<TeamSquad />} />
        <Route path="/match/:mid" element={<MatchStatistics />} />
      </Routes>
    </Router>
  );
}

export default App;
