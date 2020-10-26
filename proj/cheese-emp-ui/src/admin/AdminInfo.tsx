import React from "react";
import { PageTemplate } from './index';
// import GlobalStyles from './alpha_style/GlobalStyles';

// import { useRoutes } from 'react-router-dom';
// import DashboardLayout from "../layouts/DashboardLayout";
import Budget from './adminContents/Budget';
import TotalCustomers from './adminContents/TotalCustomers';
import TasksProgress from './adminContents/TasksProgress';
import TotalProfit from './adminContents/TotalProfit';
import Sales from './adminContents/Sales';
import TrafficByDevice from './adminContents/TrafficByDevice';
import LatestProducts from './adminContents/LatestProducts';
import LatestOrders from './adminContents/LatestOrders';

const AdminInfo = () => {

    
    return ( 
        <PageTemplate> <section className="admin_info">
        <h1> [ 관리자 정보 페이지 ] </h1>
        
        <Budget/> 
        <TotalCustomers/>
        <TasksProgress/>
        <TotalProfit/>
        <Sales />
        <TrafficByDevice/>
        <LatestProducts/>
        <LatestOrders/>

        </section></PageTemplate>
        
    );
};

export default AdminInfo