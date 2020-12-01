import React from "react";
import axios from 'axios'
import { context as c } from '../../../../modules/context'

import * as Survey from "survey-react";
import "survey-react/modern.css";
import './recommend.css'

import { json } from './Survey_json'

Survey.StylesManager.applyTheme("modern");

// function onValueChanged(result) {
//     console.log("value changed!" + JSON.stringify(result))
// }

function onComplete(result) {
    console.log("Complete!" + JSON.stringify(result.data))

    const user_id = sessionStorage.getItem('sessionUser')
    axios.post(`${c.url}/api/recommend`, 
        { "user_id": user_id, "chooseFood_1": result.data.chooseFood_1, "chooseFood_2": result.data.chooseFood_2, "chooseFood_3": result.data.chooseFood_3, "chooseFood_4": result.data.chooseFood_4 })
        .then(res => {
            // res.header["Access-Control-Allow-Origin"] =  "*"
            alert("성공")
        })
        .catch( e => {
            alert("고객님의 치즈 취향을 분석중입니다.")
        })    
}


var surveyGetResult = function (s, options) {
    if (options.success) {
        showRecommend(options.dataList)
    }
}

function showRecommend(result) {
    // const user_id = sessionStorage.getItem('sessionUser')
    axios.get(`${c.url}/api/recommend`)
        // { "user_id": user_id, "chooseFood_1": result.data.chooseFood_1, "chooseFood_2": result.data.chooseFood_2 })
        .then(res => {
            console.log("flask 연결 성공")
        })
        .catch( e => {
            alert("로그인을 하시면 결과를 확인하실 수 있습니다.")
        })    

}


export function RecommendSurvey () {
    var model = new Survey.Model(json)
    return (
        <div className="container">
            <Survey.Survey
                model={model}
                onComplete={onComplete}
                onGetResult={surveyGetResult}
            />
        </div>
    )
}


export default RecommendSurvey;


