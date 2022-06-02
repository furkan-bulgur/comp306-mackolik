import React from 'react';
import {Link} from "react-router-dom"

function LeagueHeader(props) {
    return (
    <div>
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

export default LeagueHeader;