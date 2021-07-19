import logo from './logo.svg';
import React from 'react'
import './App.css';
import HelloWorld from './Components/HelloWorld'
import Header from '/Components/Header'
import Footer from '/Components/Footer' 
import CounterExample from './Components/CounterExample'

import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
}  from "react-router-dom";

function App() {
  return (
    <div>
    

    <Router>

    <Header/>
      <HelloWorld name=" Marsian"/> 

     <ul>
       <li>
         <Link to="/"className="text-blue-500">Home</Link>
        </li> 
      
      <li>
         <Link to="/"className="text-blue-500">About</Link>
        </li> 

        </ul>  

      <Switch>
        <Route path="/"></Route>
        <h1 className="font-bold text-2xl">This is the home page</h1>
        <Route path="/about">
        <h1 className="font-bold text-2xl">About us</h1>

        </Route>

      </Switch>
      <Footer />

      </Router>
     
    </div>  
  );
}

export default App;
