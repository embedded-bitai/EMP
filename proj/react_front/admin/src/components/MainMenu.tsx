import React from "react";
import { FaHome } from 'react-icons/fa'
import { NavLink } from 'react-router-dom'

const selectedStyle = {
    backgroundColor: "white", color: "slategray"
}

const MainMenu = () => <nav className={"main-menu"}>
    <NavLink to={"/"}><FaHome/></NavLink>
    <NavLink to={"/about"} activeStyle={selectedStyle}>[회사소개]</NavLink>
    <NavLink to={"/events"} activeStyle={selectedStyle}>[이벤트]</NavLink>
    <NavLink to={"/products"} activeStyle={selectedStyle}>[제품]</NavLink>
    <NavLink to={"/contact"} activeStyle={selectedStyle}>[고객지원]</NavLink>
    <NavLink to={"/admin_info"} activeStyle={selectedStyle}>[관리자 정보]</NavLink>
</nav>

export default MainMenu