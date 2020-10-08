import React from "react";
import { Link } from 'react-router-dom'

const Home = () => <div className="home">
    <h1> [홈] </h1>
    <nav>
        <Link to={"about"}>[회사소개(홈)]</Link>
        <Link to={"events"}>[이벤트(홈)]</Link>
        <Link to={"products"}>[제품(홈)]</Link>
        <Link to={"contact"}>[고객 지원(홈)]</Link>
        <Link to={"admin_info"}>[관리자 정보(홈)]</Link>
    </nav>
</div>

export default Home