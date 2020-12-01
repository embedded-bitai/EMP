import React, { useState } from "react";
import { motion } from "framer-motion";
import tw from "twin.macro";
import styled from "styled-components";
import { css } from "styled-components/macro"; //eslint-disable-line
import { Container, ContentWithPaddingXl } from "../../../../components/cmm/Layouts.jsx";
import { SectionHeading } from "../../../../components/cmm/Headings.jsx";
import { PrimaryButton as PrimaryButtonBase } from "../../../../components/cmm/Buttons.jsx";
import { ReactComponent as StarIcon } from "../../../../components/cmm/images/star-icon.svg";
import { ReactComponent as SvgDecoratorBlob1 } from "../../../../components/cmm/images/svg-decorator-blob-5.svg";
import { ReactComponent as SvgDecoratorBlob2 } from "../../../../components/cmm/images/svg-decorator-blob-7.svg";


const HeaderRow = tw.div`flex justify-between items-center flex-col xl:flex-row`;
const Header = tw(SectionHeading)``;
const TabsControl = tw.div`flex flex-wrap bg-gray-200 px-2 py-2 rounded leading-none mt-12 xl:mt-0`;

const TabControl = styled.div`
  ${tw`cursor-pointer px-6 py-3 mt-2 sm:mt-0 sm:mr-2 last:mr-0 text-gray-600 font-medium rounded-sm transition duration-300 text-sm sm:text-base w-1/2 sm:w-auto text-center`}
  &:hover {
    ${tw`bg-gray-300 text-gray-700`}
  }
  ${props => props.active && tw`bg-primary-500! text-gray-100!`}
  }
`;

const TabContent = tw(motion.div)`mt-6 flex flex-wrap sm:-mr-10 md:-mr-6 lg:-mr-12`;
const CardContainer = tw.div`mt-10 w-full sm:w-1/2 md:w-1/3 lg:w-1/4 sm:pr-10 md:pr-6 lg:pr-12`;
const Card = tw(motion.a)`bg-gray-200 rounded-b block max-w-xs mx-auto sm:max-w-none sm:mx-0`;
const CardImageContainer = styled.div`
  ${props => css`background-image: url("${props.imageSrc}");`}
  ${tw`h-56 xl:h-64 bg-center bg-cover relative rounded-t`}
`;
const CardRatingContainer = tw.div`leading-none absolute inline-flex bg-gray-100 bottom-0 left-0 ml-4 mb-4 rounded-full px-5 py-2 items-end`;
const CardRating = styled.div`
  ${tw`mr-1 text-sm font-bold flex items-end`}
  svg {
    ${tw`w-4 h-4 fill-current text-orange-400 mr-1`}
  }
`;

const CardHoverOverlay = styled(motion.div)`
  background-color: rgba(255, 255, 255, 0.5);
  ${tw`absolute inset-0 flex justify-center items-center`}
`;
const CardButton = tw(PrimaryButtonBase)`text-sm`;

const CardReview = tw.div`font-medium text-xs text-gray-600`;

const CardText = tw.div`p-4 text-gray-900`;
const CardTitle = tw.h5`text-lg font-semibold group-hover:text-primary-500`;
const CardContent = tw.p`mt-1 text-sm font-medium text-gray-600`;
const CardPrice = tw.p`mt-4 text-xl font-bold`;

const DecoratorBlob1 = styled(SvgDecoratorBlob1)`
  ${tw`pointer-events-none -z-20 absolute right-0 top-0 h-64 w-64 opacity-15 transform translate-x-2/3 -translate-y-12 text-pink-400`}
`;
const DecoratorBlob2 = styled(SvgDecoratorBlob2)`
  ${tw`pointer-events-none -z-20 absolute left-0 bottom-0 h-80 w-80 opacity-15 transform -translate-x-2/3 text-primary-500`}
`;

export default function CheeseTexture({
  heading = "Checkout the Menu",
  tabs = {
    후레쉬치즈: [
      {
        imageSrc:
          "https://img-cf.kurly.com/shop/data/goods/1515396236580l0.jpg",
        title: "[벨지오이오소]부라타 치즈",
        content: "Tomato Salad & Carrot",
        price: "$5.99",
        rating: "5.0",
        reviews: "87",
        // url: "#",
      },
      {
        imageSrc:
          "https://img-cf.kurly.com/shop/data/goods/1544576315159l0.jpg",
        title: "[프란시아]모짜렐라 카우",
        content: "Cheese Pizza",
        price: "$2.99",
        rating: "4.8",
        reviews: "32",
        // url: "#"
      },
      {
        imageSrc:
        "https://img-cf.kurly.com/shop/data/goods/1546415956691l0.jpg",
        title: "[브렐렛]모짜렐라 카우",
        content: "Hamburger & Fries",
        price: "$7.99",
        rating: "4.9",
        reviews: "89",
        // url: "#"
      },
      {
        imageSrc:
        "https://img-cf.kurly.com/shop/data/goods/1522737162969l0.jpg",
        title: "[브리미]보코치니",
        content: "Crispy Soyabeans",
        price: "$8.99",
        rating: "4.6",
        reviews: "12",
        // url: "#"
      },
      {
        imageSrc:
        "https://img-cf.kurly.com/shop/data/goods/1583469543917l0.jpg",
        title: "[무르젤라]이탈리아 부라타 120g",
        content: "Roasted Chicken & Egg",
        price: "$7.99",
        rating: "4.2",
        reviews: "19",
        url: "#"
      },
      {
        imageSrc:
        "https://img-cf.kurly.com/shop/data/goods/1548133518976l0.jpg",
        title: "[오로비안코]부라타 치즈",
        content: "Deepfried Chicken",
        price: "$2.99",
        rating: "5.0",
        reviews: "61",
        url: "#"
      },
      {
        imageSrc:
        "https://img-cf.kurly.com/shop/data/goods/1552973598931l0.jpg",
        title: "[프란시아]리코타 치즈",
        content: "Mexican Chilli",
        price: "$3.99",
        rating: "4.2",
        reviews: "95",
        url: "#"
      },
      {
        imageSrc:
        "https://img-cf.kurly.com/shop/data/goods/152663317697l0.jpg",
        title: "[zott]바질 모짜렐라 치즈",
        content: "Chilli Crispy Nachos",
        price: "$3.99",
        rating: "3.9",
        reviews: "26",
        url: "#"
      },
    ],
    소프트치즈: [
      {
        imageSrc:
        "https://img-cf.kurly.com/shop/data/goods/1566382934703l0.jpg",
        title: "[카스텔로]덴마크 브리 치즈",
        content: "Chicken Main Course",
        price: "$5.99",
        rating: "5.0",
        reviews: "87",
        url: "#"
      },
      {
        imageSrc:
        "https://img-cf.kurly.com/shop/data/goods/1528161805562l0.jpg",
        title: "[일드프랑스]미니 브리",
        content: "Fried Mexican Beef",
        price: "$3.99",
        rating: "4.5",
        reviews: "34",
        url: "#"
      },
      {
        imageSrc:
        "https://img-cf.kurly.com/shop/data/goods/1566383011754l0.jpg",
        title: "[카스텔로]카스텔로",
        content: "Chilli Crispy Nachos",
        price: "$3.99",
        rating: "3.9",    
        reviews: "26",
        url: "#"
      },
      {
        imageSrc:
        "https://img-cf.kurly.com/shop/data/goods/1595490964205l0.jpg",
        title: "[샴피뇽]캄보졸라 치즈",
        content: "Mexican Chilli",
        price: "$3.99",
        rating: "4.2",
        reviews: "95",
        url: "#"
      },
      {
        imageSrc:
        "https://img-cf.kurly.com/shop/data/goods/155591204450l0.jpg",
        title: "[프레지덩]쁘띠 브리",
        content: "Deepfried Chicken",
        price: "$2.99",
        rating: "5.0",
        reviews: "61",
        url: "#"
      },
      {
        imageSrc:
        "https://img-cf.kurly.com/shop/data/goods/1493028272308l0.jpg",
        title: "[프레지덩]쁘띠 까망베르",
        content: "Hamburger & Fries",
        price: "$7.99",
        rating: "4.9",
        reviews: "89",
        url: "#"
      },
      {
        imageSrc:
        "https://img-cf.kurly.com/shop/data/goods/1575338281586l0.jpg",
        title: "[벨레트왈]투르 드 파리 브리",
        content: "Crispy Soyabeans",
        price: "$8.99",
        rating: "4.6",
        reviews: "12",
        url: "#"
      },
      {
        imageSrc:
        "https://img-cf.kurly.com/shop/data/goods/1477568051626l0.jpg",
        title: "[엘파스토르]고트 치즈",
        content: "Roasted Chicken & Egg",
        price: "$7.99",
        rating: "4.2",
        reviews: "19",
        url: "#"
      }
    ],
    세미하드치즈: [
      {
        imageSrc:
          "https://img-cf.kurly.com/shop/data/goodsview/20170222/gv40000000201_1.jpg",
        title: "에멘탈 슬라이스",
        content: "Tomato Salad & Carrot",
        price: "$5.99",
        rating: "5.0",
        reviews: "87",
        url: "#"
      },
      {
        imageSrc:
          "https://img-cf.kurly.com/shop/data/goods/1564729594540l0.jpg",
        title: "미국 전통 치즈 5종",
        content: "Cheese Pizza",
        price: "$2.99",
        rating: "4.8",
        reviews: "32",
        url: "#"
      },
      {
        imageSrc:
        "https://img-cf.kurly.com/shop/data/goods/151073128727l0.jpg",
        title: "고르곤졸라 피칸테",
        content: "Hamburger & Fries",
        price: "$7.99",
        rating: "4.9",
        reviews: "89",
        url: "#"
      },
      {
        imageSrc:
        "https://img-cf.kurly.com/shop/data/goods/big/201508/418_shop1_988985.jpg",
        title: "1833 체다 치즈",
        content: "Crispy Soyabeans",
        price: "$8.99",
        rating: "4.6",
        reviews: "12",
        url: "#"
      },
      {
        imageSrc:
        "https://img-cf.kurly.com/shop/data/goods/1579165836964l0.jpg",
        title: "110년 전통 고다치즈 3종",
        content: "Roasted Chicken & Egg",
        price: "$7.99",
        rating: "4.2",
        reviews: "19",
        url: "#"
      },
      {
        imageSrc:
        "https://img-cf.kurly.com/shop/data/goods/158492969355l0.jpg",
        title: "뉴질랜드 체다 치즈 3종",
        content: "Deepfried Chicken",
        price: "$2.99",
        rating: "5.0",
        reviews: "61",
        url: "#"
      },
      {
        imageSrc:
        "https://img-cf.kurly.com/shop/data/goods/1552974896497l0.jpg",
        title: "만체고 치즈 3개월",
        content: "Mexican Chilli",
        price: "$3.99",
        rating: "4.2",
        reviews: "95",
        url: "#"
      },
      {
        imageSrc:
        "https://img-cf.kurly.com/shop/data/goods/145371157091l0.jpg",
        title: "고다치즈 2종",
        content: "Chilli Crispy Nachos",
        price: "$3.99",
        rating: "3.9",
        reviews: "26",
        url: "#"
      },
    ],
    하드치즈: [
      {
        imageSrc:
          "https://img-cf.kurly.com/shop/data/goods/1511158446609l0.jpg",
        title: "[앙트르몽]에멘탈 치즈",
        content: "Tomato Salad & Carrot",
        price: "$5.99",
        rating: "5.0",
        reviews: "87",
        url: "#"
      },
      {
        imageSrc:
          "https://img-cf.kurly.com/shop/data/goods/1584929308198l0.jpg",
        title: "[만토바]파르미지아노 레지아노",
        content: "Cheese Pizza",
        price: "$2.99",
        rating: "4.8",
        reviews: "32",
        url: "#"
      },
      {
        imageSrc:
        "https://img-cf.kurly.com/shop/data/goods/1566382697740l0.jpg",
        title: "[파르네세]파르미지아노 레지아노",
        content: "Hamburger & Fries",
        price: "$7.99",
        rating: "4.9",
        reviews: "89",
        url: "#"
      },
      {
        imageSrc:
        "https://img-cf.kurly.com/shop/data/goods/1587965094771l0.jpg",
        title: "바이에른탈러 에멘탈 치즈",
        content: "Crispy Soyabeans",
        price: "$8.99",
        rating: "4.6",
        reviews: "12",
        url: "#"
      },
      {
        imageSrc:
        "https://img-cf.kurly.com/shop/data/goods/1597383414438l0.jpg",
        title: "파르미지아노 레지아노 18개월",
        content: "Roasted Chicken & Egg",
        price: "$7.99",
        rating: "4.2",
        reviews: "19",
        url: "#"
      },
      {
        imageSrc:
        "https://img-cf.kurly.com/shop/data/goods/155894449850l0.jpg",
        title: "유기농 파르마지아노 레지아노",
        content: "Deepfried Chicken",
        price: "$2.99",
        rating: "5.0",
        reviews: "61",
        url: "#"
      },
      {
        imageSrc:
        "https://img-cf.kurly.com/shop/data/goods/1597801807938l0.jpg",
        title: "만체고 치즈 12개월",
        content: "Mexican Chilli",
        price: "$3.99",
        rating: "4.2",
        reviews: "95",
        url: "#"
      },
      {
        imageSrc:
        "https://img-cf.kurly.com/shop/data/goods/1563949642720l0.jpg",
        title: "헤리티지 체다",
        content: "Chilli Crispy Nachos",
        price: "$3.99",
        rating: "3.9",
        reviews: "26",
        url: "#"
      },
    ],    
    // 소프트치즈: soft(),
    // 세미하드치즈: getRandomCards(),
    // 하드치즈: getRandomCards()
  }
}) {
  /*
   * To customize the tabs, pass in data using the `tabs` prop. It should be an object which contains the name of the tab
   * as the key and value of the key will be its content (as an array of objects).
   * To see what attributes are configurable of each object inside this array see the example above for "Starters".
   */
  const tabsKeys = Object.keys(tabs);
  const [activeTab, setActiveTab] = useState(tabsKeys[0]);


  return (
    <Container>
      <ContentWithPaddingXl>
        <HeaderRow>
          <Header>{heading}</Header>
          <TabsControl>
            {Object.keys(tabs).map((tabName, index) => (
              <TabControl key={index} active={activeTab === tabName} onClick={() => setActiveTab(tabName)}>
                {tabName}
              </TabControl>
            ))}
          </TabsControl>
        </HeaderRow>

        {tabsKeys.map((tabKey, index) => (
          <TabContent
            key={index}
            variants={{
              current: {
                opacity: 1,
                scale:1,
                display: "flex",
              },
              hidden: {
                opacity: 0,
                scale:0.8,
                display: "none",
              }
            }}
            transition={{ duration: 0.4 }}
            initial={activeTab === tabKey ? "current" : "hidden"}
            animate={activeTab === tabKey ? "current" : "hidden"}
          >
            {tabs[tabKey].map((card, index) => (
              <CardContainer key={index}>
                <Card className="group" href={card.url} initial="rest" whileHover="hover" animate="rest">
                  <CardImageContainer imageSrc={card.imageSrc}>
                    <CardRatingContainer>
                      <CardRating>
                        <StarIcon />
                        {card.rating}
                      </CardRating>
                      <CardReview>({card.reviews})</CardReview>
                    </CardRatingContainer>
                    <CardHoverOverlay
                      variants={{
                        hover: {
                          opacity: 1,
                          height: "auto"
                        },
                        rest: {
                          opacity: 0,
                          height: 0
                        }
                      }}
                      transition={{ duration: 0.3 }}
                    >
                      <CardButton onClick={function() {alert('장바구니에 담겼습니다.')}}>Buy Now</CardButton>
                    </CardHoverOverlay>
                  </CardImageContainer>
                  <CardText>
                    <CardTitle>{card.title}</CardTitle>
                    <CardContent>{card.content}</CardContent>
                    <CardPrice>{card.price}</CardPrice>
                  </CardText>
                </Card>
              </CardContainer>
            ))}
          </TabContent>
        ))}
      </ContentWithPaddingXl>
      <DecoratorBlob1 />
      <DecoratorBlob2 />
    </Container>
  );
};

/* This function is only there for demo purposes. It populates placeholder cards */
// const soft = () => {
//   const cards = [
//     {
//       imageSrc:
//       "https://img-cf.kurly.com/shop/data/goods/1566382934703l0.jpg",
//       title: "Chicken Chilled",
//       content: "Chicken Main Course",
//       price: "$5.99",
//       rating: "5.0",
//       reviews: "87",
//       url: "#"
//     },
//     {
//       imageSrc:
//       "https://img-cf.kurly.com/shop/data/goods/1528161805562l0.jpg",
//       title: "Samsa Beef",
//       content: "Fried Mexican Beef",
//       price: "$3.99",
//       rating: "4.5",
//       reviews: "34",
//       url: "#"
//     },
//     {
//       imageSrc:
//       "https://img-cf.kurly.com/shop/data/goods/1566383011754l0.jpg",
//       title: "Carnet Nachos",
//       content: "Chilli Crispy Nachos",
//       price: "$3.99",
//       rating: "3.9",
//       reviews: "26",
//       url: "#"
//     },
//     {
//       imageSrc:
//       "https://img-cf.kurly.com/shop/data/goods/1595490964205l0.jpg",
//       title: "Guacamole Mex",
//       content: "Mexican Chilli",
//       price: "$3.99",
//       rating: "4.2",
//       reviews: "95",
//       url: "#"
//     },
//     {
//       imageSrc:
//       "https://img-cf.kurly.com/shop/data/goods/155591204450l0.jpg",
//       title: "Chillie Cake",
//       content: "Deepfried Chicken",
//       price: "$2.99",
//       rating: "5.0",
//       reviews: "61",
//       url: "#"
//     },
//     {
//       imageSrc:
//       "https://img-cf.kurly.com/shop/data/goods/1493028272308l0.jpg",
//       title: "Nelli",
//       content: "Hamburger & Fries",
//       price: "$7.99",
//       rating: "4.9",
//       reviews: "89",
//       url: "#"
//     },
//     {
//       imageSrc:
//       "https://img-cf.kurly.com/shop/data/goods/1575338281586l0.jpg",
//       title: "Jalapeno Poppers",
//       content: "Crispy Soyabeans",
//       price: "$8.99",
//       rating: "4.6",
//       reviews: "12",
//       url: "#"
//     },
//     {
//       imageSrc:
//       "https://img-cf.kurly.com/shop/data/goods/1477568051626l0.jpg",
//       title: "Cajun Chicken",
//       content: "Roasted Chicken & Egg",
//       price: "$7.99",
//       rating: "4.2",
//       reviews: "19",
//       url: "#"
//     }
//   ];
  

//   // Shuffle array
//   return cards.sort(() => Math.random() - 0.5);
// };
