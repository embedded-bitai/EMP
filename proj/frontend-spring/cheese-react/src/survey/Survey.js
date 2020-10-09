import "tailwindcss/dist/base.css";
import "../styles/globalStyles.css";
import React from "react";
import AnimationRevealPage from "./AnimationRevealPage.js";
import Hero from "./TwoColumnWithPrimaryBackground.js";
import Pricing from "./ThreePlansWithHalfPrimaryBackground.js";
import FAQ from "./TwoColumnPrimaryBackground.js";
import Footer from "./FiveColumnDark.js";
import Menu from '../home/Menu.js'

export default () => {
  return (
    <AnimationRevealPage>
      <Menu />
      <Hero />
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
      <Footer />
    </AnimationRevealPage>
  );
}
