import React, {useState, useEffect}  from "react";
import {Link, useParams} from "react-router-dom";
import LeagueHeader from "./LeagueComponents.js"

function LeagueStandings(){
    const {lid} = useParams();
    const [data, setData] = useState([{}])
    console.log(data[0])
    useEffect(() => {
        console.log("here")
        if(lid){
            fetch(`/leagues/standings?lid=${lid}`).then(
                response => response.json()
                ).then(data=>setData(data))
        }
    }, []);

    function Standings(props) {
        console.log(props.standings)
        return (
        <div>
            <table>
                <tr>
                    {Object.keys(props.standings[0]).map((key) => {
                        return <th>{key}</th>
                    })}
                </tr>
            </table>
        </div>
        );
    }

    const league = data[0]
    console.log(league)
    return (
        <div className="header">
            <LeagueHeader lid={league.lid} title={league.name}></LeagueHeader>
            <Standings standings={league.standings}></Standings>
        </div>
    )
    
    
}

export default LeagueStandings;