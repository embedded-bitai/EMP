import React from "react";
import tw from "twin.macro"; //eslint-disable-line
import "tailwindcss/dist/base.css";
import "../styles/globalStyles.css";
import AnimationRevealPage from "../home/AnimationRevealPage.js";
import Header from "../home/common/Header.js";
import Hero from "./TwoColumnWithPrimaryBackground.js";
import Pricing from "./ThreePlansWithHalfPrimaryBackground.js";
import FAQ from "./TwoColumnPrimaryBackground.js";
// import Footer from "./FiveColumnDark.js";
import Footer from "../home/common/Footer.js";

// const Header = tw(HeaderBase)`max-w-none`;

export default () => {
  return (
    <div>
      <Header />
      <Hero />
      <AnimationRevealPage>
        {/* <Features /> */}
        <Pricing />
        {/* <MainFeature 
          subheading="Reliable"
          heading="Highly Redundant Servers With Backup"
          imageSrc={serverRedundancyIllustrationImageSrc}
          buttonRounded={false}
        />
        <MainFeature 
          subheading="Secure"
          heading="State of the Art Computer Security"
          imageSrc={serverSecureIllustrationImageSrc}
          buttonRounded={false}
          textOnLeft={false}
        /> */}
        {/* <Testimonial /> */}
        <FAQ />
      </AnimationRevealPage>
      <Footer />
    </div>
  );
}
