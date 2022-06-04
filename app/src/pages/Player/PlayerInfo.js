import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import Info from "./Info.js";
import PlayerHeader from "./PlayerHeader.js";

function PlayerInfo(props) {
  const { pid } = useParams();
  const [playerData, setPlayerData] = useState([{}]);

  useEffect(() => {
    const fetchInfo = async () => {
      if (pid) {
        await fetch(`/players?pid=${pid}`)
          .then((response) => response.json())
          .then((data) => setPlayerData(data));
      }
    };

    fetchInfo();
  }, []);

  const playerResponse = playerData[0];

  return (
    <div>
      <PlayerHeader
        title={playerResponse.team}
        info={playerResponse.info}
      ></PlayerHeader>
      <Info infos={playerResponse.info}></Info>
    </div>
  );
}

export default PlayerInfo;
