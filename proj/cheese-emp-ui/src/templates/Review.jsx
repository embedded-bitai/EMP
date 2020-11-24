import React, { Component } from 'react';
import tw from "twin.macro"; //eslint-disable-line
import axios from 'axios'
import Customer from '../containers/cop//rev/review/Customer'
import '../App.css';
// import styled from "../components/common/node_modules/styled-components";
// import { css } from "../components/common/node_modules/styled-components/macro"; //eslint-disable-line
import styled from "styled-components";
import { css } from "styled-components/macro"; //eslint-disable-line

import Paper from '@material-ui/core/Paper';
import Table from '@material-ui/core/Table';
import TableHead from '@material-ui/core/TableHead';
import TableBody from '@material-ui/core/TableBody';
import TableRow from '@material-ui/core/TableRow';
import TableCell from '@material-ui/core/TableCell';
import { withStyles } from '@material-ui/core/styles';

<<<<<<< HEAD:proj/cheese-emp-ui/src/templates/Review.jsx
import Header from "../components/cmm/Header.js";
import Footer from "../components/cmm/Footer.js";
=======
import Header from "../home/common/Header.js";
import Footer from "../home/common/Footer.js";

>>>>>>> upstream/master:proj/cheese-emp-ui/src/board/BoardPage.js
export const NavLink = tw.a`
  text-lg my-2 lg:text-sm lg:mx-6 lg:my-0
  font-semibold tracking-wide transition duration-300
  pb-1 border-b-2 border-transparent hover:border-yellow-500 hocus:text-yellow-500
`;

export const PrimaryLink = tw(NavLink)`
  lg:mx-0
  px-8 py-3 rounded bg-yellow-500 text-black
  hocus:bg-yellow-700 hocus:text-gray-200 focus:shadow-outline
  border-b-0
`;


const Container = styled.div`
  ${tw`relative -mx-3 px-10 bg-center bg-cover h-screen min-h-144 pt-10 `}`;

const styles = theme => ({
    root: {
        width: "100%",
        marginTop: theme.spacing.unit * 3,
        overflowX: "auto",
    },
    table: {
        minWidth: 500
    }
});

const customers = [
    {
        'id': 1,
        'image': 'https://placeimg.com/48/48/1',
        'name': '홍길동',
        'birthday': '961222',
        'gender': '남자',
        'job': '대학생'
    },
    {
        'id': 2,
        'image': 'https://placeimg.com/48/48/2',
        'name': '나동빈',
        'birthday': '960508',
        'gender': '남자',
        'job': '프로그래머'
    },
    {
        'id': 3,
        'image': 'https://placeimg.com/48/48/3',
        'name': '이순신',
        'birthday': '961127',
        'gender': '남자',
        'job': '디자이너'
    }
]

class BoardPage extends Component {
    render() {
    const { classes } = this.props;

    const fnqAxios = () => {
        axios.get(`http://localhost:8080/api/fnq`)
            .then(res => {
                alert(`Fnq Connection Success !!`)
            }).catch(
                e => alert(`Fnq Failure`)
            )
    }   

    return (<>
        <Header />
        <Container>
            {/* <button onClick={fnqAxios}>Fnq axios(검색어 입력창)</button> */}

            <PrimaryLink  margin="10em" href="/boardregister">검색</PrimaryLink>
            <PrimaryLink  margin="10em" href="/boardregister">게시글 작성</PrimaryLink>
            <Paper className={classes.root}>
                <Table className={classes.table}>
                    <TableHead>
                        <TableRow>
                            <TableCell>번호</TableCell>
                            <TableCell>이미지</TableCell>
                            <TableCell>이름</TableCell>
                            <TableCell>생년월일</TableCell>
                            <TableCell>성별</TableCell>
                            <TableCell>직업</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                    {customers.map(c => {
                    return <Customer key={c.id} id={c.id} image={c.image} name={c.name} birthday={c.birthday} gender={c.gender} job={c.job} />
                    })}
                    </TableBody>
                </Table>
            </Paper>
        </Container>
        <Footer/>   
    </>);
    }
}

export default withStyles(styles)(BoardPage);