import React from "react";
import { PageTemplate } from './index';
// import GlobalStyles from './alpha_style/GlobalStyles';

// import { useRoutes } from 'react-router-dom';
// import DashboardLayout from "../layouts/DashboardLayout";
import Budget from './admin/Budget';
import TotalCustomers from './admin/TotalCustomers';
import TasksProgress from './admin/TasksProgress';
import TotalProfit from './admin/TotalProfit';
import Sales from './admin/Sales';
import TrafficByDevice from './admin/TrafficByDevice';
import LatestProducts from './admin/LatestProducts';
import LatestOrders from './admin/LatestOrders';

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