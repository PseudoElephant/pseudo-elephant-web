import "../index.css";




import React from "react";


import { RecentProjects } from "../Components/RecentProjects"

import BrandLogo from "../assets/PseudoElefant.png"


export default function Home() {
    const names = ["Stephan", "Alessandro"]
    return (
        <div>
            <RecentProjects />
            <AboutUs>
                <UserPreview name={names[0]}></UserPreview>
                <UserPreview name={names[1]}></UserPreview>
            </AboutUs>
        </div>
    );
}


function AboutUs(props) {
    return (
        <div className="about-us">
            <h2 className="about-title">Who are we?</h2>
            <ul className="us">
                {props.children}
            </ul>
        </div>
    );
}

function UserPreview(props) {
    return (
        <li className="about">
            <h2 className="user-title">{props.name}</h2>
            <img
                src={BrandLogo}
                className="user-image shadow"
                alt={props.name + "_img"}
            ></img>
        </li>
    );
}