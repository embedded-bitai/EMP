import React from "react";
import styled from "styled-components" //eslint-disable-line
import tw from "twin.macro"; //eslint-disable-line
import "tailwindcss/dist/base.css";
import axios from "axios" //eslint-disable-line
import "../components/cmm/styles/globalStyles.css";
import { ChatbotContainer as Chatbot } from "../containers/cop/chatbot"

import AnimationRevealPage from "../components/cmm/AnimationEffect.jsx"; //eslint-disable-line
import {FullPage, Slide} from 'react-full-page' //eslint-disable-line
import RecommendTop from "../containers/cop/rec/recommend/RecommendTop.jsx";
import RecommendList from "../containers/cop/rec/recommend/RecommendList.jsx";

export default function Survey () {
  return (<>
    {/* <AnimationRevealPage> */}
      <Chatbot/>
      <RecommendTop />
      <RecommendList />
      {/* <RecommendResult /> */}
  </>)
}