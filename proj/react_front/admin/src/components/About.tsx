import React from "react";
import {PageTemplate, AboutMenu} from './index'
import {Company, History, Services, Location} from './aboutMenu/index'
import {Route} from 'react-router-dom'

const About = ({match}) => <PageTemplate>
    <section className="about">
        <Route component={AboutMenu} />
        <Route exact path={"/about"} component ={Company}/>
        <Route path={"/about/history"} component ={History}/>
        <Route path={"/about/services"} component ={Services}/>
        <Route path={"/about/location"} component ={Location}/>
    </section>
</PageTemplate>

export default About