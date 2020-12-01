import React from "react";
import styled from "styled-components" //eslint-disable-line
import tw from "twin.macro"; //eslint-disable-line
import "tailwindcss/dist/base.css";
import axios from "axios" //eslint-disable-line
import "../components/cmm/styles/globalStyles.css";

import AnimationRevealPage from "../components/cmm/AnimationEffect.jsx"; //eslint-disable-line
import {FullPage, Slide} from 'react-full-page' //eslint-disable-line
import RecommendTop from "../containers/cop/rec/recommend/RecommendTop.jsx";
import RecommendSurvey from "../containers/cop/rec/recommend/RecommendSurvey.jsx" //eslint-disable-line
import RecommendList from "../containers/cop/rec/recommend/RecommendList.jsx";
import RecommendResult from "../containers/cop/rec/recommend/RecommendResult.jsx";



export default function Survey () {
  return (<>
    {/* <AnimationRevealPage> */}
      <RecommendTop />
      {/* <RecommendSurvey/> */}
      <RecommendList />
      <RecommendResult />
  </>)
}