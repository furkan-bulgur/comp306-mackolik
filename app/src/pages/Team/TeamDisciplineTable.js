import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import DisciplineTable from "./DisciplineTable.js";
import TeamHeader from "./TeamHeader.js";

function TeamDisciplineTable(props) {
  const { tid } = useParams();
  const [data, setData] = useState([{}]);

  useEffect(() => {
    if (tid) {
      fetch(`/teams/cards?tid=${tid}`)
        .then((response) => response.json())
        .then((data) => setData(data));
    }
  }, []);

  const cards = data[0];
  return (
    <div>
      <TeamHeader tid={cards.tid} title={cards.team}></TeamHeader>
      <DisciplineTable cards={cards.cards}></DisciplineTable>
    </div>
  );
}

export default TeamDisciplineTable;
