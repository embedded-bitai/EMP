import React from "react";
import tw from "twin.macro";
import { css } from "styled-components/macro"; //eslint-disable-line
import { context as c } from '../../../../modules/context' //eslint-disable-line
// import HeaderBase, {
//   LogoLink as LogoLinkBase,
//   // NavLink as NavLinkBase,
//   // PrimaryLink as PrimaryLinkBase
// } from "../home/common/Header.jsx";

import { Container as ContainerBase, ContentWithVerticalPadding, Content2Xl } from "../../../../components/cmm/Layouts.jsx";
import { SectionHeading } from "../../../../components/cmm/Headings.jsx";
import { SectionDescription } from "../../../../components/cmm/Typography.jsx";
import { PrimaryButton as PrimaryButtonBase } from "../../../../components/cmm/Buttons.jsx";
// import logoImageSrc from "../images/logo-light.svg";
// import serverIllustrationImageSrc from "../../../../components/cmm/images/server-illustration-2.svg";
import RecommendSurvey from "./RecommendSurvey"

const PrimaryBackgroundContainer = tw.div`-mx-8 px-8 mt-16 mb-20 lg:mt-0 lg:ml-16 bg-white text-gray-100`;
const Container = tw(ContainerBase)`mt-32 mb-48 mx-16`;
const Row = tw.div`flex items-center flex-col lg:flex-row`;
const Column = tw.div`lg:w-1/2`;
const TextColumn = tw.div`text-center lg:text-left`;
const IllustrationColumn = tw(Column)`mt-16 lg:mt-0 lg:ml-16`;
const Heading = tw(SectionHeading)`max-w-3xl lg:max-w-4xl lg:text-center leading-tight text-black`;
const Description = tw(SectionDescription)`mt-4 max-w-2xl text-black lg:text-base mx-auto lg:mx-0`;
const PrimaryButton = tw(PrimaryButtonBase)`mt-8 text-sm sm:text-base px-6 py-5 sm:px-10 sm:py-5 bg-yellow-400 inline-block text-black hocus:bg-yellow-500`;
const Image = tw.img`w-144 ml-auto`



export default function RecommendTop ({
  heading = "치즈를 추천받고 구독하세요!",
  description = "지금 바로 Pic 2 Cheese 회원으로 가입해서 서비스를 즐겨보세요!",
  primaryButtonText = "지금 바로 구독하기",
  primaryButtonUrl = "/subscribe",
  // imageSrc = serverIllustrationImageSrc,
}) {

  return (
    <PrimaryBackgroundContainer>
      <Content2Xl>
        <Container>
          <ContentWithVerticalPadding>
            <Row>
              <TextColumn>
                <Heading>{heading}</Heading>
                <Description>{description}</Description>
                {/* <PrimaryButton as="a" href={primaryButtonUrl}>{primaryButtonText}</PrimaryButton> */}
              </TextColumn>
              {/* <IllustrationColumn>
                <Image src={imageSrc} />
              </IllustrationColumn> */}
            </Row>
            <RecommendSurvey/>
          </ContentWithVerticalPadding>
        </Container>
      </Content2Xl>
    </PrimaryBackgroundContainer>
  );
};
