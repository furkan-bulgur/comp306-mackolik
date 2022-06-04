import React, {useState, useEffect}  from "react";
import {useParams} from "react-router-dom";
import LeagueHeader from "../League/LeagueHeader.js";

function TeamSquad(){
    const {tid} = useParams();
    const [data, setData] = useState([{}])
    
    // useEffect(() => {
    //     if(lid){
    //         fetch(`/leagues/standings?lid=${lid}`).then(
    //             response => response.json()
    //             ).then(data=>setData(data))
    //     }
    // }, []);

    

    const league = data[0]
    return (
        <div >
            <p>{tid}</p>
        </div>
    )
    
    
}

export default TeamSquad;