export var json = {
    // title: "치즈 취향을 알아보기",
    showProgressBar: "bottom",
    // firstPageIsStarted: true,
    // startSurveyText: "Start Recommend",
    pages: [
        { 
            "name": "page1",
            "navigationTitle": "",
            "navigationDescription": "Collector's info",
            "elements": [
                {
                    type:"imagepicker", name:"chooseFood_2", title:"아래 사진들 중에서 중복해서 선택해주세요",
                    colCount: 5, isRequired: true,
                    choices:[
                        {value: "파스타", imageLink: "https://i.pinimg.com/236x/ba/a8/74/baa874b693fe434b07b25f8ec2ddea39.jpg"},
                        {value: "맥앤치즈", imageLink: "https://i.pinimg.com/236x/63/99/a1/6399a10f254ede8c4653022e31acc8b6.jpg"},
                        {value: "그라탕", imageLink: "https://i.pinimg.com/236x/e3/3d/5b/e33d5bac2bd0c7091828eccc010f13c6.jpg"},
                        {value: "스테이크", imageLink: "https://i.pinimg.com/236x/ea/ad/37/eaad37156f9c488b7e52c0eb4caeaab8.jpg"},
                        {value: "마르게리타 피자",  imageLink: "https://i.pinimg.com/236x/9a/ce/d0/9aced00ce1bbb7d9482761a5520cea11.jpg"},
                        {value: "스프", imageLink: "https://i.pinimg.com/236x/52/b7/63/52b76318d20e152556f830b9533cf36e.jpg"}
                    ]
                }
            ]
        }, 
        { 
            "name": "page2",
            "navigationTitle": "Collector",
            "navigationDescription": "Collector's info",
            "elements": [
                {
                    type:"imagepicker", name:"chooseFood_2", title:"아래 사진들 중에서 중복해서 선택해주세요",
                    colCount: 5, isRequired: true,
                    choices:[
                        {value: "파스타", imageLink: "https://i.pinimg.com/236x/ba/a8/74/baa874b693fe434b07b25f8ec2ddea39.jpg"},
                        {value: "맥앤치즈", imageLink: "https://i.pinimg.com/236x/63/99/a1/6399a10f254ede8c4653022e31acc8b6.jpg"},
                        {value: "그라탕", imageLink: "https://i.pinimg.com/236x/e3/3d/5b/e33d5bac2bd0c7091828eccc010f13c6.jpg"},
                        {value: "스테이크", imageLink: "https://i.pinimg.com/236x/ea/ad/37/eaad37156f9c488b7e52c0eb4caeaab8.jpg"},
                        {value: "마르게리타 피자",  imageLink: "https://i.pinimg.com/236x/9a/ce/d0/9aced00ce1bbb7d9482761a5520cea11.jpg"},
                        {value: "스프", imageLink: "https://i.pinimg.com/236x/52/b7/63/52b76318d20e152556f830b9533cf36e.jpg"}
                    ]
                }
            ]
        },               
        
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
    completedHtml:"고객님의 치즈 취향을 분석 중입니다."
};
