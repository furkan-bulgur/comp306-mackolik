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
import TeamFixture from "./pages/Team/TeamFixture";
import TeamGoalLeadership from "./pages/Team/TeamGoalLeadership";
import TeamAssistLeadership from "./pages/Team/TeamAssistLeadership";
import TeamDisciplineTable from "./pages/Team/TeamDisciplineTable";
import PlayerInfo from "./pages/Player/PlayerInfo";

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
        <Route path="/team/fixture/:tid" element={<TeamFixture />} />
        <Route
          path="/team/goalleadership/:tid"
          element={<TeamGoalLeadership />}
        />
        <Route
          path="/team/assistleadership/:tid"
          element={<TeamAssistLeadership />}
        />
        <Route
          path="/team/disciplinetable/:tid"
          element={<TeamDisciplineTable />}
        />
        <Route path="/match/:mid" element={<MatchStatistics />} />
        <Route path="/player/:pid" element={<PlayerInfo />} />
      </Routes>
    </Router>
  );
}

export default App;
