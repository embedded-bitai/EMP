import React from 'react'
import Home from './home/Home'
import Signup from './user/Signup'
import Login from './user/Login'
import BoardRegister from './board/BoardRegister'
import Survey from './survey/Survey'
import Board from './board/BoardPage'
import Cheese from './cheese/Cheese'
import About from './admin/About'
import AdminInfo from './admin/AdminInfo'
import { BrowserRouter, Route, Switch, Redirect } from 'react-router-dom'

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
                    <Route path="/cheese" component={Cheese}/>
                    <Route path="/boardregister" component={BoardRegister}/>
                    <Route path="/about" component ={About}/>
                    <Redirect from={"/history"} to={"/about/history"}/>
                    <Redirect from={"/services"} to={"/about/services"}/>
                    <Redirect from={"/location"} to={"/about/location"}/>
                    {/* <Route path="/contact" component = {Contact}/>
                    <Route path="/events" component = {Events} />
                    <Route path="/products" component = {Products} /> */}
                    <Route path="/admin_info" component = {AdminInfo} />
                </Switch>
            </div>
        </BrowserRouter>
    </div>
}
export default Main