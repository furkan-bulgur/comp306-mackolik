import React from "react";
import { Link } from "react-router-dom";

function Matches(props) {
    if (props.matches && props.weeks) {
      const weekArray = [...Array(props.weeks + 1).keys()].slice(1);
      return (
        //week numbers
        <div>
          <div className="league_table">
            <ul>
              {weekArray.map((i) => {
                return (
                  <li
                    style={{
                      display: "inline-block",
                      margin: "auto",
                      border: "0.5px solid #023e8a",
                      padding: "0.5em",
                      width: "1.5em",
                    }}
                  >
                    <Link
                      to={{
                        pathname: `/league/matches/${props.lid}/${i}`,
                      }}
                    >
                      {i}
                    </Link>
                  </li>
                );
              })}
            </ul>
          </div>
          {/* matches */}
          <div className="league_table">
            <table>
              <thead>
                <tr>
                  <th>Date</th>
                  <th>Home</th>
                  <th>Home Score</th>
                  <th>Away Score</th>
                  <th>Away Team</th>
                  <th>Referee</th>
                </tr>
              </thead>
              <tbody>
                {props.matches.map((match) => (
                  <tr key={match.mid}>
                    {Object.values(match)
                      .slice(4)
                      .map((val, index) => {
                        // return <td>{val}</td>;
                        if (index === 1) {
                          return (
                            <td>
                              <Link
                                to={{
                                  pathname: `/team/squad/${match.home_tid}`,
                                }}
                              >
                                {val}
                              </Link>
                            </td>
                          );
                        } else if (index === 4) {
                            return (
                              <td>
                                <Link
                                  to={{
                                    pathname: `/team/squad/${match.away_tid}`,
                                  }}
                                >
                                  {val}
                                </Link>
                              </td>
                            );
                        }
                        else {
                          return <td>{val}</td>;
                        }
                      })}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
          
        </div>
      );
    } else {
      return <div></div>;
    }
  }

export default Matches;