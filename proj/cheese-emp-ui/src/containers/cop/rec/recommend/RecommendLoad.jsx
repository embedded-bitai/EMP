import React from 'react';
import styled from 'styled-components';
import tw from 'twin.macro';
import { css } from 'styled-components/macro'; //eslint-disable-line
import {ReactComponent as SvgDotPatternIcon} from '../../../../components/cmm/images/dot-pattern.svg'
// import { Signup } from '../../usr/user';
const Container = tw.div`relative `;
const Content = tw.div`max-w-screen-xl mx-auto py-20 lg:py-24`;
const FormContainer = styled.div`
  ${tw`p-10 sm:p-12 md:p-16 border-2 border-green-500 bg-white text-black text-center rounded-lg relative`}
  form {
    ${tw`mt-16 mb-16`}
  }
  h2 {
    ${tw`text-3xl sm:text-4xl font-bold mt-16`}
  }
`;
// const TwoColumn = tw.div`flex flex-col sm:flex-row justify-between`;
// const Column = tw.div`sm:w-5/12 flex flex-col`;
// const InputContainer = tw.div`relative py-5 mt-6`;
// const Label = tw.label`absolute top-0 left-0 tracking-wide font-semibold text-sm`;
// const Input = tw.input``;
// const TextArea = tw.textarea`h-24 sm:h-full resize-none`;
const SubmitButton = tw.button`w-full sm:w-32 mt-6 py-3 bg-green-300 text-black rounded-full font-bold tracking-wide shadow-lg uppercase text-sm transition duration-300 transform focus:outline-none focus:shadow-outline hover:bg-green-300 hover:text-black hocus:-translate-y-px hocus:shadow-xl`;
const SvgDotPattern1 = tw(SvgDotPatternIcon)`absolute bottom-0 right-0 transform translate-y-1/2 translate-x-1/2 -z-10 opacity-50 text-primary-500 fill-current w-24`
export default function RecommendLoad() {
  return (
    <Container>
      <Content>
        <FormContainer>
          <div tw="mx-auto max-w-4xl">
            <h2>고객님의 치즈 취향 분석이 끝났습니다!</h2>
            <h3>[결과 보기] 버튼을 눌러 확인해주세요!</h3>
            <form action="/recommend-result">
              <SubmitButton type="submit" value="Submit">결과 보기</SubmitButton>
            </form>
          </div>
          <SvgDotPattern1 />
        </FormContainer>
      </Content>
    </Container>
  );
};