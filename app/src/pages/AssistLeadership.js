import React from "react";
import { useNavigate } from "react-router-dom";

function AssistLeadership(props) {
  const navigate = useNavigate();
  if (props.assisters) {
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
              <th>Assists Per Match</th>
            </tr>
          </thead>
          <tbody>
            {props.assisters.map((assister, index) => (
              <tr key={assister.pid}>
                <td>{index + 1}</td>
                {Object.values(assister)
                  .slice(2)
                  .map((val, inner) => {
                    if (inner === 0) {
                      return (
                        <td
                          className="navigatable"
                          onClick={() => {
                            navigate(`/team/squad/${assister.tid}`);
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

export default AssistLeadership;
