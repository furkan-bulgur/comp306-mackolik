import React from "react";
import { useNavigate } from "react-router-dom";

function Standings(props) {
  const navigate = useNavigate();
  if (props.standings) {
    return (
      <div className="league_table">
        <table>
          <thead>
            <tr>
              <th>Rank</th>
              <th>Team</th>
              <th>Played</th>
              <th>Won</th>
              <th>Draw</th>
              <th>Loss</th>
              <th>Goals For</th>
              <th>Goals Against</th>
              <th>Goal Diff</th>
              <th>Points</th>
            </tr>
          </thead>
          <tbody>
            {props.standings.map((standing) => (
              <tr key={standing.tid}>
                {Object.values(standing)
                  .slice(1)
                  .map((val, index) => {
                    if (index === 1) {
                      return (
                        <td
                          className="navigatable"
                          onClick={() => {
                            navigate(`/team/squad/${standing.tid}`);
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

export default Standings;
