import React from "react";
import Home from "./Components/Home";
import Projects from "./Components/Projects"
import About from "./pages/About"
const routes = {
    "/": () => <Home/>,
    "/projects":() => <Projects/>,
    "/poll": () => <About/>
};
export default routes;