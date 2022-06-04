import React from "react";
import { useNavigate } from "react-router-dom";

function DisciplineTable(props) {
    const navigate = useNavigate();
    if (props.cards) {
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
                <th>Red Cards</th>
                <th>Yellow Cards</th>
                <th>Total Cards</th>
              </tr>
            </thead>
            <tbody>
                {props.cards.map((card, index) => (
                <tr key={card.pid}>
                    <td>{index + 1}</td>
                    {Object.values(card)
                    .slice(2)
                    .map((val, inner) => {
                        if (inner === 0) {
                        return (
                            <td
                            className="navigatable"
                            onClick={() => {
                                navigate(`/team/squad/${card.tid}`);
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

export default DisciplineTable;