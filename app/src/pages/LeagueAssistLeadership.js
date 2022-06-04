import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import LeagueHeader from "./LeagueHeader.js";
import AssistLeadership from "./AssistLeadership.js";

function LeagueAssistLeadership(props) {
  const { lid } = useParams();
  const [data, setData] = useState([{}]);

  useEffect(() => {
    if (lid) {
      fetch(`/leagues/assisters?lid=${lid}`)
        .then((response) => response.json())
        .then((data) => setData(data));
    }
  }, []);

  const assisters = data[0];
  return (
    <div>
      <LeagueHeader lid={assisters.lid} title={assisters.name}></LeagueHeader>
      <AssistLeadership assisters={assisters.assisters}></AssistLeadership>
    </div>
  );
}

export default LeagueAssistLeadership;
