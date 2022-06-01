import './App.css';
import React from 'react';
import Home from './pages/Home'
import League from './pages/League';
import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";

function App() {

  return (
    <Router>
      <Routes>
        <Route exact path="/" element={<Home />} />
        <Route exact path="/league/:lid" element={<League />} />
      </Routes>
    </Router>
  );




  
}

export default App;
