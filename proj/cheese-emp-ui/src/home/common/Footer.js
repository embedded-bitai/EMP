import React from "react";
import tw from "twin.macro";
import styled from "styled-components";
import { css } from "styled-components/macro"; //eslint-disable-line

import LogoImage from "../../images/cheese-logo.png";
// import LogoImage from "../../images/cheeseLogo.svg";
import { ReactComponent as FacebookIcon } from "../../images/facebook-icon.svg";
import { ReactComponent as TwitterIcon } from "../../images/twitter-icon.svg";
import { ReactComponent as YoutubeIcon } from "../../images/youtube-icon.svg";

const Container = tw.div`relative bg-gray-200 -mx-8 -mb-8 px-8`;
const FiveColumns = tw.div`max-w-screen-xl mx-auto py-16 lg:py-20 flex flex-wrap justify-between`;

const Column = tw.div`md:w-1/5`;
const WideColumn = tw(Column)`text-center md:text-left w-full md:w-2/5 mb-10 md:mb-0`;

const ColumnHeading = tw.h5`font-bold`;

const LinkList = tw.ul`mt-1 text-sm font-medium`;
const LinkListItem = tw.li`mt-3`;
const Link = tw.a`border-b-2 border-transparent hocus:text-yellow-500 hocus:border-yellow-500 pb-1 transition duration-300`;

const LogoContainer = tw.div`flex items-center justify-center md:justify-start`;
const LogoImg = tw.img`w-8`;
const LogoText = tw.h5`ml-2 text-xl font-black text-yellow-500`;

const CompanyDescription = tw.p`mt-4 max-w-xs font-medium text-sm mx-auto md:mx-0 md:mr-4 `;

const SocialLinksContainer = tw.div`mt-4 `;
const SocialLink = styled.a`
  ${tw`cursor-pointer inline-block p-2 rounded-full bg-gray-700 text-gray-100 hover:bg-gray-900 transition duration-300 mr-4`}
  svg {
    ${tw`w-4 h-4`}
  }
`;

export default () => {
  return (
    <Container>
      <FiveColumns>
        <WideColumn>
          <LogoContainer>
            <LogoImg src={LogoImage} />
            <LogoText>Pic 2 Cheese Inc.</LogoText>
          </LogoContainer>
          <CompanyDescription>
            Treact is an Internet Technology company providing design resources such as website templates and themes.
          </CompanyDescription>
          <SocialLinksContainer>
            <SocialLink href="https://facebook.com">
              <FacebookIcon />
            </SocialLink>
            <SocialLink href="https://twitter.com">
              <TwitterIcon />
            </SocialLink>
            <SocialLink href="https://youtube.com">
              <YoutubeIcon />
            </SocialLink>
          </SocialLinksContainer>
        </WideColumn>
        <Column>
          <LinkList>
            <LinkListItem>
              <Link href="#">BRAND</Link>
            </LinkListItem>
            <LinkListItem>
              <Link href="#">이용약관</Link>
            </LinkListItem>
            <LinkListItem>
              <Link href="#">개인정보처리방침</Link>
            </LinkListItem>
          </LinkList>
        </Column>
        <Column>
        <LinkList>
                <p>Pic2 Cheese(주)</p>
        <p>대표이사 : 옥수민,김유정,최민근,김병준</p>
        <p>서울시 송파구 송파대로 570</p>
        <p>사업자 등록번호 : 120-88-00767</p>
        통신판매업신고 : 2017-서울송파-0680
        </LinkList>
        </Column>
        <Column>
        <LinkList>
        <p>365고객센터 | 전자금융거래분쟁처리담당</p>
        <p>1577-7011</p>
        <p>서울시 송파구 송파대로 570</p>
        <p>email : help@pic2cheese.com</p>
        </LinkList>
        </Column>
      </FiveColumns>
    </Container>
  );
};
