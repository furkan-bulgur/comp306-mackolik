import React from "react";
import { Link, useNavigate, useParams } from "react-router-dom";

function Fixture(props) {
//   const { week } = useParams();
  const navigate = useNavigate();
  if (props.fixtures) {
    return (
      <div>
        {/* matches */}
        <div className="league_table">
          <table>
            <thead>
              <tr>
                <th>Date</th>
                <th>Home</th>
                <th>Final Score</th>
                <th>Away Team</th>
                <th>Referee</th>
              </tr>
            </thead>
            <tbody>
              {props.fixtures.map((match) => (
                <tr key={match.mid}>
                  {Object.values(match)
                    .slice(4)
                    .map((val, index) => {
                      // return <td>{val}</td>;
                      if (index === 1) {
                        return (
                          <td
                            onClick={() =>
                              navigate(`/team/squad/${match.home_tid}`)
                            }
                            className="navigatable"
                          >
                            {val}
                          </td>
                        );
                      } else if (index === 2) {
                        return (
                          <td
                            onClick={() => navigate(`/match/${match.mid}`)}
                            className="navigatable"
                          >
                            {val}
                          </td>
                        );
                      } else if (index === 3) {
                        return (
                          <td
                            onClick={() =>
                              navigate(`/team/squad/${match.away_tid}`)
                            }
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
      </div>
    );
  } else {
    return <div></div>;
  }
}

export default Fixture;
