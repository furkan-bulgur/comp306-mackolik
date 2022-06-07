import React, {useState, useEffect}  from "react";

function FunFacts(){
    const [data, setData] = useState([{}])
    

    useEffect(() => {
        function sleep(time) {
            return new Promise((resolve) => setTimeout(resolve, time));
        }

        const myfetch = async () => {await fetch("/funfacts").then(
            // response => console.log(response)
            response => response.json()
        ).then(data=>setData(data))}
        sleep(500).then(() => myfetch());
    }, []);
    
    const funfacts = data
    if(funfacts){
        return(
            <div className="funfacts">
                {funfacts.map(funfact => <FunFact explanation={funfact.explanation} table={funfact.result}></FunFact>)}
            </div>
        );
    }
}

function FunFact(props){

    if(props.explanation){
        return (
            <div className="funfact">
                <p>{props.explanation}</p>
                <table className="funfact-table">
                    <thead>
                        {Object.keys(props.table[0]).map(key => {
                            return (<th>{key.replaceAll("_", " ")}</th>)
                        })}
                    </thead>
                    <tbody>
                        {props.table.map(row => {
                            return (<tr>{Object.values(row).map(val => <td>{val}</td>)}</tr>)
                        })}
                    </tbody>
                </table>
            </div>
        )
    }
    
}

export default FunFacts;