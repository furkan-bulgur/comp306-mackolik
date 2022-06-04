import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import MatchHeader from "./MatchHeader.js";
import Statistics from "./Statistics.js";

function MatchStatistics(props) {
  const { mid } = useParams();
  const [homeData, setHomeData] = useState([{}]);
  const [awayData, setAwayData] = useState([{}]);

  useEffect(() => {
    function sleep(time) {
      return new Promise((resolve) => setTimeout(resolve, time));
    }

    const fetchHome = async () => {
      if (mid) {
        await fetch(`/matches/statistics/home?mid=${mid}`)
          .then((response) => response.json())
          .then((data) => setHomeData(data));
      }
    };

    const fetchAway = async () => {
      if (mid) {
        await fetch(`/matches/statistics/away?mid=${mid}`)
          .then((response) => response.json())
          .then((data) => setAwayData(data));
      }
    };

    fetchHome();
    //not a pretty solution but it works:)
    //i think two consecutive fast fetch request to mysql, makes it crash
    sleep(500).then(() => fetchAway());
  }, []);

  const homeResponse = homeData[0];
  const awayResponse = awayData[0];
  // console.log(JSON.stringify(homeResponse));
  console.log(JSON.stringify(awayResponse));
  // console.log("week:" + JSON.stringify(weekResponse));

  return (
    <div>
      <MatchHeader title={homeResponse.name}></MatchHeader>
      <Statistics home={homeResponse} away={awayResponse}></Statistics>
    </div>
  );
}

export default MatchStatistics;
