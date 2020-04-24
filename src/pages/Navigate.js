import "../index.css";

import React from 'react';
import { ReactComponent as BellIcon } from "../icons/bell.svg";
import { ReactComponent as CaretIcon } from "../icons/caret.svg";
import { ReactComponent as PlusIcon } from "../icons/plus.svg";
import { ReactComponent as HomeIcon } from "../icons/home.svg";
import { Link } from "react-router-dom";
import {Navbar,BrandNavigation,NavItem,DropdownMenu} from '../Components/Navigation'


export default function Navigation(){
    const brand = "Pseudo Elephant";
    return (
    <Navbar>
        <BrandNavigation brand={brand} />
        <NavItem icon={<PlusIcon />} />
        <Link to={`/`} style={{marginTop:"auto", marginBottom:"auto"}}>
        <NavItem icon={<HomeIcon />} />
            </Link>

        <NavItem icon={<CaretIcon />}>
            <DropdownMenu></DropdownMenu>
        </NavItem>
    </Navbar>
    )
}