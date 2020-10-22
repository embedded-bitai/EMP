import React from "react";
import tw from "twin.macro"; //eslint-disable-line
import "tailwindcss/dist/base.css";
import axios from "axios" //eslint-disable-line
import "../styles/globalStyles.css";
import AnimationRevealPage from "../home/AnimationPage.js";
import Header from "../home/common/Header.js";
import Hero from "./TwoColumnWithPrimaryBackground.js";
import Pricing from "./ThreePlansWithHalfPrimaryBackground.js";
import FAQ from "./TwoColumnPrimaryBackground.js";
import Footer from "../home/common/Footer.js";

// const Header = tw(HeaderBase)`max-w-none`;

const Survey = () => {
  return (<>
    <Header />
    <Hero />
    <AnimationRevealPage>
      <Pricing />
      <FAQ />
    </AnimationRevealPage>
    <Footer />
  </>)
}

export default Survey