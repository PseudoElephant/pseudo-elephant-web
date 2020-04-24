import React from 'react';
// Import css files
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import "../index.css"
import "../slider.css"
import Slider from "react-slick";
import BrandLogo from "../assets/PseudoElefant.png";
import {ReactComponent as Caret} from "../icons/caret.svg"

class SimpleSlider extends React.Component {
    render() {
        var settings = {
            dots: true,
            infinite: true,
            speed: 700,
            autoplay:true,
            autoplaySpeed: 4000,
            fade:false,
            slidesToShow: 3,
            slidesToScroll: 1,
            focusOnSelect: true,
            nextArrow:<SampleNextArrow/>,
            prevArrow:<SamplePrevArrow/>
            // centerMode: true,
      
        };
        return (
            <div className="slider-cont" style={{width:"60%",margin:"auto"}}>
            <Slider {...settings}>
                <div>
                    <ProjectPreview></ProjectPreview>
                </div>
                <div>
                        <ProjectPreview></ProjectPreview>
                </div>
                <div>
                        <ProjectPreview></ProjectPreview>
                </div>
                <div>
                        <ProjectPreview></ProjectPreview>
                </div>
                <div>
                        <ProjectPreview></ProjectPreview>
                </div>
                <div>
                        <ProjectPreview></ProjectPreview>
                </div>
            </Slider>
            </div>
        );
    }
}

export default SimpleSlider;

function ProjectPreview() {
    
    return (
        <li className="project">
            <h2 className="project-title">Title</h2>
            <img
                style={{ width: "80%" ,height:"60%"}}
                src={BrandLogo}
                className="project-image shadow"
                alt={"im+ "+"_img"}
            ></img>
        </li>
    );
}

function SampleNextArrow(props) {
    const { className, style, onClick } = props;
    console.log(className)
    
    return (
        <div
            className={className+" icon-button rotated-right"}
            style={{ ...style, display: "block" }}
            onClick={onClick}
            
       >
           <Caret></Caret>
       </div>

    );
}

function SamplePrevArrow(props) {
    const { className, style, onClick } = props;
    console.log(className)

    return (
        <div
            className={className + " icon-button rotated-left"}
            style={{ ...style, display: "block" }}
            onClick={onClick}

        >
            <Caret></Caret>
        </div>

    );
}