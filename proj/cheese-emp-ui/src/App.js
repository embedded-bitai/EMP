import React, { useState } from 'react'
import { createStore, applyMiddleware, combineReducers } from 'redux' //eslint-disable-line
import { BrowserRouter as Router, Route, Switch, Redirect, BrowserRouter } from 'react-router-dom' //eslint-disable-line
// import { Nav } from './components'
import { Header, Footer } from './components/cmm'
import {Home, Cheese, Recommend, Review, Subscribe} from './templates'
import {Login, Signup, UserInfo } from './containers/usr/user'
import { RecommendResult } from './containers/cop/rec/recommend'
// import { Cart } from "./containers/cop/cart";
// import { Cart } from "./templates/Cart";

// import { HelmetProvider } from 'react-helmet-async';
// import ProductsContextProvider from './containers/cop/cart_1/contexts/ProductsContextProvider';
// import CartContextProvider from './containers/cop/cart_1/contexts/CartContextProvider';

export default function App(){
    const [loggedIn, setLoggedIn] = useState(sessionStorage.getItem('sessionUser'))
    return (<>
        <BrowserRouter>
                {/* <Header /> */}
                <Header isAuth = {loggedIn}/>
                <Switch>
                    <Route exact path='/' component={Home}></Route>
                    <Redirect from = {'/home'} to={'/'}/> 
                    <Route path='/login' component={Login}></Route>
                    <Route path='/signup' component={Signup}></Route>
                    <Route path='/user-info' component={UserInfo}/>

                    <Route path='/recommend' component={Recommend}></Route>
                    <Route path='/recommend-result' component={RecommendResult}/>

                    <Route path='/subscribe' component={Subscribe}></Route>
                    <Route path='/cheese' component={Cheese}></Route>
                    <Route path='/review' component={Review}></Route>

                 </Switch>
                 <Footer />
        </BrowserRouter>

</>)}