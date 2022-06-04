import React from "react";
import { Link, useNavigate, useParams } from "react-router-dom";

function Matches(props) {
    const {week} = useParams();
  const navigate = useNavigate();
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
            <p id="week_num">Week: {week}</p>
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
                            <td onClick={() => navigate(`/team/squad/${match.home_tid}`)} className='navigatable'>
                              {val}
                            </td>
                          );
                        } 
                        else if (index === 4) {
                            return (
                              <td onClick={() => navigate(`/team/squad/${match.away_tid}`)} className='navigatable'>
                                  {val}
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