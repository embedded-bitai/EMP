import React, { useState } from "react";
import { context as c } from '../../../modules/context'
import axios from 'axios'
import {useHistory } from "react-router-dom"

import { Container as ContainerBase } from "../../../components/cmm/Layouts";
import tw from "twin.macro";

import {css} from "styled-components/macro"; //eslint-disable-line
import styled from "styled-components";
import cheeseLogin from "../../../components/cmm/images/cheese/cheeseImg2.png";
// import logo from "../images/logo.svg";
import { ReactComponent as LoginIcon } from "feather-icons/dist/icons/log-in.svg";



const Container = tw(ContainerBase)`min-h-screen bg-yellow-500 text-white font-medium flex justify-center`;
const Content = tw.div`max-w-screen-xl m-0 sm:mx-20 sm:my-16 bg-white text-gray-900 shadow sm:rounded-lg flex justify-center flex-1`;
const MainContainer = tw.div`lg:w-1/2 xl:w-5/12 p-6 sm:p-12`;
const MainContent = tw.div`mt-12 flex flex-col items-center`;
const Heading = tw.h1`text-2xl xl:text-3xl font-extrabold`;
const FormContainer = tw.div`w-full flex-1 mt-8`;


const DividerTextContainer = tw.div`my-12 border-b text-center relative`;
const DividerText = tw.div`leading-none px-2 inline-block text-sm text-gray-600 tracking-wide font-medium bg-white transform -translate-y-1/2 absolute inset-x-0 top-1/2 bg-transparent`;

const Form = tw.form`mx-auto max-w-xs`;
const Input = tw.input`w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5 first:mt-0`;
const SubmitButton = styled.button`
  ${tw`mt-5 tracking-wide font-semibold bg-yellow-500 text-black w-full py-4 rounded-lg hover:bg-yellow-900 transition-all duration-300 ease-in-out flex items-center justify-center focus:shadow-outline focus:outline-none`}
  .icon {
    ${tw`w-6 h-6 -ml-2`}
  }
  .text {
    ${tw`ml-3`}
  }
`;
const CheeseLoginContainer = tw.div`sm:rounded-r-lg flex-1 bg-purple-100 text-center hidden lg:flex justify-center`;
const CheeseLoginImage = styled.div`
  ${props => `background-image: url("${props.imageSrc}");`}
  ${tw`m-12 xl:m-16 w-full max-w-sm bg-contain bg-center bg-no-repeat`}
`;

const cheeseLoginImageSrc  = cheeseLogin,
      headingText = "Sign In for Pic 2 Cheese",  
      submitButtonText = "Sign In",
      SubmitButtonIcon = LoginIcon,
      forgotPasswordUrl = "#"

export default function Login (
) {
  const [user_id, setUserId] = useState('')
  const [password, setPassword] = useState('')
  // const dispatch = useDispatch()

  const history = useHistory()
  const login = e => {
    // 유저 로그인 한다
    e.preventDefault()
    axios.post(`${c.url}/api/login`, {"user_id":user_id, "password":password})
        .then(user => {
            // alert(`Welcome ! ${res.data["fname"]}.  ${res.data["usr_id"]}'s connection is successful. ! `)

            sessionStorage.setItem("sessionUser", user.data['user_id'])
            
            // history.push("/user-detail")
            history.push("/user-info")
            window.location.reload()

        })
        .catch(error => {
            alert("아이디 또는 비밀번호를 다시 확인해주세요.")
            window.location.reload()
        })
  }
    return (
      <div>
        {/* <Header /> */}
        {/* <AnimationRevealPage> */}
          <Container>
            <Content>
              <MainContainer>
                {/* <LogoLink href={logoLinkUrl}>
                  <LogoImage src={logo} />
                </LogoLink> */}
                <MainContent>
                  <Heading>{headingText}</Heading>
                  <FormContainer>
                    <DividerTextContainer>
                      <DividerText>Sign in with your Id</DividerText>
                    </DividerTextContainer>
                    <Form>
                      {/* <Input type="email" placeholder="Email" /> */}
                      <Input type="text" placeholder="ID" onChange={e => setUserId(`${e.target.value}`)}/>
                      <Input type="password" placeholder="Password"  onChange={e => setPassword(`${e.target.value}`)}/>
                      
                      {/* <SubmitButton type="submit" onClick= {
                        e => dispatch(userActions.login(user_id,password))
                        }>
                        <SubmitButtonIcon className="icon" />
                        <span className="text">{submitButtonText}</span>
                      </SubmitButton> */}

                      <SubmitButton type="submit" onClick= {login}>
                        <SubmitButtonIcon className="icon" />
                        <span className="text">{submitButtonText}</span>
                      </SubmitButton>
                    
                    </Form>
                    <p tw="mt-6 text-xs text-gray-600 text-center">
                      <a href={forgotPasswordUrl} tw="border-b border-gray-500 border-dotted">
                        Forgot Password ?
                      </a>
                    </p>
                    <p tw="mt-8 text-sm text-gray-600 text-center">
                      Dont have an account?{" "}
                      <a href="/signup" tw="border-b border-gray-500 border-dotted">
                        Sign Up
                      </a>
                    </p>
                  </FormContainer>
                </MainContent>
              </MainContainer>
              <CheeseLoginContainer>
                <CheeseLoginImage imageSrc={cheeseLoginImageSrc} />
              </CheeseLoginContainer>
            </Content>
          </Container>
        {/* </AnimationRevealPage> */}
      </div>
    );
  }