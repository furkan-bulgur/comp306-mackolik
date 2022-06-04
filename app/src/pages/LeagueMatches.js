import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import { LeagueHeader, Matches } from "./LeagueComponents.js";

function LeagueMatches(props) {
  const { lid, week } = useParams();
  const [matchData, setMatchData] = useState([{}]);
  const [weekData, setWeekData] = useState([{}]);

  useEffect(() => {
    function sleep(time) {
      return new Promise((resolve) => setTimeout(resolve, time));
    }

    const fetchWeeks = async () => {
      if (lid) {
        await fetch(`/leagues/weeks?lid=${lid}`)
          .then((response) => response.json())
          .then((data) => setWeekData(data));
      }
    };

    const fetchMatches = async () => {
      if (lid && week) {
        await fetch(`/leagues/fixtures?lid=${lid}&week=${week}`)
          .then((response) => response.json())
          .then((data) => setMatchData(data));
      }
    };

    fetchMatches();
    //not a pretty solution but it works:)
    //i think two consecutive fast fetch request to mysql, makes it crash
    sleep(500).then(() => fetchWeeks());
  }, [week]);

  const matchResponse = matchData[0];
  const weekResponse = weekData[0];
  const defaultWeek = 1;
  // console.log(JSON.stringify(matchResponse));
  // console.log("week:" + JSON.stringify(weekResponse));
  return (
    <div>
      <LeagueHeader
        lid={matchResponse.lid}
        title={matchResponse.name}
        week={defaultWeek}
      ></LeagueHeader>
      {weekResponse.weeks && (
        <Matches
          lid={matchResponse.lid}
          matches={matchResponse.fixtures}
          weeks={weekResponse.weeks[0].weeks}
        ></Matches>
      )}
    </div>
  );
}

export default LeagueMatches;
