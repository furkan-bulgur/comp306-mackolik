import React from "react";
import { useNavigate } from "react-router-dom";

function Statistics(props) {
  const navigate = useNavigate();
  if (props.home && props.away) {
    return (
      // <div>Statistics page</div>
      <div className="league_table">
        <p className="match-team-name">{props.home[0].team}</p>
        <table>
          <thead>
            <tr>
              <th>Number</th>
              <th>Name</th>
              <th>Position</th>
              <th>Played Minutes</th>
              <th>Yellow Cards</th>
              <th>Red Cards</th>
              <th>Passes</th>
              <th>Total Shots</th>
              <th>On Shots</th>
              <th>Saves</th>
              <th>Conceded Goals</th>
              <th>Goals</th>
              <th>Assists</th>
              <th>Rating</th>
            </tr>
          </thead>
          <tbody>
            {/* <tr className="match-team-name">{props.home[0].team}</tr> */}
            {props.home.map((player) => (
              <tr key={player.mid}>
                {Object.values(player)
                  .slice(4)
                  .map((val, index) => {
                    // return <td>{val}</td>;
                    if (index === 1) {
                      return (
                        <td
                          onClick={() => navigate(`/player/${player.pid}`)}
                          className="navigatable"
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
        <p className="match-team-name">{props.away[0].team}</p>
        <table>
          <thead>
            <tr>
              <th>Number</th>
              <th>Name</th>
              <th>Position</th>
              <th>Played Minutes</th>
              <th>Yellow Cards</th>
              <th>Red Cards</th>
              <th>Passes</th>
              <th>Total Shots</th>
              <th>On Shots</th>
              <th>Saves</th>
              <th>Conceded Goals</th>
              <th>Goals</th>
              <th>Assists</th>
              <th>Rating</th>
            </tr>
          </thead>
          <tbody>
            {props.away.map((player) => (
              <tr key={player.mid}>
                {Object.values(player)
                  .slice(4)
                  .map((val, index) => {
                    // return <td>{val}</td>;
                    if (index === 1) {
                      return (
                        <td
                          onClick={() => navigate(`/player/${player.pid}`)}
                          className="navigatable"
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
  }
}

export default Statistics;
