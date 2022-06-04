import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import AssistLeadership from "./AssistLeadership.js";
import TeamHeader from "./TeamHeader.js";

function TeamAssistLeadership(props) {
  const { tid } = useParams();
  const [data, setData] = useState([{}]);

  useEffect(() => {
    if (tid) {
      fetch(`/teams/assisters?tid=${tid}`)
        .then((response) => response.json())
        .then((data) => setData(data));
    }
  }, []);

  const assisters = data[0];
  
  return (
    <div>
      <TeamHeader tid={assisters.tid} title={assisters.team}></TeamHeader>
      <AssistLeadership assisters={assisters.assisters}></AssistLeadership>
    </div>
  );
}

export default TeamAssistLeadership;
