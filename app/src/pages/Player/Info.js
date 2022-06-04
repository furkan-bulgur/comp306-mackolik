import React from "react";

function Info(props) {
  if (props.infos) {
    return (
      // <div>Statistics page</div>
      <div className="league_table">
        <table>
          <thead>
            <tr>
              <th>Nation</th>
              <th>Height</th>
              <th>Weight</th>
              <th>Birthdate</th>
              <th>Age</th>
            </tr>
          </thead>
          <tbody>
            {props.infos.map((info, index) => (
              <tr key={index}>
                {Object.values(info)
                  .slice(2)
                  .map((val) => {
                    return <td>{val}</td>;
                  })}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    );
  }
}

export default Info;
