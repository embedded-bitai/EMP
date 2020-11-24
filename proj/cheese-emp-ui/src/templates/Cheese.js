import React from "react";
import tw from "twin.macro";
import axios from "axios"
import AnimationRevealPage from "../containers/cmm/hom/AnimationPage.js";
import Hero from "../containers/cop/itm/cheese/TwoColumnWithVideo.js";
// import StyledHeader from '../home/BackgroundAsImageWithCenteredContent'

// import Features from "./ThreeColSimple.js";
// import MainFeature from "./TwoColWithButton.js";
// import MainFeature2 from "./TwoColSingleFeatureWithStats2.js";

import TabGrid from "../containers/cop/itm/cheese/TabCardGrid.js";
import Testimonial from "../containers/cop/itm/cheese/ThreeColumnWithProfileImage.js";
// import Footer from "./FiveColumnWithInputForm.js";
import Footer from "../components/cmm/Footer.js";

// import chefIconImageSrc from "../images/chef-icon.svg";
// import celebrationIconImageSrc from "../images/celebration-icon.svg";
// import shopIconImageSrc from "../images/shop-icon.svg";

import Header from "../components/cmm/Header.js";
import Blog from "../containers/cmm/hom/Blogs.js";

export default () => {
  // const Subheading = tw.span`tracking-wider text-sm font-medium`;
  const HighlightedText = tw.span`bg-primary-500 text-gray-100 px-4 transform -skew-x-12 inline-block`;
  // const HighlightedTextInverse = tw.span`bg-gray-100 text-primary-500 px-4 transform -skew-x-12 inline-block`;
  // const Description = tw.span`inline-block mt-8`;
  const imageCss = tw`rounded-4xl`;

  const cheeseAxios = () => {
    axios.get(`http://localhost:8080/api/cheese`)
      .then(res => {
        alert(`Cheese Connection Success !!`)
      }).catch(
        e => alert(`Cheese Failure`)
      )
  }


  return (
    <div>
      <Header />
      <AnimationRevealPage>
        <button onClick={cheeseAxios}>Cheese axios</button>
        <Hero
          heading={<>Delicious & Affordable <HighlightedText>Cheese Near You. 랜덤 치즈 (이벤트,광고) 보여주기</HighlightedText></>}
          description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
          imageSrc="https://images.unsplash.com/photo-1504674900247-0877df9cc836?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=768&q=80"
          imageCss={imageCss}
          imageDecoratorBlob={true}
          primaryButtonText="Order Now"
          watchVideoButtonText="Meet The Chefs"
        />
        {/* <MainFeature
          subheading={<Subheading>Established Since 2014</Subheading>}
          heading={
            <>
              We've been serving for
              <wbr /> <HighlightedText>over 5 years.</HighlightedText>
            </>
          }
          description={
            <Description>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et
              dolore magna aliqua.
              <br />
              <br />
              Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
            </Description>
          }
          buttonRounded={false}
          textOnLeft={false}
          primaryButtonText="Latest Offers"
          imageSrc={
            "https://images.unsplash.com/photo-1460306855393-0410f61241c7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=768&q=80"
          }
          imageCss={imageCss}
          imageDecoratorBlob={true}
          imageDecoratorBlobCss={tw`left-1/2 -translate-x-1/2 md:w-32 md:h-32 opacity-25`}
        /> */}
        <Blog />
        </AnimationRevealPage>

        {/* TabGrid Component also accepts a tabs prop to customize the tabs and its content directly. Please open the TabGrid component file to see the structure of the tabs props.*/}
        <TabGrid
          heading={
            <>
              Checkout our <HighlightedText>menu.</HighlightedText>
            </>
          }
        />
        <AnimationRevealPage>
        {/* <Features
          heading={
            <>
              Amazing <HighlightedText>Services.</HighlightedText>
            </>
          }
          cards={[
            {
              imageSrc: shopIconImageSrc,
              title: "230+ Locations",
              description: "Lorem ipsum donor amet siti ceali placeholder text",
              url: "https://google.com"
            },
            {
              imageSrc: chefIconImageSrc,
              title: "Professional Chefs",
              description: "Lorem ipsum donor amet siti ceali placeholder text",
              url: "https://timerse.com"
            },
            {
              imageSrc: celebrationIconImageSrc,
              title: "Birthday Catering",
              description: "Lorem ipsum donor amet siti ceali placeholder text",
              url: "https://reddit.com"
            }
          ]}

          imageContainerCss={tw`p-2!`}
          imageCss={tw`w-20! h-20!`}
        />
        <MainFeature2
          subheading={<Subheading>A Reputed Brand</Subheading>}
          heading={<>Why <HighlightedText>Choose Us ?</HighlightedText></>}
          statistics={[
            {
              key: "Orders",
              value: "94000+",
            },
            {
              key: "Customers",
              value: "11000+"
            },
            {
              key: "Chefs",
              value: "1500+"
            }
          ]}
          primaryButtonText="Order Now"
          primaryButtonUrl="https://order.now.com"
          imageInsideDiv={false}
          imageSrc="https://images.unsplash.com/photo-1414235077428-338989a2e8c0?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEzNzI2fQ&auto=format&fit=crop&w=768&q=80"
          imageCss={Object.assign(tw`bg-cover`, imageCss)}
          imageContainerCss={tw`md:w-1/2 h-auto`}
          imageDecoratorBlob={true}
          imageDecoratorBlobCss={tw`left-1/2 md:w-32 md:h-32 -translate-x-1/2 opacity-25`}
          textOnLeft={true}
        /> */}
        <Testimonial
          subheading=""
          heading={<>Customers <HighlightedText>Love Us.</HighlightedText></>}
        />

      </AnimationRevealPage>
      <Footer />
    </div>
  );
}