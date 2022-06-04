import React, {useState, useEffect}  from "react";
import {useParams} from "react-router-dom";
import Fixture from "./Fixture.js";
import TeamHeader from "./TeamHeader.js";

function TeamFixture(){
    const {tid} = useParams();
    const [fixtureData, setFixtureData] = useState([{}])
    
    useEffect(() => {
        if(tid){
            fetch(`/teams/fixtures?tid=${tid}`).then(
                response => response.json()
                ).then(data=>setFixtureData(data))
        }
    }, []);    

    const fixturesResponse = fixtureData[0]
    
    return (
        <div >
            <TeamHeader tid={fixturesResponse.tid} title={fixturesResponse.team}></TeamHeader>
            <Fixture fixtures={fixturesResponse.fixtures}></Fixture>
        </div>
    )
    
}

export default TeamFixture;