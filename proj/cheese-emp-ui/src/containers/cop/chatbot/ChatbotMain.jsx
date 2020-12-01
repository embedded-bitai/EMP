import React, { Component } from 'react';
import ChatBot from 'react-simple-chatbot';
import PropTypes from 'prop-types'
import { ThemeProvider } from 'styled-components';
import { context as c } from '../../../modules/context'
import axios from 'axios'
// import { m } from 'framer-motion';



// const user_id = sessionStorage.getItem('sessionUser')

class Review extends Component {
    constructor(props) {
        super(props)
        this.state = {
            tasty: '',
            texture: '',
        }
    }

    componentWillMount() {
        const { steps } = this.props;
        const { chatbot_id, user_id, tasty, texture } = steps
        this.setState({ chatbot_id, user_id, tasty, texture })
    }
    render () {
        const { chatbot_id, user_id, tasty, texture } = this.state
        return (
            <div style={{ width: '100%' }}>
                <h1>[설문조사 내역]</h1>
                <table>
                    <tbody>
                        <tr>
                            <td>챗봇 번호</td>
                            <td>{chatbot_id.value}</td>
                        </tr>
                        <tr>
                            <td>사용자 ID</td>
                            <td>{user_id.value}</td>
                        </tr>
                        <tr>
                            <td>선호하는 맛</td>
                            <td>{tasty.value}</td>
                        </tr>
                        <tr>
                            <td>선호하는 식감</td>
                            <td>{texture.value}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        )
    }
}
Review.propsTypes = {
    steps: PropTypes.object,
}
Review.defaultProps = {
    step: undefined,
}

class Answer extends Component {
    constructor(props) {
        super(props)
        this.state = {
            // target_name: ''
        }
    }
    componentWillMount() {
        const {steps} = this.props
        const { chatbot_id, user_id, tasty, texture } = steps
        axios.post(`${c.url}/api/chatbot`, 
        { "chatbot_id": chatbot_id.value, "tasty": tasty.value, "texture": texture.value, "user_id": user_id.value})
        .then(res => {
            alert("성공")
        })
        .catch( e => {
            alert("실패")
        })
    }
    render() {
        console.log(localStorage.getItem("actor"))
        return (
            <div style={{ width: '100%' }}>
                <h3>{ localStorage.getItem("actor") }</h3>
            </div>
        )
    }
}
Answer.propTypes = {
    steps: PropTypes.object,
}
Answer.defaultProps = {
    steps: undefined,
}
const config = {
    width: '600px',
    height: '500px'
}

export const ItemSearch = () => {
        return (<>

        </>)
    
}

export const ItemSearch2 = () => {
    return (
            <p>정보가 없습니다.</p>

    )

}

// all available props
const theme = {
    background: '#f5f8fb',
    fontFamily: 'Helvetica Neue',
    headerBgColor: '#ffb74d',
    headerFontColor: '#fff',
    headerFontSize: '15px',
    botBubbleColor: '#ffb74d',
    botFontColor: '#black',
    userBubbleColor: '#fff',
    userFontColor: '#4a4a4a',
    width: "500",
    height: "900"
  };

class MyChatbot extends Component {
    render() {
        return (
        <ThemeProvider theme={theme}>        
            <ChatBot
                { ...config }
                style={{ width: '700px'}}
                floating = {true}
                headerTitle = {'서비스'}
                enableSmoothScroll = {true}
                steps={[
                    //서비스선택
                    {
                        id: '1',
                        message: '원하시는 서비스를 선택해주세요.',
                        trigger: '2',
                    },
                    {
                        id: '2',
                        options: [
                            { value: 1, label: '치즈 추천 받기', trigger: 'recommend' },
                            { value: 2, label: '치즈 종류 소개', trigger: 'category' },
                            { value: 3, label: '구독회원', trigger: 'fare' },
                            { value: 4, label: '비회원', trigger: 'fare' },
                        ],
                    },
                    {
                        id: 'recommend',
                        message: '고객님의 치즈 취향을 파악하여 추천받으시겠습니까?',
                        trigger: 'recommend1'
                    },
                    {
                        id: 'recommend1',
                        options: [
                            { value: 1, label: '네. 치츠 추천 받으러 갈게요!', trigger: 'recommend2' },
                            { value: 2, label: '아니요. 그냥 치즈 상품 구경하러 갈게요!', trigger: 'cheeseList' },
                            { value: 3, label: '다른 치즈 종류도 궁금해요!', trigger: 'category' },
                        ],
                    },
                    {
                        id: 'recommend2',
                        message: '그러면 고객님의 치즈 취향을 분석해보겠습니다. 총 5가지의 질문을 드리겠습니다!',
                        trigger: 'question1',
                    },
                    {
                        id: 'question1',
                        message: '치즈나 음식의 어떤 맛을 선호하시나요?',
                        trigger: 'tasty',
                    },
                    {
                        id: 'tasty',
                        options: [
                            { value: 1, label: '단맛', trigger: 'question2' },
                            { value: 2, label: '짠맛', trigger: 'question2' },
                            { value: 3, label: '신맛', trigger: 'question2' },
                            { value: 4, label: '쓴맛', trigger: 'question2' },
                            { value: 5, label: '담백한 맛', trigger: 'question2' },
                        ],
                    },
                    {
                        id: 'question2',
                        message: '치즈에 어떤 경도를 좋아하시나요?',
                        trigger: 'texture',

                    },
                    {
                        id: 'texture',
                        options: [
                            { value: 1, label: '후레쉬', trigger: 'chatbot_number' },
                            { value: 2, label: '소프트', trigger: 'chatbot_number' },
                            { value: 3, label: '세미하드', trigger: 'chatbot_number' },
                            { value: 4, label: '하드', trigger: 'chatbot_number' },
                        ],
                    },
                    {
                        id: 'category',
                        options: [
                            { value: 1, label: '리코타', trigger: 'ricotta' },
                            { value: 2, label: '까망베르', trigger: 'camembert'},
                            { value: 3, label: '모짜렐라', trigger: 'mozzarella' },
                            { value: 4, label: '체다', trigger: 'cheddar' },
                            { value: 5, label: '브리', trigger: 'brie' }
                        ],
                    },
                    {
                        id: 'ricotta',
                        message: '프레쉬 크림치즈의 일종인 리코타는 입자가 고와 약간 얼은 생크림 같고 순백색으로 부드럽습니다. 샐러드, 파스타, 빵이나 스낵과도 잘 어울리는 치즈입니다',
                        trigger: 'recommend'
                    },
                    {
                        id: 'camembert',
                        message: '파마산 치즈는 블록 형태로 가루를 내어 많은 요리에 쓰이는 치즈입니다. 좋은 와인과 그렇지 못한 와인을 가리는 품질평가회에서도 쓰입니다. 전세계적으로 피자나 파스타에 뿌려먹습니다.',
                        trigger: 'recommend'
                    },
                    {
                        id: 'mozzarella',
                        message: '리코타 치즈와 함께 가장 유명한 치즈입니다. 가열하였을 때 녹고 잡아당기면 늘어나는 특징이 있어서 피자 토핑에 이용되고 있습니다.',
                        trigger: 'recommend'
                    },
                    {
                        id: 'cheddar',
                        message: '풍부하고 부드러운 특유의 향과 맛으로 유명합니다. 샌드위치, 햄버거, 샐러드 등에 쓰입니다.',
                        trigger: 'recommend'
                    },
                    {
                        id: 'brie',
                        message: '부드러운 나무향과 버섯향이 진한 흰곰팡이 치즈로 치즈의 여왕이라고도 합니다. 레드와인과 잘 어울리고 냉장고에서 미리 꺼내두어 물렁하게 드시면 맛있습니다. ',
                        trigger: 'recommend'
                    },

                    {
                        id: 'cheeseList',
                        user: true,
                        trigger: 'itemSearchResult',
                    },
                    {
                        id: 'itemSearchResult',
                        component: <ItemSearch/>,
                        trigger: '1',
                    },
                    {
                        id: 'fare',
                        message: '주문사항을 입력해주세요.',
                        trigger: 'startName',
                    },
                    {
                        id: 'startName',
                        user: true,
                        trigger: 'fare1',
                    },
                    {
                        id: 'fare1',
                        message: '주문사항을 입력해주세요.',
                        trigger: 'arriveName'
                    },
                    {
                        id: 'arriveName',
                        user: true,
                        trigger: 'fareResult',
                    },
                    {
                        id: 'fareResult',
                        component: <ItemSearch2/>,
                        trigger: '1',
                    },
                    {
                        id: 'chatbot_number',
                        message: '고객님의 챗봇 번호를 입력해주세요.',
                        trigger: 'chatbot_id'
                    },
                    {
                        id: 'chatbot_id',
                        user: true,
                        trigger: 'user_number'
                    },
                    {
                        id: 'user_number',
                        message: '고객 아이디를 적어주세요.',
                        trigger: 'user_id'
                    },
                    {
                        id: 'user_id',
                        user: true,
                        trigger: 'review'
                    },
                    {
                        id: 'review',
                        component: <Review/>,
                        asMessage: true,
                        trigger: 'update',
                    },
                    {
                        id: 'update',
                        message: '결과를 확인하시겠습니까?',
                        trigger: 'update_question'
                    },
                    // {
                    //     id: 'update_question',
                    //     options: [
                    //         { value: 'yes', label: '아니오. 수정할게요.', trigger: 'update_yes'},
                    //         { value: 'no', label: '예', trigger: 'end-message'},
                    //     ],
                    // },
                    // {
                    //     id: 'update_yes',
                    //     message: '어떤 정보를 수정하시겠습니까?',
                    //     trigger: 'update-fields',
                    // },
                    // {
                    //     id: 'update-fields',
                    //     options: [
                    //         {}
                    //     ]
                    // },
                    {
                        id: 'update_question',
                        options: [
                            { value: 'no', label: '결과보러 가기', trigger: 'end-message'}
                        ],
                    },
                    {
                        id: 'end-message',
                        component: <Answer/>,
                        waitAction: true,
                        asMessage: true,
                        end: true,
                    },
                ]}
            />
        </ThemeProvider>  
        )
    }
}

export default MyChatbot

// const theme = {
//     background: '#f5f8fb',
//     fontFamily: 'Helvetica Neue',
//     headerBgColor: '#ffb74d',
//     headerFontColor: '#fff',
//     headerFontSize: '15px',
//     botBubbleColor: '#ffb74d',
//     botFontColor: '#black',
//     userBubbleColor: '#fff',
//     userFontColor: '#4a4a4a',
//     width: "500",
//     height: "900"
//   };

// export const ItemSearch = () => {
//         return (<>

//         </>)
    
// }

// export const ItemSearch2 = () => {
//     return (
//             <p>정보가 없습니다.</p>

//     )

// }

// export default function ChatbotContainer () {   
//     return (
//         <ThemeProvider theme={theme}>     
//             <ChatBot
//                 style={{ width: '700px'}}
//                 floating = {true}
//                 headerTitle = {'서비스'}
//                 enableSmoothScroll = {true}
//                 steps={[
//                     //서비스선택
//                     {
//                         id: '1',
//                         message: '원하시는 서비스를 선택해주세요.',
//                         trigger: '2',
//                     },
//                     {
//                         id: '2',
//                         options: [
//                             { value: 1, label: '치즈 추천 받기', trigger: 'recommend' },
//                             { value: 2, label: '치즈 종류 소개', trigger: 'category' },
//                             { value: 3, label: '구독회원', trigger: 'fare' },
//                             { value: 4, label: '비회원', trigger: 'fare' },
//                         ],
//                     },
//                     {
//                         id: 'recommend',
//                         message: '고객님의 치즈 취향을 파악하여 추천받으시겠습니까?',
//                         trigger: 'recommend1'
//                     },
//                     {
//                         id: 'recommend1',
//                         options: [
//                             { value: 1, label: '네. 치츠 추천 받으러 갈게요!', trigger: 'recommend2' },
//                             { value: 2, label: '아니요. 그냥 치즈 상품 구경하러 갈게요!', trigger: 'cheeseList' },
//                             { value: 3, label: '다른 치즈 종류도 궁금해요!', trigger: 'category' },
//                         ],
//                     },
//                     {
//                         id: 'recommend2',
//                         message: '그러면 고객님의 치즈 취향을 분석해보겠습니다. 총 5가지의 질문을 드리겠습니다!',
//                         trigger: 'question1',
//                     },
//                     {
//                         id: 'question1',
//                         message: '치즈나 음식의 어떤 맛을 선호하시나요?',
//                         trigger: 'quedstion2',
//                     },
//                     {
//                         id: 'quedstion2',
//                         options: [
//                             { value: 1, label: '단맛', trigger: 'question3' },
//                             { value: 2, label: '짠맛', trigger: 'question3' },
//                             { value: 3, label: '신맛', trigger: 'question3' },
//                             { value: 3, label: '쓴맛', trigger: 'question3' },
//                             { value: 3, label: '담백한 맛', trigger: 'question3' },
//                         ],
//                     },
//                     {
//                         id: 'question3',
//                         message: '치즈에 어떤 경도를 좋아하시나요?',
//                         // trigger: 'question4',
//                     },

//                     {
//                         id: 'category',
//                         options: [
//                             { value: 1, label: '리코타', trigger: 'ricotta' },
//                             { value: 2, label: '까망베르', trigger: 'camembert'},
//                             { value: 3, label: '모짜렐라', trigger: 'mozzarella' },
//                             { value: 4, label: '체다', trigger: 'cheddar' },
//                             { value: 5, label: '브리', trigger: 'brie' }
//                         ],
//                     },
//                     {
//                         id: 'ricotta',
//                         message: '프레쉬 크림치즈의 일종인 리코타는 입자가 고와 약간 얼은 생크림 같고 순백색으로 부드럽습니다. 샐러드, 파스타, 빵이나 스낵과도 잘 어울리는 치즈입니다',
//                         trigger: 'recommend'
//                     },
//                     {
//                         id: 'camembert',
//                         message: '파마산 치즈는 블록 형태로 가루를 내어 많은 요리에 쓰이는 치즈입니다. 좋은 와인과 그렇지 못한 와인을 가리는 품질평가회에서도 쓰입니다. 전세계적으로 피자나 파스타에 뿌려먹습니다.',
//                         trigger: 'recommend'
//                     },
//                     {
//                         id: 'mozzarella',
//                         message: '리코타 치즈와 함께 가장 유명한 치즈입니다. 가열하였을 때 녹고 잡아당기면 늘어나는 특징이 있어서 피자 토핑에 이용되고 있습니다.',
//                         trigger: 'recommend'
//                     },
//                     {
//                         id: 'cheddar',
//                         message: '풍부하고 부드러운 특유의 향과 맛으로 유명합니다. 샌드위치, 햄버거, 샐러드 등에 쓰입니다.',
//                         trigger: 'recommend'
//                     },
//                     {
//                         id: 'brie',
//                         message: '부드러운 나무향과 버섯향이 진한 흰곰팡이 치즈로 치즈의 여왕이라고도 합니다. 레드와인과 잘 어울리고 냉장고에서 미리 꺼내두어 물렁하게 드시면 맛있습니다. ',
//                         trigger: 'recommend'
//                     },

//                     {
//                         id: 'cheeseList',
//                         user: true,
//                         trigger: 'itemSearchResult',
//                     },
//                     {
//                         id: 'itemSearchResult',
//                         component: <ItemSearch/>,
//                         trigger: '1',
//                     },
//                     {
//                         id: 'fare',
//                         message: '주문사항을 입력해주세요.',
//                         trigger: 'startName',
//                     },
//                     {
//                         id: 'startName',
//                         user: true,
//                         trigger: 'fare1',
//                     },
//                     {
//                         id: 'fare1',
//                         message: '주문사항을 입력해주세요.',
//                         trigger: 'arriveName'
//                     },
//                     {
//                         id: 'arriveName',
//                         user: true,
//                         trigger: 'fareResult',
//                     },
//                     {
//                         id: 'fareResult',
//                         component: <ItemSearch2/>,
//                         trigger: '1',
//                     },
//                 ]}
//             />
//         </ThemeProvider>
//     )
// }
