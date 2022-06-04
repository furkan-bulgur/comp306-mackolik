import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import LeagueHeader from "./LeagueHeader.js";
import DisciplineTable from "./DisciplineTable.js";

function LeagueDisciplineTable(props) {
  const { lid } = useParams();
  const [data, setData] = useState([{}]);

  useEffect(() => {
    if (lid) {
      fetch(`/leagues/cards?lid=${lid}`)
        .then((response) => response.json())
        .then((data) => setData(data));
    }
  }, []);

  const cards = data[0];
  return (
    <div>
      <LeagueHeader lid={cards.lid} title={cards.name}></LeagueHeader>
      <DisciplineTable cards={cards.cards}></DisciplineTable>
    </div>
  );
}

export default LeagueDisciplineTable;
