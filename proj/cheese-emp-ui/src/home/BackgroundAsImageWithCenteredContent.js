import React from "react";
import tw from "twin.macro";
import styled from "styled-components";
import { css } from "styled-components/macro"; //eslint-disable-line
import axios from 'axios'

const Container = styled.div`
  ${tw`relative -mx-3 bg-center bg-cover h-screen min-h-144 pt-10`}
  background-image: url("https://post-phinf.pstatic.net/MjAyMDA2MDNfMjE4/MDAxNTkxMTQ4ODg0MzY5.MjSnIId_fn5_Cqe07p8FaJvzRbCrJZsECjfm2e6CHOsg.HKKfGRtpu4XehJI2yo9qyJ3Rm5zUn8pPa46WONNboNUg.JPEG/%EC%9C%A0%EC%96%B4%EB%84%A4%EC%9D%B4%ED%82%A4%EB%93%9C%EC%B9%98%EC%A6%88_%282%29.jpg?type=w1200");
`;
// const Heading = styled.h1`
//   ${tw`text-3xl text-center sm:text-4xl lg:text-5xl xl:text-6xl font-black text-gray-100 leading-snug -mt-24 sm:mt-0 pt-10`}
//   span {
//     ${tw`inline-block mt-2`}
//   }
// `;


const HeroContainer = tw.div`z-20 relative px-6 sm:px-8 mx-auto h-full flex flex-col pt-10`;
const Content = tw.div`px-4 flex flex-1 flex-col justify-center items-center`;

const PrimaryAction = tw.button`rounded-full px-8 py-3 mt-10 text-sm sm:text-base sm:mt-16 sm:px-8 sm:py-4 bg-gray-100 font-bold shadow transition duration-300 bg-yellow-500 text-black hocus:bg-yellow-700 hocus:text-gray-200 focus:outline-none focus:shadow-outline`;

const homeAxios = () => {
  axios.get(`http://localhost:8080/api`)
    .then(res => {
      alert(`Home Connection Success !!`)
    }).catch(
      e => alert(`Home Failure`)
    )
}

export default () => {
  return (
    <Container>
      {/* <OpacityOverlay /> */}
      <HeroContainer>
        <Content>
          {/* <Heading>
              메인페이지 & 로그인/회원가입
              <br />
              설문지, 상품 리스트 페이지
          </Heading> */}
          <PrimaryAction onClick={homeAxios}>
            Home axios
          </PrimaryAction>
        </Content>
      </HeroContainer>
    </Container>
  );
};
