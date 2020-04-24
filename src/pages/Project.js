import React, { useEffect,useState } from 'react'

function Project({ match }) {
    useEffect(() => {
        fetchItem();
    },[]);

    const [item,setItem] = useState({})

    const fetchItem = async () => {
        const fetchItem = await fetch(`/api/project/${match.params.name}`);
        const data = await fetchItem.json();
        console.log(data);
        setItem(data);
    };
    return (<div style={{"justifyContent":"center",display:"flex"}}>
        <h2 style={{"fontSize":"5rem", "color":"white"}}>{item.name}</h2>
        <h1 style={{color:"white",padding:"1.5rem"}}>{item.number}</h1>
    </div>)
}

export default Project;