import React from "react";
import { Link } from "react-router-dom";



function Standings(props) {
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
                          <td>
                            <Link
                              to={{
                                pathname: `/team/squad/${standing.tid}`,
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

  export default Standings;