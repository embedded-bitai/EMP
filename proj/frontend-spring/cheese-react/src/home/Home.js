import React from "react";
import tw from "twin.macro"; //eslint-disable-line
import { Link } from 'react-router-dom'; //eslint-disable-line
import AnimationRevealPage from "./AnimationRevealPage.js";
// import Header from "./common/header-practice.js"
import Hero from "./BackgroundAsImageWithCenteredContent.js";
import Features from "./VerticalWithAlternateImageAndText.js";
import Blog from "./Blogs.js";
import Testimonial from "./TwoColumnWithImage.js";
import ContactUsForm from "./SimpleContactUs.js";
import Footer from "./common/Footer.js";

import Header from "./common/Header.js";

const Home = () => <div className="home">
  <Header />
  <Hero />
  <AnimationRevealPage>
    <Features />
    <Blog />
    <Testimonial />
    <ContactUsForm />
  </AnimationRevealPage>
  <Footer />
  
</div>

export default Home
