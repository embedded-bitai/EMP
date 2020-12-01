import React, { useEffect, useState } from "react";
import PropTypes from 'prop-types'
import axios from 'axios'
import { context as c } from '../../../../modules/context'

import * as Survey from "survey-react";
import "survey-react/modern.css";
import './recommend.css'

import { json } from './Survey_json'

Survey.StylesManager.applyTheme("modern");

function onValueChanged(result) {
    console.log("value changed!" + JSON.stringify(result))
}

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

var resultId = 'result_id'

var surveySendResult = function (result) {
    console.log("Complete!" + JSON.stringify(result.data))

    const user_id = sessionStorage.getItem('sessionUser')
    axios.post(`${c.url}/api/recommend`, 
        { "user_id": user_id, "chooseFood_1": result.data.chooseFood_1, "chooseFood_2": result.data.chooseFood_2 })
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
    const user_id = sessionStorage.getItem('sessionUser')
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
                // onSendResult={surveySendResult}
                onComplete={onComplete}
                onGetResult={surveyGetResult}
            />
        </div>
    )
}


// export function RecommendSurvey () {
//     var model = new Survey.Model(json)
//     return (
//         <div className="container">
//             <Survey.Survey
//                 model={model}
//                 onComplete={onComplete}
//                 onValueChanged={onValueChanged}
//             />
//         </div>
//     )
// }


// class RecommendSurvey extends Component {
//     constructor() {
//         super();
        
//     }

//     render() {
        
//         const json = {
//             title: "치즈 취향을 알아보기",
//             showProgressBar: "bottom",
//             // showTimerPanel: "top",
//             // maxTimeToFinishPage: 10,
//             // maxTimeToFinish: 25,
//             firstPageIsStarted: true,
//             startSurveyText: "Start Recommend",
//             pages: [
//                 { questions: [ {type: "html", html: "You are about to start quiz by history. <br/>You have 10 seconds for every page and 25 seconds for the whole survey of 3 questions.<br/>Please click on <b>'Start Quiz'</b> button when you are ready." } ] },
//                 {   title: "양식 중에 어떤 음식을 좋아하시나요?",
//                     questions: [
//                     {type:"imagepicker", name:"chooseKorean", title:"아래 사진들 중에서 중복해서 선택해주세요",
//                         colCount: 4, isRequired: true,
//                         choices:[
//                             {id: "라자냐", value: 1, imageLink: "https://i.pinimg.com/236x/fa/17/97/fa1797e94b8305566e628e55c0de142c.jpg", height: "100px"},
//                             {id: "피자", value: 2, imageLink: "https://i.pinimg.com/236x/ca/40/8e/ca408eb24ee259b8195f09971899b4a6.jpg"},
//                             {id: "리소토", value: 3, imageLink: "https://i.pinimg.com/564x/8a/5f/86/8a5f86389c848d2dea572f15efae71e4.jpg"},
//                             {id: "베이컨", value: 4, imageLink: "https://i.pinimg.com/236x/80/f1/01/80f101f196ff753b51bdac5b680609bf.jpg"}
//                             // {id: "파스타", value: 1, imageLink: "https://i.pinimg.com/236x/ba/a8/74/baa874b693fe434b07b25f8ec2ddea39.jpg"},
//                             // {id: "맥앤치즈", value: 1, imageLink: "https://i.pinimg.com/236x/63/99/a1/6399a10f254ede8c4653022e31acc8b6.jpg"},
//                             // {id: "그라탕", value: 1, imageLink: "https://i.pinimg.com/236x/e3/3d/5b/e33d5bac2bd0c7091828eccc010f13c6.jpg"},
//                             // {id: "스테이크", value: 1, imageLink: "https://i.pinimg.com/236x/ea/ad/37/eaad37156f9c488b7e52c0eb4caeaab8.jpg"},
//                             // {id: "마르게리타 피자", value: 1, imageLink: "https://i.pinimg.com/236x/9a/ce/d0/9aced00ce1bbb7d9482761a5520cea11.jpg"},
//                             // {id: "스프", value: 1, imageLink: "https://i.pinimg.com/236x/52/b7/63/52b76318d20e152556f830b9533cf36e.jpg"},
                        
//                         ]
//                     }
//                 ]},        
                
//                 // {   title: "한식 중에 어떤 음식을 좋아하시나요?",
//                 //     questions: [
//                 //     {type:"checkbox", name:"langs",title:"Please select from the list",
//                 //         colCount: 4, isRequired: true,
//                 //         choices:["Javascript", "Java", "Python", "CSS", "PHP", "Ruby", "C++", "C", 
//                 //             "Shell", "C#", "Objective-C", "R", "VimL", "Go", "Perl", "CoffeeScript", 
//                 //             "TeX", "Swift", "Scala", "Emacs Lisp", "Haskell", "Lua", "Clojure", 
//                 //             "Matlab", "Arduino", "Makefile", "Groovy", "Puppet", "Rust", "PowerShell"]
//                 //     }
//                 // ]},        
//                 // { title: "Please enter your name and e-mail",
//                 //     questions: [ 
//                 //     {type: "text", name: "name", title: "Name:"}, 
//                 //     {type: "text", name: "email", title: "Your e-mail"}]
//                 // }
//             ],
//         };
//         const survey = new Survey.Model(json);

//         return (
//             <Survey.Survey
//                 model={survey}
//             />
//         );
    
//         // survey
//         //     .onComplete
//         //     .add(function (result) {
//         //         document
//         //             .querySelector('#surveyResult')
//         //             .textContent = "Result JSON:\n" + JSON.stringify(result.data, null, 3);
//         //     });
//     }
// }

export default RecommendSurvey;


