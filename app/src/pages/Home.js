import React, {useState, useEffect}  from "react";
import "./Home.css"
import {
    Link
} from "react-router-dom";

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
            <ul>
                {props.leagues.map((league) => {
                    return (
                    <li key={'' + league.lid}>
                        <Link to={{
                            pathname: `/league/${league.lid}`,
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
        /* <div className="header">
            <h1>Comp 306 Term Project</h1>
            <h5>Gülay Canbaloğlu</h5>
            <h5>Murat Han Aydoğan</h5>
            <h5>Furkan Bulgur</h5>
            <h5>Burhan Özer Çavdar</h5>
            <h5>Talha Enes Güler</h5>
        </div> */
        <div className="league-list">
            <h1>Mini-Mackolik</h1>
            <Leagues leagues={leagues} />
        </div>   
    );
}

export default Home;