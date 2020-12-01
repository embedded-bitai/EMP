import React from "react";
import tw from "twin.macro";
import styled from "styled-components";
import { css } from "styled-components/macro"; //eslint-disable-line

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

const Actions = styled.form`
  ${tw`relative max-w-md text-center mx-auto lg:mx-0`}
  input {
    ${tw`sm:pr-48 pl-8 py-4 sm:py-5 rounded-full border-2 w-full font-medium focus:outline-none transition duration-300 focus:border-primary-500 hover:border-gray-500`}
  }
  button {
    ${tw`w-full sm:absolute right-0 top-0 bottom-0 bg-primary-500 text-gray-100 font-bold mr-2 my-4 sm:my-2 rounded-full py-4 flex items-center justify-center sm:w-40 sm:leading-none focus:outline-none hover:bg-yellow-700 transition duration-300 bg-yellow-500`}
  }
`;

export default function BackgroundAsImageWithCenteredContent() {
  return (
    <div>
      <Container>
        {/* <OpacityOverlay /> */}
        <HeroContainer>
          <Content>
            <Heading>
                <h1>Find Your Cheese !</h1>
                나에게 맞는 치즈를 추천 받아보세요.
            </Heading>
            <br/>
            <Actions action="/signup">
              <input type="text" placeholder="Your E-mail Address" />
              <button herf="/signup">지금 시작하기</button>
            </Actions>
          </Content>
        </HeroContainer>
      </Container>
    </div>
  );
};