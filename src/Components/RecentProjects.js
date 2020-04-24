import BrandLogo from "../assets/PseudoElefant.png";
import React from "react";

export function RecentProjects() {
  // API CALL
  const projects = [
    {
      title: "DiscordBot",
      description: "Intense Project",
      icon: "somefile.png",
    },
    {
      title: "The Minecraft Map",
      description: "Intense Project, maybe more intense.",
      icon: "somefile.png",
    },
    {
      title: "The Web Page",
      description: "Intense Project",
      icon: "somefile.png",
    },
  ];
  return (
    <div className="recent-projects">
      <ul className="projects">
        {projects.map((project, index) => (
          <ProjectPreview project={project} key={index} />
        ))}
      </ul>
    </div>
  );
}

function ProjectPreview(props) {
  const project = props.project;
  return (
    <li className="project">
      <h2 className="project-title">{project.title}</h2>
      <img
        src={BrandLogo}
        className="project-image shadow"
        alt={project.title + "_img"}
      ></img>
    </li>
  );
}
