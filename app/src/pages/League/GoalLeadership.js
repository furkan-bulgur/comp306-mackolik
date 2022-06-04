import React from "react";
import { useNavigate } from "react-router-dom";

function GoalLeadership(props) {
  const navigate = useNavigate();
  if (props.scorers) {
    return (
      <div className="league_table">
        <table>
          <thead>
            <tr>
              <th>Rank</th>
              <th>Team</th>
              <th>Player Name</th>
              <th>Played Match</th>
              <th>Played Minutes</th>
              <th>Goals</th>
              <th>Assists</th>
              <th>Goal Per Match</th>
            </tr>
          </thead>
          <tbody>
            {props.scorers.map((scorer, index) => (
              <tr key={scorer.pid}>
                <td>{index + 1}</td>
                {Object.values(scorer)
                  .slice(2)
                  .map((val, inner) => {
                    if (inner === 0) {
                      return (
                        <td
                          className="navigatable"
                          onClick={() => {
                            navigate(`/team/squad/${scorer.tid}`);
                          }}
                        >
                          {val}
                        </td>
                      );
                    } else if (inner === 1) {
                      return (
                        <td
                          className="navigatable"
                          onClick={() => {
                            navigate(`/player/${scorer.pid}`);
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

export default GoalLeadership;
