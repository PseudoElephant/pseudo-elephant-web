import "./index.css";

import React from "react";
import Navigate from "./pages/Navigate";
import About from "./pages/About";
import Home from "./pages/Home";
import Projects from "./pages/Projects"
import Project from "./pages/Project";
import CustomPoll from "./Components/Poll";
import { BrowserRouter as Router, Route, Switch} from "react-router-dom";
import SimpleSlider from "./Components/Slider";

function App() {
    
  return (
    <Router>
      <div className="main">
        <Navigate/>
        <Switch>
        <Route path="/" exact component={Home}/>
        <Route path="/about" component={About}/>
        <Route path="/projects" component={Projects}/>
        <Route path="/project/:name" component={Project}/>
        <Route path="/poll" component={CustomPoll}/>
          <Route path="/test" component={SimpleSlider }/>
        </Switch>
      </div>
    </Router>
  )

}

export default App;
