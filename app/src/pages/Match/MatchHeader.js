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
    </div>
  );
}

export default MatchHeader;
