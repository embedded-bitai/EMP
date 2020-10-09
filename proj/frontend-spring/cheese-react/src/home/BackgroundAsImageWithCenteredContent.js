import React from "react";
import tw from "twin.macro";
import styled from "styled-components";
import { css } from "styled-components/macro"; //eslint-disable-line

import Header, { NavLink, LogoLink, NavToggle, DesktopNavLinks } from "./Headers.js";

const StyledHeader = styled(Header)`
  ${tw`pt-8 max-w-none w-full`}
  ${DesktopNavLinks} ${NavLink}, ${LogoLink} {
    ${tw`text-gray-100 hover:border-gray-300 hover:text-gray-300`}
  }
  ${NavToggle}.closed {
    ${tw`text-gray-100 hover:text-primary-500`}
  }
`;

// const PrimaryLink = tw(PrimaryLinkBase)`rounded-full`
const Container = styled.div`
  ${tw`relative -mx-8 -mt-8 bg-center bg-cover h-screen min-h-144`}
  background-image: url("https://post-phinf.pstatic.net/MjAyMDA2MDNfMjE4/MDAxNTkxMTQ4ODg0MzY5.MjSnIId_fn5_Cqe07p8FaJvzRbCrJZsECjfm2e6CHOsg.HKKfGRtpu4XehJI2yo9qyJ3Rm5zUn8pPa46WONNboNUg.JPEG/%EC%9C%A0%EC%96%B4%EB%84%A4%EC%9D%B4%ED%82%A4%EB%93%9C%EC%B9%98%EC%A6%88_%282%29.jpg?type=w1200");
`;

// const OpacityOverlay = tw.div`z-10 absolute inset-0 bg-black opacity-75`;

const HeroContainer = tw.div`z-20 relative px-6 sm:px-8 mx-auto h-full flex flex-col`;
const Content = tw.div`px-4 flex flex-1 flex-col justify-center items-center`;

const Heading = styled.h1`
  ${tw`text-3xl text-center sm:text-4xl lg:text-5xl xl:text-6xl font-black text-gray-100 leading-snug -mt-24 sm:mt-0`}
  span {
    ${tw`inline-block mt-2`}
  }
`;

const PrimaryAction = tw.button`rounded-full px-8 py-3 mt-10 text-sm sm:text-base sm:mt-16 sm:px-8 sm:py-4 bg-gray-100 font-bold shadow transition duration-300 bg-primary-500 text-gray-100 hocus:bg-primary-700 hocus:text-gray-200 focus:outline-none focus:shadow-outline`;

export default () => {
  const navLinks = [
  //   <NavLinks key={1}>
  //     {/* <NavLink href="#">
  //       About
  //     </NavLink>
  //     <NavLink href="#">
  //       Blog
  //     </NavLink >*/
  //     <NavLink href="/components/landingPages/HostingCloudLandingPage">
  //       Survey
  //     </NavLink>}
  //     <NavLink href="/components/landingPages/RestaurantLandingPage">
  //       Menu
  //     </NavLink>
  //   </NavLinks>,
  //   <NavLinks key={2}>
  //     <PrimaryLink href="/components/innerPages/LoginPage">
  //       Log In
  //     </PrimaryLink>
  //     <PrimaryLink href="/components/innerPages/SignupPage">
  //       Sign Up
  //     </PrimaryLink>
  // </NavLinks>
  ];

  return (
    <Container>
      {/* <OpacityOverlay /> */}
      <HeroContainer>
        <StyledHeader links={navLinks} />
        <Content>
          <Heading>
              {/* 메인페이지 & 로그인/회원가입
              <br />
              설문지, 상품 리스트 페이지 */}
          </Heading>
          <PrimaryAction href="/components/blocks/Pricing/ThreePlansWithHalfPrimaryBackground">
            Search Events Near Me
          </PrimaryAction>
        </Content>
      </HeroContainer>
    </Container>
  );
};
