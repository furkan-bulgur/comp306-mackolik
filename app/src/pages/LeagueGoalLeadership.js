import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import LeagueHeader from "./LeagueHeader.js";
import GoalLeadership from "./GoalLeadership.js";

function LeagueGoalLeadership(props) {
  const { lid } = useParams();
  const [data, setData] = useState([{}]);

  useEffect(() => {
    if (lid) {
      fetch(`/leagues/scorers?lid=${lid}`)
        .then((response) => response.json())
        .then((data) => setData(data));
    }
  }, []);

  const scorers = data[0];
  return (
    <div>
      <LeagueHeader lid={scorers.lid} title={scorers.name}></LeagueHeader>
      <GoalLeadership scorers={scorers.scorers}></GoalLeadership>
    </div>
  );
}

export default LeagueGoalLeadership;
