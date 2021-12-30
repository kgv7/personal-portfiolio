import React from "react";
import { BrowserRouter, Route } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";
import "../static/styles.css"
import Main from "./Main";

export default function App() {

  return (
  <React.Fragment>
    <BrowserRouter>
        {/* <Navbar logo="" brand="Kaitlyn Goodman-Vojdani"/> */}
        <div className="main-container-fluid">
            <Route exact path="/" component={Main} />
        </div>
    </BrowserRouter>
  </React.Fragment>
  )
}