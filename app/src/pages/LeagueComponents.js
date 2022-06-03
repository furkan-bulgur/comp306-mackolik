import React from "react";
import { Link } from "react-router-dom";

function LeagueHeader(props) {
  return (
    <div className="header">
      <Link to={{
              pathname: `/`,
            }}>
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
      </ul>
    </div>
  );
}

function Standings(props) {
  if (props.standings) {
    return (
      <div className="league_table">
        <table>
          <thead>
            <tr>
              <th>Rank</th>
              <th>Team</th>
              <th>Played</th>
              <th>Won</th>
              <th>Draw</th>
              <th>Loss</th>
              <th>Goals For</th>
              <th>Goals Against</th>
              <th>Goal Diff</th>
              <th>Points</th>
            </tr>
          </thead>
          <tbody>
            {props.standings.map((standing) => (
              <tr key={standing.tid}>
                {Object.values(standing)
                  .slice(1)
                  .map((val, index) => {
                    if (index === 1) {
                      return (
                        <td>
                          <Link
                            to={{
                              pathname: `/team/squad/${standing.tid}`,
                            }}
                          >
                            {val}
                          </Link>
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

function GoalLeadership(props) {
  if (props.scorers) {
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
              <th>Goal Per Match</th>
            </tr>
          </thead>
          <tbody>
            {props.scorers.map((scorer, index) => (          
                                <tr key={scorer.pid}>
                                  <td>{index+1}</td>
                                    {Object.values(scorer).slice(2).map((val,inner) => {
                                        if(inner === 0){
                                          return (<td>
                                            <Link
                                              to={{
                                                pathname: `/team/squad/${scorer.tid}`,
                                              }}
                                            >
                                              {val}
                                            </Link>
                                          </td>);
                                        }else{
                                          return <td>{val}</td> 
                                        }
                                      })
                                    }
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

function AssistLeadership(props) {
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
                                  <td>{index+1}</td>
                                    {Object.values(assister).slice(2).map((val,inner) => {
                                        if(inner === 0){
                                          return (<td>
                                            <Link
                                              to={{
                                                pathname: `/team/squad/${assister.tid}`,
                                              }}
                                            >
                                              {val}
                                            </Link>
                                          </td>);
                                        }else{
                                          return <td>{val}</td> 
                                        }
                                      })
                                    }
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

export { LeagueHeader, Standings, GoalLeadership, AssistLeadership };
