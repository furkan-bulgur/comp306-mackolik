import React, {useState, useEffect}  from "react";
import {useParams} from "react-router-dom";
import {LeagueHeader, Standings} from "./LeagueComponents.js"

function LeagueStandings(){
    const {lid} = useParams();
    const [data, setData] = useState([{}])
    useEffect(() => {
        if(lid){
            fetch(`/leagues/standings?lid=${lid}`).then(
                response => response.json()
                ).then(data=>setData(data))
        }
    }, []);

    

    const league = data[0]
    return (
        <div >
            <LeagueHeader lid={league.lid} title={league.name}></LeagueHeader>
            <Standings standings={league.standings}></Standings>
        </div>
    )
    
    
}

export default LeagueStandings;