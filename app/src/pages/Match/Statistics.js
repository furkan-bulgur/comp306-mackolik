import React from "react";
import { Link, useNavigate, useParams } from "react-router-dom";

function Statistics(props) {
  if (props.home && props.away) {
    return (
      // <div>Statistics page</div>
      <div className="league_table">
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
            <tr>{props.home[0].team}</tr>
            {props.home.map((match) => (
              <tr key={match.mid}>
                {Object.values(match)
                  .slice(4)
                  .map((val, index) => {
                    return <td>{val}</td>;
                    // if (index === 1) {
                    //   return (
                    //     <td
                    //       onClick={() =>
                    //         navigate(`/team/squad/${match.home_tid}`)
                    //       }
                    //       className="navigatable"
                    //     >
                    //       {val}
                    //     </td>
                    //   );
                    // } else {
                    //   return <td>{val}</td>;
                    // }
                  })}
              </tr>
            ))}
            <tr>{props.away[0].team}</tr>
            {props.away.map((match) => (
              <tr key={match.mid}>
                {Object.values(match)
                  .slice(4)
                  .map((val, index) => {
                    return <td>{val}</td>;
                    // if (index === 1) {
                    //   return (
                    //     <td
                    //       onClick={() =>
                    //         navigate(`/team/squad/${match.home_tid}`)
                    //       }
                    //       className="navigatable"
                    //     >
                    //       {val}
                    //     </td>
                    //   );
                    // } else {
                    //   return <td>{val}</td>;
                    // }
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
