import React from "react";
import { Link } from "react-router-dom";

function TeamHeader(props) {
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
              pathname: `/team/squad/${props.tid}`,
            }}
          >
            Squad
          </Link>
        </li>
        <li>
          <Link
            to={{
              pathname: `/team/fixture/${props.tid}`,
            }}
          >
            Fixture
          </Link>
        </li>
        <li>
          <Link
            to={{
              pathname: `/team/goalleadership/${props.tid}`,
            }}
          >
            Goal Leadership
          </Link>
        </li>
        <li>
          <Link
            to={{
              pathname: `/team/assistleadership/${props.tid}`,
            }}
          >
            Assist Leadership
          </Link>
        </li>
        {/* <li>
          <Link
            to={{
              pathname: `/team/disciplinetable/${props.tid}`,
            }}
          >
            Discipline Table
          </Link>
        </li> */}
      </ul>
    </div>
  );
}

export default TeamHeader;