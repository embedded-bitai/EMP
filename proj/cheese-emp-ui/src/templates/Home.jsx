import React from "react";
import tw from "twin.macro"; //eslint-disable-line
import { Link } from 'react-router-dom'; //eslint-disable-line
import AnimationRevealPage from "../components/cmm/AnimationEffect.jsx";
import MainBackground from "../containers/cmm/hom/MainBackground.jsx";
import HomeInfo from "../containers/cmm/hom/HomeInfo.jsx";
import ContactUs from "../containers/cmm/hom/SubscribeForm.jsx";
import { ChatbotContainer as Chatbot } from "../containers/cop/chatbot"
import FAQ from "../containers/cmm/hom/Faq.jsx";

  const Subheading = tw.span`uppercase tracking-widest font-bold text-primary-500`;
  const HighlightedText = tw.span`text-primary-500`;

export default function Home () {
  return( <div className="home">
  {/* <Header /> */}
  <AnimationRevealPage>
    <Chatbot/>
    <MainBackground />
    <HomeInfo />
  <FAQ
        subheading={<Subheading>FAQS</Subheading>}
        heading={
          <>
            You have <HighlightedText>Questions ?</HighlightedText>
          </>
        }
        faqs={[
          {
            question: "Pic 2 Cheese는 어떤 서비스 인가요?",
            answer:
              "Pic 2 Cheese는 취향을 분석해서 취향에 맞는 치즈를 추천해드립니다. "
          },
          {
            question: "추천 과정은 어떻게 이루어지나요?",
            answer:
              "인공지능 모델을 활용해서 구매패턴을 분석하거나 챗봇 설문조사를 통해 추천이 이루집니다. "
          },
          {
            question: "정기구독을 시작하면 약정기간이 있거나 해지가 어렵진 않나요?",
            answer:
            "Pic 2 Cheese의 정기구독은 별도의 약정기간이 없어요. 원할때는 홈페이지에 로그인해 언제든 직접 관리할 수 있어요."
          },
          {
            question: "잊고있다가 자동으로 결제가 되어버릴까봐 걱정돼요.",
            answer:
              "Pic 2 Cheese는 정기결제 2일 전에 미리 결제 알림을 카카오 알림톡으로 보내드려요. 가격과 주소 등 확인하고 관리할 수 있으니 안심하세요."
          },
          {
            question: "이번 달 치즈를 다 먹지 못하면 어떡하죠?",
            answer:
              "이런 저런 이유로 치즈를 다 드시지 못하셨군요. 걱정하지 마세요. 홈페이지에서 정기결제일을 언제든 직접 변경할 수 있어요. 언제든 내 맘대로 관리하는 정기구독 시작하세요.  "
          }
        ]}
      />
    <ContactUs />
  </AnimationRevealPage>      
</div>)
}