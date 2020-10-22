import React from "react";
import axios from 'axios'
import tw from "twin.macro";
import { css } from "styled-components/macro"; //eslint-disable-line
import HeaderBase, {
  LogoLink as LogoLinkBase,
  // NavLink as NavLinkBase,
  // PrimaryLink as PrimaryLinkBase
} from "../home/common/Header.js";
import { Container as ContainerBase, ContentWithVerticalPadding, Content2Xl } from "../home/common/Layouts.js";
import { SectionHeading } from "../home/common/Headings.js";
import { SectionDescription } from "../home/common/Typography.js";
import { PrimaryButton as PrimaryButtonBase } from "../home/common/Buttons.js";
import logoImageSrc from "../images/logo-light.svg";
import serverIllustrationImageSrc from "../images/server-illustration-2.svg";

const PrimaryBackgroundContainer = tw.div`-mx-8 px-8 bg-yellow-500 text-gray-100`;
const Header = tw(HeaderBase)`max-w-none -mt-8 py-8 -mx-8 px-8`;
// const NavLink = tw(NavLinkBase)`lg:text-gray-100 lg:hocus:text-gray-300 lg:hocus:border-gray-100`;
const LogoLink = tw(LogoLinkBase)`text-gray-100 hocus:text-gray-300`;
// const PrimaryLink = tw(PrimaryLinkBase)`shadow-raised lg:bg-primary-400 lg:hocus:bg-primary-500`;

const Container = tw(ContainerBase)``;
const Row = tw.div`flex items-center flex-col lg:flex-row`;
const Column = tw.div`lg:w-1/2`;
const TextColumn = tw.div`text-center lg:text-left`;
const IllustrationColumn = tw(Column)`mt-16 lg:mt-0 lg:ml-16`;
const Heading = tw(SectionHeading)`max-w-3xl lg:max-w-4xl lg:text-left leading-tight`;
const Description = tw(SectionDescription)`mt-4 max-w-2xl text-gray-100 lg:text-base mx-auto lg:mx-0`;
const PrimaryButton = tw(PrimaryButtonBase)`mt-8 text-sm sm:text-base px-6 py-5 sm:px-10 sm:py-5 bg-yellow-400 inline-block text-black hocus:bg-yellow-500`;
const Image = tw.img`w-144 ml-auto`

const recommend= () => {
  axios.get(`http://localhost:8080/recommend`)
    .then(res => {
       alert(`Connection Success !!`)
}
  ).catch(
    e => alert(`Failure`)
  )
} 

export default ({
  heading = "설문지 형식과 결과 페이지",
  description = "설문지를 끝내고 제출하기 버튼 누르면 결과 페이지 볼 수 있도록 만들 것입니다.",
  primaryButtonText = "Find Your Cheese",
  primaryButtonUrl = "#",
  imageSrc = serverIllustrationImageSrc,
}) => {
  const logoLink = (
    <LogoLink href="/">
      <img src={logoImageSrc} alt="Logo" />
      메인페이지
    </LogoLink>
  );
  const navLinks = [
  ];
  return (
    <PrimaryBackgroundContainer>      
      <Content2Xl>
        <Header logoLink={logoLink} links={navLinks} />
        <Container>
          <ContentWithVerticalPadding>
            <Row>
              <TextColumn>
                <Heading>{heading}</Heading>
                <Description>{description}</Description>
                {/* <PrimaryButton as="a" href={primaryButtonUrl}>{primaryButtonText}</PrimaryButton> */}
                <PrimaryButton onClick={recommend}>{primaryButtonText}</PrimaryButton>
              </TextColumn>
              <IllustrationColumn>
                <Image src={imageSrc} />
              </IllustrationColumn>
            </Row>
          </ContentWithVerticalPadding>
        </Container>
      </Content2Xl>
    </PrimaryBackgroundContainer>
  );
};
