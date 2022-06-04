import React from "react";
import { Link } from "react-router-dom";

function PlayerHeader(props) {
  return (
    <div className="header">
      <Link
        to={{
          pathname: `/`,
        }}
      >
        Home
      </Link>
      {props.info && <h1>{props.info[0].name}</h1>}
      <h2>{props.title}</h2>
    </div>
  );
}

export default PlayerHeader;
