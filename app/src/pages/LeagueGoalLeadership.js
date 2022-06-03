import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import { LeagueHeader, GoalLeadership } from "./LeagueComponents.js";

function LeagueGoalLeadership(props) {
  const { lid } = useParams();
  const [data, setData] = useState([{}]);

  useEffect(() => {
    if (lid) {
      fetch(`/leagues/standings?lid=${lid}`)
        .then((response) => response.json())
        .then((data) => setData(data));
    }
  }, []);

  const league = data[0];
  return (
    <div>
      <LeagueHeader lid={league.lid} title={league.name}></LeagueHeader>
      <GoalLeadership display={true}></GoalLeadership>
    </div>
  );
}

export default LeagueGoalLeadership;
