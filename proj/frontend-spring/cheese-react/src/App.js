import "tailwindcss/dist/base.css";
import "./styles/globalStyles.css";
import React from "react";
import './App.css'
import Main from './Main'
// import { css } from "./user/node_modules/styled-components/macro"; //eslint-disable-line
import './assets/stylesheets/total.css'

// import HomePage from "./home/Home.js";

//import ComponentRenderer from "ComponentRenderer.js";

import { BrowserRouter as Router, Switch, Route } from "react-router-dom";

export default function App() {
  return (
    <Router>
      <Switch>
        {/* <Route path="/components/:type/:subtype/:name">
          <ComponentRenderer />
        </Route>
        <Route path="/components/:type/:name">
          <ComponentRenderer />
        </Route> */}
        <Route path="/">
          <Main/>  
        </Route>
      </Switch>
    </Router>
  );
}

// export default EventLandingPage;

// export default LoginPage;
// export default SignupPage;

