
export var json = {
    // title: "치즈 취향을 알아보기",
    showProgressBar: "bottom",
    // showTimerPanel: "top",
    // maxTimeToFinishPage: 10,
    // maxTimeToFinish: 25,
    firstPageIsStarted: true,
    startSurveyText: "Start Recommend",
    pages: [
        { 
            questions: [ 
                {
                    type: "html", 
                    html: "치즈를 추천받아보세요. <br/>AI를 통해 고객님의 치즈 취향을 분석해드립니다. <br/><b>'Start Recommend'</b>버튼을 눌러 시작해주세요.",
                } 
            ] 
        },
        {   
            title: "다음 중에 어떤 음식을 좋아하시나요?",
            questions: [
                {
                    type:"imagepicker", name:"chooseFood_1", title:"아래 사진들 중에서 하나를 선택해주세요",
                    colCount: 5, isRequired: true, 
                    choices:[
                        {value: "라자냐", imageLink: "https://i.pinimg.com/236x/fa/17/97/fa1797e94b8305566e628e55c0de142c.jpg", height: "100px"},
                        {value: "피자", imageLink: "https://i.pinimg.com/236x/ca/40/8e/ca408eb24ee259b8195f09971899b4a6.jpg"},
                        {value: "리소토",  imageLink: "https://i.pinimg.com/564x/8a/5f/86/8a5f86389c848d2dea572f15efae71e4.jpg"},
                        {value: "베이컨", imageLink: "https://i.pinimg.com/236x/80/f1/01/80f101f196ff753b51bdac5b680609bf.jpg"},
                        {value: "파스타", imageLink: "https://i.pinimg.com/236x/ba/a8/74/baa874b693fe434b07b25f8ec2ddea39.jpg"},
                        {value: "맥앤치즈", imageLink: "https://i.pinimg.com/236x/63/99/a1/6399a10f254ede8c4653022e31acc8b6.jpg"},
                        {value: "그라탕", imageLink: "https://i.pinimg.com/236x/e3/3d/5b/e33d5bac2bd0c7091828eccc010f13c6.jpg"},
                        {value: "스테이크", imageLink: "https://i.pinimg.com/236x/ea/ad/37/eaad37156f9c488b7e52c0eb4caeaab8.jpg"},
                        {value: "볶음밥", imageLink: "https://i.pinimg.com/236x/55/86/e2/5586e243e101607d0362556906b76ed6.jpg"},
                        {value: "스프", imageLink: "https://i.pinimg.com/236x/52/b7/63/52b76318d20e152556f830b9533cf36e.jpg"},
                    
                    ]
                }
        ]},        
        {   title: "디저트 중에 어떤 음식을 좋아하시나요?",
            questions: [
            {type:"imagepicker", name:"chooseFood_2", title:"아래 사진들 중에서 하나를 선택해주세요",
                colCount: 4, isRequired: true,
                choices:[
                    {value: "과일", imageLink: "https://i.pinimg.com/236x/1f/40/7a/1f407ab1ca30fe6002190646536bae5a.jpg"},
                    {value: "빵", imageLink: "https://i.pinimg.com/236x/bd/0f/65/bd0f653712ed63b588e52684e7e15bf5.jpg"},
                    {value: "샐러드", imageLink: "https://i.pinimg.com/236x/3e/94/a6/3e94a68a72c0390d3f4178f071dd0e4b.jpg"},
                    {value: "카프레제", imageLink: "https://i.pinimg.com/236x/30/db/60/30db60c305dff679234bd836b9fe0c8d.jpg"},
                    {value: "핑거푸드",  imageLink: "https://i.pinimg.com/236x/b1/85/af/b185af3082d1c91488597929e2d9e996.jpg"},
                    {value: "타르트", imageLink: "https://i.pinimg.com/236x/2e/d4/9d/2ed49d71eb8f15f75a0fbe4696f7880a.jpg"},
                    {value: "치즈케이크", imageLink: "https://i.pinimg.com/236x/f6/35/db/f635dbd89260a13b4ed7d34af0026a17.jpg"},
                    {value: "견과류", imageLink: "https://i.pinimg.com/236x/b6/d9/aa/b6d9aa6a8d0fdf3439d5877a30552e0a.jpg"}
                ]
            }
        ]},     
        {   title: "어떤 소스를 좋아하시나요?",
        questions: [
            {type:"imagepicker", name:"chooseFood_3", title:"아래 사진들 중에서 하나를 선택해주세요",
                colCount: 4, isRequired: true,
                choices:[
                    {value: "꿀", imageLink: "https://i.pinimg.com/236x/16/60/f0/1660f0c74cab820463f62b99d2dd175d.jpg"},
                    {value: "딥소스", imageLink: "https://i.pinimg.com/236x/6a/c1/a6/6ac1a68da9a4663d519ea436e10e7b12.jpg"},
                    {value: "발사믹식초", imageLink: "https://i.pinimg.com/236x/48/91/d3/4891d3983eec181df891a264e11ff50b.jpg"},
                    {value: "바질", imageLink: "https://i.pinimg.com/236x/56/7f/25/567f25729d903c991c7b26e33008f7f7.jpg"},
                    {value: "잼",  imageLink: "https://i.pinimg.com/236x/54/c7/ab/54c7ab31bd0123243204165502d887ce.jpg"},
                    {value: "올리브유", imageLink: "https://i.pinimg.com/236x/8c/1e/68/8c1e68368204c4635d276d13916843d2.jpg"},
                    // {value: "스프레드", imageLink: "https://i.pinimg.com/236x/f6/35/db/f635dbd89260a13b4ed7d34af0026a17.jpg"},
                    {value: "퐁듀", imageLink: "https://i.pinimg.com/236x/39/60/6c/39606ca3e6afa99d8d36e21bc9596e0f.jpg"}
                ]
            }
        ]},    
        {   title: "어떤 주류를 좋아하시나요?",
        questions: [
            {type:"imagepicker", name:"chooseFood_4", title:"아래 사진들 중에서 하나를 선택해주세요",
                colCount: 3, isRequired: true,
                choices:[
                    {value: "맥주", imageLink: "https://i.pinimg.com/236x/1b/83/3d/1b833de638ada3c0ebbb0468d8d9ba89.jpg"},
                    {value: "와인", imageLink: "https://i.pinimg.com/236x/05/93/bb/0593bb9e234e38610d2eab58c306810b.jpg"},
                    {value: "위스키", imageLink: "https://i.pinimg.com/236x/10/70/55/107055a9ca5a9c4b94719f8e8d4db618.jpg"},
                    {value: "화이트와인", imageLink: "https://i.pinimg.com/236x/e4/32/89/e43289ce96b0d1877040479b75374384.jpg"},
                    {value: "막걸리",  imageLink: "https://i.pinimg.com/236x/e8/f0/3d/e8f03d518d3e462c25ec1a7609641ad7.jpg"},
                    {value: "사케", imageLink: "https://i.pinimg.com/236x/3c/5c/81/3c5c813c679461a23582ff9a9629a2f9.jpg"}
                ]
            }
        ]},  
        
        
        // {   title: "한식 중에 어떤 음식을 좋아하시나요?",
        //     questions: [
        //     {type:"checkbox", name:"langs",title:"Please select from the list",
        //         colCount: 4, isRequired: true,
        //         choices:["Javascript", "Java", "Python", "CSS", "PHP", "Ruby", "C++", "C", 
        //             "Shell", "C#", "Objective-C", "R", "VimL", "Go", "Perl", "CoffeeScript", 
        //             "TeX", "Swift", "Scala", "Emacs Lisp", "Haskell", "Lua", "Clojure", 
        //             "Matlab", "Arduino", "Makefile", "Groovy", "Puppet", "Rust", "PowerShell"]
        //     }
        // ]},        
        // { title: "Please enter your name and e-mail",
        //     questions: [ 
        //     {type: "text", name: "name", title: "Name:"}, 
        //     {type: "text", name: "email", title: "Your e-mail"}]
        // }
    ],
    completedHtml:"당신이 좋아하는 치즈상품은 <br/> <b>[브리미] 보코치니<br/>입니다. "
};



// class SurveyComponent extends Component {

//     json = {
//         title: "치즈 취향을 알아보기",
//         showProgressBar: "bottom",
//         // showTimerPanel: "top",
//         // maxTimeToFinishPage: 10,
//         // maxTimeToFinish: 25,
//         firstPageIsStarted: true,
//         startSurveyText: "Start Recommend",
//         pages: [
//             { questions: [ {type: "html", html: "You are about to start quiz by history. <br/>You have 10 seconds for every page and 25 seconds for the whole survey of 3 questions.<br/>Please click on <b>'Start Quiz'</b> button when you are ready." } ] },
//             {   title: "양식 중에 어떤 음식을 좋아하시나요?",
//                 questions: [
//                 {type:"imagepicker", name:"chooseKorean", title:"아래 사진들 중에서 중복해서 선택해주세요",
//                     colCount: 5, isRequired: true,
//                     choices:[
//                         {id: "라자냐", value: 1, imageLink: "https://i.pinimg.com/236x/fa/17/97/fa1797e94b8305566e628e55c0de142c.jpg", height: "100px"},
//                         {id: "피자", value: 1, imageLink: "https://i.pinimg.com/236x/ca/40/8e/ca408eb24ee259b8195f09971899b4a6.jpg"},
//                         {id: "리소토", value: 1, imageLink: "https://i.pinimg.com/564x/8a/5f/86/8a5f86389c848d2dea572f15efae71e4.jpg"},
//                         {id: "베이컨", value: 1, imageLink: "https://i.pinimg.com/236x/80/f1/01/80f101f196ff753b51bdac5b680609bf.jpg"}
//                         // {id: "파스타", value: 1, imageLink: "https://i.pinimg.com/236x/ba/a8/74/baa874b693fe434b07b25f8ec2ddea39.jpg"},
//                         // {id: "맥앤치즈", value: 1, imageLink: "https://i.pinimg.com/236x/63/99/a1/6399a10f254ede8c4653022e31acc8b6.jpg"},
//                         // {id: "그라탕", value: 1, imageLink: "https://i.pinimg.com/236x/e3/3d/5b/e33d5bac2bd0c7091828eccc010f13c6.jpg"},
//                         // {id: "스테이크", value: 1, imageLink: "https://i.pinimg.com/236x/ea/ad/37/eaad37156f9c488b7e52c0eb4caeaab8.jpg"},
//                         // {id: "마르게리타 피자", value: 1, imageLink: "https://i.pinimg.com/236x/9a/ce/d0/9aced00ce1bbb7d9482761a5520cea11.jpg"},
//                         // {id: "스프", value: 1, imageLink: "https://i.pinimg.com/236x/52/b7/63/52b76318d20e152556f830b9533cf36e.jpg"},
                    
//                     ]
//                 }
//             ]},        
            
//             // {   title: "한식 중에 어떤 음식을 좋아하시나요?",
//             //     questions: [
//             //     {type:"checkbox", name:"langs",title:"Please select from the list",
//             //         colCount: 4, isRequired: true,
//             //         choices:["Javascript", "Java", "Python", "CSS", "PHP", "Ruby", "C++", "C", 
//             //             "Shell", "C#", "Objective-C", "R", "VimL", "Go", "Perl", "CoffeeScript", 
//             //             "TeX", "Swift", "Scala", "Emacs Lisp", "Haskell", "Lua", "Clojure", 
//             //             "Matlab", "Arduino", "Makefile", "Groovy", "Puppet", "Rust", "PowerShell"]
//             //     }
//             // ]},        
//             // { title: "Please enter your name and e-mail",
//             //     questions: [ 
//             //     {type: "text", name: "name", title: "Name:"}, 
//             //     {type: "text", name: "email", title: "Your e-mail"}]
//             // }
//         ],
//         completedHtml:""
//     };
    
//     onComplete(survey, options) {
//         console.log("Survey results: " + JSON.stringify(survey.data))
//     }

//     render() {
//         var model = new Survey.Model(this.json)
//         return (<Survey.Survey model={model} onComplete={this.onComplete}/>)

//     }
// }