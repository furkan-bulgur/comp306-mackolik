import React from "react";
import { useNavigate } from "react-router-dom";

function Squad(props) {
  const navigate = useNavigate();
  if (props.players) {
    return (
      <div className="league_table">
        <table>
          <thead>
            <tr>
              <th>Number</th>
              <th>Position</th>
              <th>Nation</th>
              <th>Name</th>
              <th>Age</th>
              <th>Played Match</th>
              <th>Played Min.</th>
              <th>Goals</th>
              <th>Assists</th>
              <th>Yellow Cards</th>
              <th>Red Cards</th>
              <th>Total Shots</th>
              <th>On Shots</th>
              <th>Saves</th>
              <th>Conceded Goals</th>
              <th>Avg. Rating</th>
            </tr>
          </thead>
          <tbody>
            {props.players.map((player) => (
              <tr key={player.pid}>
                {Object.values(player)
                  .slice(1)
                  .map((val, index) => {
                    // return <td>{val}</td>;
                    if (index === 3) {
                      return (
                        <td
                          className="navigatable"
                          onClick={() => {
                            navigate(`/player/${player.pid}`);
                          }}
                        >
                          {val}
                        </td>
                      );
                    } else {
                      return <td>{val}</td>;
                    }
                  })}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    );
  } else {
    return <div></div>;
  }
}

export default Squad;