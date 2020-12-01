import React from "react";
import { motion } from "framer-motion";
import tw from "twin.macro";
import styled from "styled-components";
import { css } from "styled-components/macro"; //eslint-disable-line
import {useHistory} from 'react-router-dom'
// import { CartContext } from '../../containers/cop/cart/contexts/CartContext';
import { history } from '../../modules/history' //eslint-disable-line

import useAnimatedNavToggler from "./AnimatedNavToggler";

import logo from "./images/cheese/cheese_img.png";
import { ReactComponent as MenuIcon } from "feather-icons/dist/icons/menu.svg";
import { ReactComponent as CloseIcon } from "feather-icons/dist/icons/x.svg";
import {CartIcon} from '../../containers/cop/cart/Icons' //eslint-disable-line

// // import Button from '@material-ui/core/Button';
// import ClickAwayListener from '@material-ui/core/ClickAwayListener';
// import Grow from '@material-ui/core/Grow';
// import Paper from '@material-ui/core/Paper';
// import Popper from '@material-ui/core/Popper';
// // import MenuItem from '@material-ui/core/MenuItem';
// import MenuList from '@material-ui/core/MenuList';

import Tooltip from '@material-ui/core/Tooltip'

import { FaRegUser } from "react-icons/fa"  //eslint-disable-line


// const useStyles = makeStyles((theme) => ({
//   root: {
//     display: 'flex',
//   },
//   paper: {
//     marginRight: theme.spacing(2),
//   },
// }));



const HeaderBlock = tw.header`
  flex justify-between items-center
  max-w-screen-xl mx-auto pt-3 pb-3
`;

const NavLinks = tw.div`inline-block -mx-8`;

const NavLink = tw.a`
  text-lg my-2 lg:text-sm lg:mx-6 lg:my-0
  font-semibold tracking-wide transition duration-300 
  pb-1 border-b-2 border-transparent hover:border-yellow-500 hocus:text-yellow-500
`;

const PrimaryLink = tw(NavLink)`
  lg:mx-0
  px-8 py-3 rounded bg-yellow-500 text-black
  hocus:bg-yellow-700 hocus:text-gray-200 focus:shadow-outline
  border-b-0
`;

const LogoLink = styled(NavLink)`
  ${tw`flex items-center font-black border-b-0 text-2xl! ml-0!`};

  img {
    ${tw`w-10 mr-3`}
  }
`;


const MobileNavLinksContainer = tw.nav`flex flex-1 items-center justify-between`;
const NavToggle = tw.button`
  lg:hidden z-20 focus:outline-none hocus:text-yellow-500 transition duration-300
`;
const MobileNavLinks = motion.custom(styled.div`
  ${tw`lg:hidden z-10 fixed top-0 inset-x-0 mx-4 my-6 p-8 border text-center rounded-lg text-gray-900 bg-white`}
  ${NavLinks} {
    ${tw`flex flex-col items-center`}
  }
`);

const DesktopNavLinks = tw.nav`
  hidden lg:flex flex-1 justify-between items-center
`;

// const selectedStyle = {
//   backgroundColor: "white", color: "yellow"
// }


const Header = (props, { roundedHeaderButton = false, logoLink, links, className, collapseBreakpointClass = "lg" }) => {
  
  const history = useHistory()
  
  const logout = e => {
    alert('다음 치즈도 pic 2 cheese와 함께~')
    e.preventDefault()
    sessionStorage.removeItem("sessionUser")
    history.push('/')
    window.location.reload()
  }

  // const classes = useStyles();
  const [open, setOpen] = React.useState(false);
  const anchorRef = React.useRef(null);

  // const handleToggle = () => {
  //   setOpen((prevOpen) => !prevOpen);
  // };

  // const handleClose = (event) => {
  //   if (anchorRef.current && anchorRef.current.contains(event.target)) {
  //     return;
  //   }

  //   setOpen(false);
  // };

  // function handleListKeyDown(event) {
  //   if (event.key === 'Tab') {
  //     event.preventDefault();
  //     setOpen(false);
  //   }
  // }

  // return focus to the button when we transitioned from !open -> open
  const prevOpen = React.useRef(open);
  React.useEffect(() => {
    if (prevOpen.current === true && open === false) {
      anchorRef.current.focus();
    }

    prevOpen.current = open;
  }, [open]);

  const defaultLinks = (
    <NavLinks key={1}>
      { props.isAuth !== null
      ? <ul>
        <NavLink href="/" >홈</NavLink>
        <NavLink href="/cheese">치즈</NavLink>
        <NavLink href="/review">Review</NavLink>
        <NavLink href="/recommend">추천</NavLink>
        {/* <NavLink href="/cart"><CartIcon/>Cart ({itemCount})</NavLink> */}
        {/* <NavLink href="/cart">Cart</NavLink> */}
        <NavLink href="/user-info" tw="lg:ml-20!">My Page</NavLink>
        {/* <NavLink ref={anchorRef} aria-controls={open ? 'menu-list-grow' : undefined} aria-haspopup="true" onClick={handleToggle} tw="lg:ml-20!">My Page
          <Popper open={open} anchorEl={anchorRef.current} role={undefined} transition disablePortal>
            {({ TransitionProps, placement }) => (
              <Grow
                {...TransitionProps}
                style={{ transformOrigin: placement === 'bottom' ? 'center top' : 'center top' }}
              >
                <Paper>
                  <ClickAwayListener onClickAway={handleClose}>
                    <MenuList autoFocusItem={open} id="menu-list-grow" onKeyDown={handleListKeyDown}>
                      <NavLink href="/user-detail" onClick={handleClose}>나의 정보</NavLink><br/><br/>
                      <NavLink href="/user-profile" onClick={handleClose} >나의 프로필</NavLink><br/><br/>
                      <NavLink href="/cart" onClick={handleClose}>장바구니</NavLink>
                    </MenuList>
                  </ClickAwayListener>
                </Paper>
              </Grow>
            )}
          </Popper>
        </NavLink> */}
        <NavLink onClick={logout} tw="lg:ml-4!" style={{textDecoration: 'underline'}}>Logout</NavLink>
      </ul>:

      <ul>
        {/* <NavLink href="/" >홈</NavLink>
        <NavLink href="/cheese">치즈</NavLink>
        <NavLink href="/review">Review</NavLink>
        <NavLink href="/survey">추천</NavLink>
        <NavLink href="/cart" onClick={handleClose}>장바구니</NavLink>
        <NavLink href="/login" tw="lg:ml-20!">Sign in</NavLink>
        <PrimaryLink css={roundedHeaderButton && tw`rounded-full`}href="/signup">Sign Up</PrimaryLink> */}
        <Tooltip title="우리 사이트 소개 & 치즈 소개">
        <NavLink href="/" >홈</NavLink>
        </Tooltip>
        <Tooltip title="치즈 상품 리스트 & 장바구니와 연결">
        <NavLink href="/cheese">치즈</NavLink>
        </Tooltip>
        <Tooltip title="구매 고객 리뷰 리스트 CRUD">
        <NavLink href="/review">Review</NavLink>
        </Tooltip>
        <Tooltip title="챗봇을 통해 추천 받은 치즈 카테고리와 함께 치즈 상품 2~3개 추천 리스트 보여주는 기능(모델링 적용)">
          <NavLink href="/recommend">추천</NavLink>
        </Tooltip>
        {/* <Tooltip title="구독 상품과 치즈 상품을 구매할 수 있는 장바구니 기능">
          <NavLink href="/cart" onClick={handleClose}>장바구니</NavLink>
        </Tooltip> */}
        <Tooltip title="로그인 기능">
        <NavLink href="/login" tw="lg:ml-20!">Sign in</NavLink>
        </Tooltip>
        <Tooltip title="회원가입 기능">
        <PrimaryLink css={roundedHeaderButton && tw`rounded-full`}href="/signup">Sign Up</PrimaryLink>
        </Tooltip>
      </ul>
      }
    </NavLinks>
  )

  const { showNavLinks, animation, toggleNavbar } = useAnimatedNavToggler();
  const collapseBreakpointCss = collapseBreakPointCssMap[collapseBreakpointClass];

  const defaultLogoLink = (
    <LogoLink href="/">
      <img src={logo} alt="logo" />
      Pic 2 Cheese
    </LogoLink>
  );

  logoLink = logoLink || defaultLogoLink;
  links = links || defaultLinks;
  
  // const {itemCount} = useContext(CartContext)



  return (<>
    <HeaderBlock className={className || "header-light"}>
      <DesktopNavLinks css={collapseBreakpointCss.desktopNavLinks}>
        {logoLink}
        {links}
      </DesktopNavLinks>

      <MobileNavLinksContainer css={collapseBreakpointCss.mobileNavLinksContainer}>
        {logoLink}
        <MobileNavLinks initial={{ x: "150%", display: "none" }} animate={animation} css={collapseBreakpointCss.mobileNavLinks}>
          {links}
        </MobileNavLinks>
        <NavToggle onClick={toggleNavbar} className={showNavLinks ? "open" : "closed"}>
          {showNavLinks ? <CloseIcon tw="w-6 h-6" /> : <MenuIcon tw="w-6 h-6" />}
        </NavToggle>
      </MobileNavLinksContainer>
    </HeaderBlock>
  </>);
};

export default Header

const collapseBreakPointCssMap = {
  sm: {
    mobileNavLinks: tw`sm:hidden`,
    desktopNavLinks: tw`sm:flex`,
    mobileNavLinksContainer: tw`sm:hidden`
  },
  md: {
    mobileNavLinks: tw`md:hidden`,
    desktopNavLinks: tw`md:flex`,
    mobileNavLinksContainer: tw`md:hidden`
  },
  lg: {
    mobileNavLinks: tw`lg:hidden`,
    desktopNavLinks: tw`lg:flex`,
    mobileNavLinksContainer: tw`lg:hidden`
  },
  xl: {
    mobileNavLinks: tw`lg:hidden`,
    desktopNavLinks: tw`lg:flex`,
    mobileNavLinksContainer: tw`lg:hidden`
  }
};