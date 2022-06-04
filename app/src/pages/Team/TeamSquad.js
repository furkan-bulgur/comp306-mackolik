import React, {useState, useEffect}  from "react";
import {useParams} from "react-router-dom";
import Squad from "./Squad.js";
import TeamHeader from "./TeamHeader.js";

function TeamSquad(){
    const {tid} = useParams();
    const [squadData, setSquadData] = useState([{}])
    
    useEffect(() => {
        if(tid){
            fetch(`/teams/players?tid=${tid}`).then(
                response => response.json()
                ).then(data=>setSquadData(data))
        }
    }, []);    

    const team = squadData[0]
    return (
        <div >
            <TeamHeader tid={team.tid} title={team.team}></TeamHeader>
            <Squad players={team.players}></Squad>
        </div>
    )
    
}

export default TeamSquad;