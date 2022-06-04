import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import GoalLeadership from "./GoalLeadership";
import TeamHeader from "./TeamHeader";

function TeamGoalLeadership(props) {
  const { tid } = useParams();
  const [data, setData] = useState([{}]);

  useEffect(() => {
    if (tid) {
      fetch(`/teams/scorers?tid=${tid}`)
        .then((response) => response.json())
        .then((data) => setData(data));
    }
  }, []);

  const scorers = data[0];
  return (
    <div>
      <TeamHeader
        tid={scorers.tid}
        title={scorers.team}
      ></TeamHeader>
      <GoalLeadership scorers={scorers.scorers}></GoalLeadership>
    </div>
  );
}

export default TeamGoalLeadership;
