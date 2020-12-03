import React, { Component } from "react";
// import ReactDOM from "react-dom";
import axios from 'axios'
import {context as c} from '../../../../modules/context'
import * as Survey from "survey-react";
import './recommend.css'
import "survey-react/survey.css";
import RecommendLoad from './RecommendLoad'
// import RecommendResult from './RecommendResult'

import { json } from './Survey_json'

class SurveyComponent extends Component {
    constructor(props) {
        super(props);
        this.state = { isCompleted: false };
        this.onCompleteComponent = this.onCompleteComponent.bind(this);  
    }
    onCompleteComponent(result) {
        this.setState({ isCompleted: true })
        console.log("Complete!" + JSON.stringify(result.data))

        const user_id = sessionStorage.getItem('sessionUser')
        axios.post(`${c.url}/api/recommend`, 
            { "user_id": user_id, "chooseFood_1": result.data.chooseFood_1, "chooseFood_2": result.data.chooseFood_2, "chooseFood_3": result.data.chooseFood_3, "chooseFood_4": result.data.chooseFood_4 })
            .then(res => {
                // res.header["Access-Control-Allow-Origin"] =  "*"
                console.log("성공")
            })
            .catch( e => {
                console.log("api axios 실패")
            })    
    }
    render() {
        var model = new Survey.Model(json)
        var surveyRender = !this.state.isCompleted ? (
            <Survey.Survey
                model={model}
                // onSendResult={surveySendResult}
                showCompletedPage={false}
                onComplete={this.onCompleteComponent}
                // onComplete={onComplete}
                // onGetResult={surveyGetResult}
            />
        ) : null;
        var onCompleteComponent = this.state.isCompleted ? (
            <RecommendLoad/>
        ) : null;
        return (
            <div>
                {surveyRender}
                {onCompleteComponent}
            </div>
        )
    }
}

export default function RecommendPick() {
    return (
        <div className="recommend-survey">
            <SurveyComponent/>
        </div>
    )
}
