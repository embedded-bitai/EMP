import React, {useState} from "react";
import { userActions } from '../../../modules/usr/user/user.action'
import { useDispatch } from "react-redux"

import Select from 'react-select' //eslint-disable-line
import { Container as ContainerBase } from "../../../components/cmm/Layouts";
import tw from "twin.macro"; 
import styled from "styled-components";
import { css } from "styled-components/macro"; //eslint-disable-line
import cheeseRegister from "../../../components/cmm/images/cheese/cheeseImg2.png";


import { ReactComponent as SignUpIcon } from "feather-icons/dist/icons/user-plus.svg";
import {FormControl,FormLabel, RadioGroup, Radio, Card } from '@material-ui/core' //eslint-disable-line
import FormControlLabel from '@material-ui/core/FormControlLabel';




const Container = tw(ContainerBase)`min-h-screen bg-yellow-500 text-white font-medium flex justify-center`;
const Content = tw.div`max-w-screen-xl m-0 sm:mx-20 sm:my-16 bg-white text-gray-900 shadow sm:rounded-lg flex justify-center flex-1`;
const MainContainer = tw.div`lg:w-1/2 xl:w-5/12 p-6 sm:p-12`;
const MainContent = tw.div`mt-12 flex flex-col items-center`;
const Heading = tw.h1`text-2xl xl:text-3xl font-extrabold`;
const FormContainer = tw.div`w-full flex-1`;

const DividerTextContainer = tw.div`my-10 border-b text-center relative`;
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
const IllustrationContainer = tw.div`sm:rounded-r-lg flex-1 bg-purple-100 text-center hidden lg:flex justify-center`;
const IllustrationImage = styled.div`
  ${props => `background-image: url("${props.imageSrc}");`}
  ${tw`m-12 xl:m-16 w-full max-w-lg bg-contain bg-center bg-no-repeat`}
`;

const cheeseRegisterImageSrc = cheeseRegister,
      headingText = "Sign Up For Pic 2 Cheese",
      submitButtonText = "Sign Up",
      SubmitButtonIcon = SignUpIcon,
      tosUrl = "#",
      privacyPolicyUrl = "#"

export default function SignUp () {
  const [user, setUser] = useState({
    user_id: '',
    password: '',
    name: '',
    gender: '',
    age: '',
    phone: '',
    email: ''
  });
  
  // const options = [
  //   { value: '10', label: '10대' },
  //   { value: '20', label: '20대' },
  //   { value: '30', label: '30대' },
  //   { value: '40', label: '40대' },
  //   { value: '50', label: '50대' },
  //   { value: '60', label: '60대' },
  //   { value: '70', label: '70대' },
  //   { value: '80', label: '80대' }
  // ]

  const [submitted, setSubmitted] = useState(false);
  // const registering = useSelector(state => state.registering.registering);
  const dispatch = useDispatch();

  // reset login status
  /*
  useEffect(() => {
      dispatch(userActions.logout());
  }, [])
  */

  function handleChange(e) {
    const { name, value } = e.target;
    setUser(user => ({...user, [name]: value}));
  }

  function handleSubmit(e) {
    e.preventDefault();

    setSubmitted(true);
    if (user.user_id && user.password && user.name && user.gender && user.age && user.phone && user.email) {
      dispatch(userActions.register(user));
    }
}


  return (
  <div>
    {/* <Header/> */}
    {/* <AnimationRevealPage> */}
      <Container>
        <Content>
          <MainContainer>
            <MainContent>
              <Heading>{headingText}</Heading>
              <FormContainer>
                <DividerTextContainer>
                  <DividerText>Sign up with your Information</DividerText>
                </DividerTextContainer>
                <Form name="form" onSubmit={handleSubmit}>
                  {/* <Input type="email" placeholder="Email" />  */}
                  <Input type="text" placeholder="Id" name= "user_id" value={user.user_id} onChange={handleChange}
                  className={'form-control' + (submitted && !user.user_id ? 'is-invalid' : '')}/>
                  {submitted && !user.user_id &&
                      <div className="invalied-feedback">User Id is required</div>}

                  <Input type="password" placeholder="Password" name="password" value={user.password} onChange={handleChange}
                  className={'form-control' + (submitted && !user.password ? ' is-invalid' : '')} />
                  {submitted && !user.password &&
                      <div className="invalid-feedback">Password is required</div>
                  }

                  <Input type="text" placeholder="Your name" name="name" value={user.name} onChange={handleChange} 
                  className={'form-control' + (submitted && !user.name ? 'is-invalid' : '')}/>
                  {submitted && !user.name &&
                      <div className="invalid-feedback">User Name is required</div>
                  }
     
                  <RadioGroup defaultValue="female" aria-label="gender" name="gender" value={user.gender} onChange={handleChange}>
                    <FormControlLabel value="F" control={<Radio />} label="Female" />
                    <FormControlLabel value="M" control={<Radio />} label="Male" />
                  </RadioGroup>

                  {/* <Select options={options} placeholder="Age" name="age" value={user.age} onChange={handleChange} /> */}

                  <Input type="text" placeholder="Age" name="age" value={user.age} onChange={handleChange}
                  className={'form-control' + (submitted && !user.name ? 'is-invalid' : '')}/>
                  {submitted && !user.name &&
                      <div className="invalid-feedback">User Name is required</div>
                  }


                  <Input type="text" placeholder="Tel" name="phone" value={user.phone} onChange={handleChange} 
                  size="small"
                  control={<Radio color="yellow" />}
                  className={'form-control' + (submitted && !user.phone ? 'is-invalid' : '')}/>
                  {submitted && !user.phone &&
                    <div className="invalid-feedback">Tel is required</div>
                  }           

                  <Input type="email" placeholder="Email" name="email" value={user.email} onChange={handleChange} 
                  className= {'form-control' + (submitted && !user.email ? 'is-invalid' : '')}/>
                  {submitted && !user.email &&  
                    <div className="invalid-feedback">Email is required</div>
                  }  

                  <SubmitButton type="submit" onClick={userActions.register}>
                    <SubmitButtonIcon className="icon" />
                    <span className="text" >{submitButtonText}</span>
                  </SubmitButton>


                  <p tw="mt-6 text-xs text-gray-600 text-center">
                    I agree to abide by treact's{" "}
                    <a href={tosUrl} tw="border-b border-gray-500 border-dotted">
                      Terms of Service
                    </a>{" "}
                    and its{" "}
                    <a href={privacyPolicyUrl} tw="border-b border-gray-500 border-dotted">
                      Privacy Policy
                    </a>
                  </p>

                  <p tw="mt-8 text-sm text-gray-600 text-center">
                    Already have an account?{" "}
                    <a href="/login" tw="border-b border-gray-500 border-dotted">
                        Sign In
                      </a>
                  </p>
                </Form>
              </FormContainer>
            </MainContent>
          </MainContainer>
          <IllustrationContainer>
            <IllustrationImage imageSrc={cheeseRegisterImageSrc} />
          </IllustrationContainer>
        </Content>
      </Container>
    {/* </AnimationRevealPage> */}
  </div>
  );
}
