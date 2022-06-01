import React, {useState, useEffect}  from "react";
import "./League.css";
import {useParams} from "react-router-dom";

function League(){
    const {lid} = useParams();
    const [data, setData] = useState([{}])

    useEffect(() => {
        if(lid){
            fetch(`/leagues?lid=${lid}`).then(
                response => response.json()
                ).then(data=>setData(data))
        }
    }, []);

    const league = data[0]
    return (
        <div>
            <h1>
                {league.name}
            </h1>
            <p>{league.country}</p>
            <p>Start Date: {league.start_date}</p>
            <p>End Date: {league.end_date}</p>
        </div>
    )
}

export default League;