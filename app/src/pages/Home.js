import React, {useState, useEffect}  from "react";
import {
    Link
} from "react-router-dom";
import FunFacts from "./FunFacts";
import gpp from "../photos/gpp.png";
import fpp from "../photos/fpp.png";
import bpp from "../photos/bpp.png";
import mpp from "../photos/mpp.png";
import tpp from "../photos/tpp.png";

function Home (){
    const [data, setData] = useState([{}])

    useEffect(() => {
        fetch("/leagues").then(
        response => response.json()
        ).then(data=>setData(data))
    }, []);
    
    const leagues = data
    //console.log(leagues);
    
    function Leagues(props) {
        return (
        <div>
            <h1>{props.title}</h1>
            <ul>
                {props.leagues.map((league) => {
                    return (
                    <li key={'' + league.lid}>
                        <Link to={{
                            pathname: `/league/standings/${league.lid}`,
                        }}>
                            {league.name}
                        </Link>
                    </li>
                    )})}
            </ul>
        </div>
        );
    }

    return(
        
        <div className="root">
            <div className="header">
                <Leagues leagues={leagues} title="Mini Mackolik"/>
            </div> 
            <h2>Fun Facts</h2>
            <FunFacts></FunFacts>
            <div className="footer">
            <h3>Comp 306 Term Project</h3>
            <div className="student"><p>Gülay Canbaloğlu </p><img src={gpp} /></div>
            <div className="student"><p>Murat Han Aydoğan </p><img src={mpp} /></div>
            <div className="student"><p>Furkan Bulgur </p><img src={fpp} /></div>
            <div className="student"><p>Burhan Özer Çavdar </p><img src={bpp} /></div>
            <div className="student"><p>Talha Enes Güler </p><img src={tpp} /></div>

        </div> 
        </div>
    );
}

export default Home;