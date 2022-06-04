import React from "react";
import { Link } from "react-router-dom";

function MatchHeader(props) {
  return (
    <div className="header">
      <Link
        to={{
          pathname: `/`,
        }}
      >
        Home
      </Link>
      <h1>{props.title}</h1>
      {props.homeResponse && props.awayResponse && (
        <h2>
          {props.homeResponse.team} {props.homeResponse.home_goals} - {props.awayResponse.away_goals} {props.awayResponse.team}
        </h2>
      )}
    </div>
  );
}

export default MatchHeader;
