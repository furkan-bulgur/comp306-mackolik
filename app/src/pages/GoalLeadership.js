import React from "react";
import { Link } from "react-router-dom";

function GoalLeadership(props) {
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
                          <td>
                            <Link
                              to={{
                                pathname: `/team/squad/${scorer.tid}`,
                              }}
                            >
                              {val}
                            </Link>
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