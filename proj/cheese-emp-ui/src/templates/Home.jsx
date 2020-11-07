import React from "react";
import tw from "twin.macro"; //eslint-disable-line
import { Link } from 'react-router-dom'; //eslint-disable-line
import AnimationRevealPage from "../containers/cmm/hom/AnimationPage.js";
// import Header from "./common/header-practice.js"
import Hero from "../containers/cmm/hom/BackgroundAsImageWithCenteredContent.js";
import Features from "../containers/cmm/hom/VerticalWithAlternateImageAndText.js";
// import Blog from "./Blogs.js";
// import Testimonial from "./TwoColumnWithImage.js";
import ContactUsForm from "../containers/cmm/hom/SimpleContactUs.js";
import Footer from "../components/cmm/Footer.js";

import Header from "../components/cmm/Header.js";

const Home = () => {
  return (<>
      <Header />
      <Hero />
      <AnimationRevealPage>
        <Features />
        {/* <Blog />
        <Testimonial /> */}
        <ContactUsForm />
      </AnimationRevealPage>
      <Footer />
  </>)
}

export default Home
