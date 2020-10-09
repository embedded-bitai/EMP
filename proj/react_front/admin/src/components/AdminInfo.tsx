import React from "react";
import { PageTemplate } from './index'
import GlobalStyles from './alpha_style/GlobalStyles';

// import { useRoutes } from 'react-router-dom';
// import DashboardLayout from "../layouts/DashboardLayout";
import Budget from '../views/reports/dashboardView/Budget'
import TotalCustomers from "../views/reports/dashboardView/TotalCustomers";
import TasksProgress from "../views/reports/dashboardView/TasksProgress";
import TotalProfit from "../views/reports/dashboardView/TotalProfit";
import Sales from "../views/reports/dashboardView/Sales";
import TrafficByDevice from "../views/reports/dashboardView/TrafficByDevice";
import LatestProducts from "../views/reports/dashboardView/LatestProducts";
import LatestOrders from "../views/reports/dashboardView/LatestOrders";


const AdminInfo = () => {

    
    return ( 
        <PageTemplate> <section className="admin_info">
        <GlobalStyles/>
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