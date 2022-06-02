import React from 'react';
import {Link} from "react-router-dom"

function LeagueHeader(props) {
    return (
    <div className="header">
        <h1>{props.title}</h1>
        <ul>
            <li>
                <Link to={{
                    pathname: `/league/standings/${props.lid}`,
                }}>
                    Standings
                </Link>
            </li>
        </ul>
    </div>
    );
}

function Standings(props) {
    if(props.standings){
        return (
            <div className='league_table'>
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
                                {Object.values(standing).slice(1).map((val) => (
                                    <td>{val}</td>
                                ))}
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
            );
    }
    else{
        return(<div></div>)
    }
}

export {
    LeagueHeader,
    Standings
}