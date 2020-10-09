import React from "react"
import Home from "./home/Home"
import Signup from './user/Signup'
import Login from './user/Login'
import Survey from './survey/Survey'
import Board from './board/BoardPage'
import Menu from './cheese/CheeseList'
import { BrowserRouter, Route, Switch } from 'react-router-dom'

const Main: React.FC = () => {
    return <div>
        <BrowserRouter>
            <div className="main">
                <Switch>
                    <Route exact path="/" component = {Home}/>
                    <Route path="/signUp" component ={Signup} />
                    <Route path="/login" component ={Login} />
                    <Route path="/survey" component={Survey}/>
                    <Route path="/board" component = {Board}/>
                    <Route path="/menu" component={Menu}/>
                    {/* <Redirect from={"/history"} to={"/about/history"}/>
                    <Redirect from={"/services"} to={"/about/services"}/>
                    <Redirect from={"/location"} to={"/about/location"}/>
                    <Route path="/contact" component = {Contact}/>
                    <Route path="/events" component = {Events} />
                    <Route path="/products" component = {Products} /> */}

                    {/* <Route component={Error}/> */}
                </Switch>
            </div>
        </BrowserRouter>
    </div>
}
export default Main