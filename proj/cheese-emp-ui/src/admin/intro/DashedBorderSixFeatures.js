import React from "react";
import styled from 'styled-components';
import tw from 'twin.macro';
//eslint-disable-next-line
//import { css } from "styled-components/macro";
import { SectionHeading } from './Headings';

import defaultCardImage from "../../images/shield-icon.svg";

import { ReactComponent as SvgDecoratorBlob3 } from "../../images/svg-decorator-blob-3.svg";

import SupportIconImage from "../../images/support-icon.svg";
import ShieldIconImage from "../../images/shield-icon.svg";
import CustomizeIconImage from "../../images/customize-icon.svg";
import FastIconImage from "../../images/fast-icon.svg";
import ReliableIconImage from "../../images/reliable-icon.svg";
import SimpleIconImage from "../../images/simple-icon.svg";

const Container = tw.div`relative`;

const ThreeColumnContainer = styled.div`
  ${tw`flex flex-col items-center md:items-stretch md:flex-row flex-wrap md:justify-center max-w-screen-xl mx-auto py-20 md:py-24`}
`;
const Heading = tw(SectionHeading)`w-full`;

const Column = styled.div`
  ${tw`md:w-1/2 lg:w-1/3 px-6 flex`}
`;

const Card = styled.div`
  ${tw`flex flex-col mx-auto max-w-xs items-center px-6 py-10 border-2 border-dashed border-primary-500 rounded-lg mt-12`}
  .imageContainer {
    ${tw`border-2 border-primary-500 text-center rounded-full p-6 flex-shrink-0 relative`}
    img {
      ${tw`w-8 h-8`}
    }
  }

  .textContainer {
    ${tw`mt-6 text-center`}
  }

  .title {
    ${tw`mt-2 font-bold text-xl leading-none text-primary-500`}
  }

  .description {
    ${tw`mt-3 font-semibold text-secondary-100 text-sm leading-loose`}
  }
`;

const DecoratorBlob = styled(SvgDecoratorBlob3)`
  ${tw`pointer-events-none absolute right-0 bottom-0 w-64 opacity-25 transform translate-x-32 translate-y-48 `}
`;

export default () => {
  /*
   * This componets has an array of object denoting the cards defined below. Each object in the cards array can have the key (Change it according to your need, you can also add more objects to have more cards in this feature component):
   *  1) imageSrc - the image shown at the top of the card
   *  2) title - the title of the card
   *  3) description - the description of the card
   *  If a key for a particular card is not provided, a default value is used
   */

  const cards = [
    {
      imageSrc: ShieldIconImage,
      title: "치즈 추천 AI 플랫폼 'OOO' 입니다.",
      description: "세상에는 셀 수 없을 정도의 치즈가 있다는 것 알고 계시나요?"
    },

    { imageSrc: SupportIconImage, 
      title: "치즈 전문가 챗봇",
      description: "치즈에 대한 모든 것을 알고있는 챗봇과 이야기를 나눠보세요."
    },

    { imageSrc: CustomizeIconImage,
      title: "정확한 추천",
      description: "취향에 맞는 치즈를 추천해드려요."
    },
    
    { imageSrc: FastIconImage,
      title: "번개같은 속도",
      description: "복잡하지 않은 설문과 빠른 분석을 통해 여러분의 시간을 아껴드려요."
    },

    { imageSrc: SimpleIconImage,
      title: "치즈 추천 서비스",
      description: "고객 여러분들이 감동할만한 추천 서비스를 제공합니다."
    },

    { imageSrc: ReliableIconImage,
      title: "다양한 치즈를 구경해보세요",
      description: "자동 배송까지 기다리기 어려운 고객님들을 위해 치즈 마켓을 통해 직접 주문할 수 있는 서비스도 제공합니다. 지금 시작해보세요."
    },
  ];

  return (
    <Container>
      <ThreeColumnContainer>
        <Heading>Our Professional <span tw="text-primary-500">Services</span></Heading>
        {cards.map((card, i) => (
          <Column key={i}>
            <Card>
              <span className="imageContainer">
                <img src={card.imageSrc || defaultCardImage} alt="" />
              </span>
              <span className="textContainer">
                <span className="title">{card.title || "Fully Secure"}</span>
                <p className="description">
                  {card.description || "일괄 적용되는 description 입니다."}
                </p>
              </span>
            </Card>
          </Column>
        ))}
      </ThreeColumnContainer>
      <DecoratorBlob />
    </Container>
  );
};
