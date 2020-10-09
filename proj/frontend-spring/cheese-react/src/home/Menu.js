import React from 'react';
import { Link } from 'react-router-dom'

const Menu = () => <div className="menu">
    <Link to={"/"}> [홈] </Link>
    <nav>
        <Link to={"signup"}> [회원가입] </Link>
        <Link to={"login"}>[로그인]</Link>
        <Link to={"menu"}>[치즈]</Link>
        <Link to={"order"}>[주문]</Link>
        <Link to={"board"}>[F&Q]</Link>
        <Link to={"survey"}>[추천]</Link>
        <Link to={"admin"}>[Admin]</Link>
    </nav>
</div>

export default Menu