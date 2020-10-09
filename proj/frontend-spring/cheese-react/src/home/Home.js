import React from "react";
import { Link } from 'react-router-dom'; //eslint-disable-line
import AnimationRevealPage from "./AnimationRevealPage.js";
import Menu from "./Menu.js"
import Hero from "./BackgroundAsImageWithCenteredContent.js";
import Features from "./VerticalWithAlternateImageAndText.js";
import Blog from "./Blogs.js";
import Testimonial from "./TwoColumnWithImage.js";
import ContactUsForm from "./SimpleContactUs.js";
import Footer from "./SimpleFiveColumn.js";

const Home = () => <div className="home">
  <Menu />
  {/* <h1> [홈] </h1>
  <nav>
      <Link to={"signup"}> [회원가입] </Link>
      <Link to={"login"}>[로그인]</Link>
      <Link to={"menu"}>[치즈]</Link>
      <Link to={"order"}>[주문]</Link>
      <Link to={"board"}>[F&Q]</Link>
      <Link to={"survey"}>[추천]</Link>
      <Link to={"admin"}>[Admin]</Link>
  </nav> */}
  <AnimationRevealPage>
    <Hero />
    <Features />
    <Blog />
    <Testimonial />
    <ContactUsForm />
    <Footer />
  </AnimationRevealPage>
);
</div>

export default Home
