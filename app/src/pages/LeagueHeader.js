import React from "react";
import { Link } from "react-router-dom";

function LeagueHeader(props) {
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
      <ul>
        <li>
          <Link
            to={{
              pathname: `/league/standings/${props.lid}`,
            }}
          >
            Standings
          </Link>
        </li>
        <li>
          <Link
            to={{
              pathname: `/league/matches/${props.lid}/1`,
            }}
          >
            Fixture
          </Link>
        </li>
        <li>
          <Link
            to={{
              pathname: `/league/goalleadership/${props.lid}`,
            }}
          >
            Goal Leadership
          </Link>
        </li>
        <li>
          <Link
            to={{
              pathname: `/league/assistleadership/${props.lid}`,
            }}
          >
            Assist Leadership
          </Link>
        </li>
        <li>
          <Link
            to={{
              pathname: `/league/disciplinetable/${props.lid}`,
            }}
          >
            Discipline Table
          </Link>
        </li>
      </ul>
    </div>
  );
}

export default LeagueHeader;