import React, { Component } from 'react';
import tw from "twin.macro"; //eslint-disable-line
import axios from 'axios'
import Customer from './Customer'
import '../App.css';
import Paper from '@material-ui/core/Paper';
import Table from '@material-ui/core/Table';
import TableHead from '@material-ui/core/TableHead';
import TableBody from '@material-ui/core/TableBody';
import TableRow from '@material-ui/core/TableRow';
import TableCell from '@material-ui/core/TableCell';
import { withStyles } from '@material-ui/core/styles';

import Header from "../home/common/Header.js";
import Footer from "../home/common/Footer.js";

// const Header = tw(HeaderBase)`max-w-none`;

const styles = theme => ({
root: {
width: "100%",
marginTop: theme.spacing.unit * 3,
overflowX: "auto"
},
table: {
minWidth: 1080
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

return (
    <div>
        <Header />
        <button onClick={fnqAxios}>Fnq axios</button>
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
        <Footer/>
    </div>
    
    );
    }
}

export default withStyles(styles)(BoardPage);