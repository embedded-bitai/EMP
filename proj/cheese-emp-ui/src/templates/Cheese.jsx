import React from "react";
import tw from "twin.macro";
import AnimationRevealPage from "../components/cmm/AnimationEffect.jsx";
import CheeseTop from "../containers/cop/itm/cheese/CheeseTop.jsx";
import CheeseTexture from "../containers/cop/itm/cheese/CheeseTexture.jsx";
import { BestReview } from '../containers/cop/itm/cheese'
import CheeseMenu from "../containers/cop/itm/cheese/CheeseMenu.jsx";
import { ChatbotContainer as Chatbot } from "../containers/cop/chatbot"


export default function Cheese () {
  // const Subheading = tw.span`tracking-wider text-sm font-medium`;
  const HighlightedText = tw.span`bg-primary-500 text-gray-100 px-4 transform -skew-x-12 inline-block`;
  const imageCss = tw`rounded-4xl`;
  
  return (
    <div>
      <AnimationRevealPage>
        <Chatbot/>
        <CheeseTop
          heading={<>Delicious & Affordable <HighlightedText>Cheese Near You.</HighlightedText></>}
          description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
          imageSrc="https://img-cf.kurly.com/shop/data/goods/1515396236580l0.jpg"
          imageCss={imageCss}
          imageDecoratorBlob={true}
          primaryButtonText="Subscribe Now"
          watchVideoButtonText="Meet The Chefs"
          
        />
        </AnimationRevealPage>
        <CheeseTexture
          heading={
            <>
              Pic 2 Cheese's <HighlightedText>Recommend</HighlightedText>
            </>
          }
        />
        <AnimationRevealPage>
        <CheeseMenu />
        <BestReview/>
      </AnimationRevealPage>
    </div>
  );
}