import React, { useEffect,useState } from "react";
import { Link } from "react-router-dom";


const brand = "Pseudo Elephant";
export default function Projects() {
    return (<div className="projects-container">
        <ProjectsDisplay />
    </div>
    )
}

function ProjectsDisplay() {
    // Request to the API for the project information

    const [projects,setprojects] = useState([])
    useEffect(() => {
        fetchItems();
    },[]) // solo se ejecuta once
    const fetchItems = async () => {
        const data = await fetch('/api/projects');
        const projects = await data.json();
        setprojects(projects);
    }

    return (
      <div>
      
        {projects.map(project => (
            <div key={project.id}>
            <Link
          to={`/project/${project.title}`}>
            <h1>{project.title}</h1>
            </Link>
            <h2>{project.item}</h2>
            </div>
        ))}
      </div>
    );

}