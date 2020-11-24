import React, { useState } from 'react'
// import { createStore, applyMiddleware, combineReducers } from 'redux'
import { BrowserRouter as Router, Route, Switch, Redirect, BrowserRouter } from 'react-router-dom'
// import { Nav } from './components'
// import { AirportContainer, BmiContainer, CabbageContainer , ChatbotContainer,
//          CounterContainer, MovieReviewConainer } from './containers/item'
// import { UserRegister, UserLogin, UserDetail, UserModify, UserWithdrawal, UserList } from './containers/user'
// import { ArticleList, EditArticle, ReadArticle, RemoveArticle, ArticleWriteForm } from './containers/article'
import {Home, Cheese, Login,  Survey, Review} from './templates'
// import { Home, User, Article, Item} from './templates'



export default function App(){
    const [loggedIn, setLoggedIn] = useState(sessionStorage.getItem('sessionUser'))
    return (<>
        <BrowserRouter>
                {/* <Nav isAuth = {loggedIn}/> */}
                <Switch>
                    <Route exact path='/' component={Home}></Route>
                    <Redirect from = {'/home'} to={'/'}/> 
                    <Route path='/login' component={Login}></Route>
                    {/* <Route path='/signup' component={Signup}></Route> */}
                    {/* <Route path='/signup-form' component={ UserRegister }/>
                    <Route path='/signin-form' component={ UserLogin }/>
                    <Route path='/user-detail' component={ UserDetail }/>
                    <Route path='/modifying-user-info' component={ UserModify }/>
                    <Route path='/membership-withdrawal' component={ UserWithdrawal }/>
                    <Route path='/userlist' component={ UserList }/>*/}
                    
                    <Route exact path='/survey' component={ Survey }></Route>
                    {/*<Route path='/article-list' component={ ArticleList }></Route>
                    <Route path='/edit-article' component={ EditArticle }></Route>
                    <Route path='/read-article' component={ ReadArticle }></Route>
                    <Route path='/remove-article' component={ RemoveArticle }></Route>
                    <Route path='/article-write-form' component={ ArticleWriteForm }></Route>*/}

                    <Route exact path='/cheese' component={Cheese}></Route>
                    {/*<Route path='/search-airport' component={ AirportContainer }></Route>
                    <Route path='/find-bmi' component={ BmiContainer }></Route>
                    <Route path='/cabbage-price-predict' component={ CabbageContainer }></Route>
                    <Route path='/chabtbot-service' component={ ChatbotContainer }></Route>
                    <Route path='/counter' component={ CounterContainer }></Route> */}

                    <Route exact path='/review' component={Review}></Route>
                </Switch>
        </BrowserRouter>

</>)}

// import React from 'react'
// import Home from './template/Home'
// import Signup from './user/Signup'
// import Login from './user/Login'
// import BoardRegister from './board/BoardRegister'
// import Survey from './survey/Survey'
// import Board from './board/BoardPage'
// import Cheese from './cheese/Cheese'
// import About from './admin/About'
// import AdminInfo from './admin/AdminInfo'
// import { BrowserRouter, Route, Switch, Redirect } from 'react-router-dom'

// const Main: React.FC = () => {
//     return <div>
//         <BrowserRouter>
//             <div className="main">
//                 <Switch>
//                     <Route exact path="/" component = {Home}/>
//                     <Route path="/signUp" component ={Signup} />
//                     <Route path="/login" component ={Login} />
//                     <Route path="/survey" component={Survey}/>
//                     <Route path="/board" component = {Board}/>
//                     <Route path="/cheese" component={Cheese}/>
//                     <Route path="/boardregister" component={BoardRegister}/>
//                     <Route path="/about" component ={About}/>
//                     <Redirect from={"/history"} to={"/about/history"}/>
//                     <Redirect from={"/services"} to={"/about/services"}/>
//                     <Redirect from={"/location"} to={"/about/location"}/>
//                     {/* <Route path="/contact" component = {Contact}/>
//                     <Route path="/events" component = {Events} />
//                     <Route path="/products" component = {Products} /> */}
//                     <Route path="/admin_info" component = {AdminInfo} />
//                 </Switch>
//             </div>
//         </BrowserRouter>
//     </div>
// }
// export default Main