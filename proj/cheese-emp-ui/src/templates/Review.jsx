import React from 'react';
import tw from "twin.macro"; //eslint-disable-line
import axios from 'axios'
import { useEffect, useState } from 'react';
import { context as c } from '../modules/context'
// import { reviewActions } from '../modules/cop/rev/review/review.action'

import '../App.css';
import styled from "styled-components";
import { css } from "styled-components/macro"; //eslint-disable-line

import PropTypes from 'prop-types';
import Paper from '@material-ui/core/Paper';
import Table from '@material-ui/core/Table';
import TableHead from '@material-ui/core/TableHead';
import TableBody from '@material-ui/core/TableBody';
import TableRow from '@material-ui/core/TableRow';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';

import TableFooter from '@material-ui/core/TableFooter';
import TablePagination from '@material-ui/core/TablePagination';
import IconButton from '@material-ui/core/IconButton';
import FirstPageIcon from '@material-ui/icons/FirstPage';
import KeyboardArrowLeft from '@material-ui/icons/KeyboardArrowLeft';
import KeyboardArrowRight from '@material-ui/icons/KeyboardArrowRight';
import LastPageIcon from '@material-ui/icons/LastPage';
import { makeStyles, useTheme } from '@material-ui/core/styles';

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


const useStyles1 = makeStyles((theme) => ({
  root: {
    flexShrink: 0,
    marginLeft: theme.spacing(2.5),
  },
}));
  

function TablePaginationActions (props) {
  const classes = useStyles1()
  const theme = useTheme()
  const { count, page, rowsPerPage, onChangePage } = props

  const handleFirstPageButtonClick = (event) => {
    onChangePage(event, 0)
  }

  const handleBackButtonClick = (event) => {
    onChangePage(event, page - 1)
  }

  const handleNextButtonClick = (event) => {
    onChangePage(event, page + 1)
  }

  const handleLastPageButtonClick = (event) => {
    onChangePage(event, Math.max(0, Math.ceil(count / rowsPerPage) - 1))
  }

  return (
    <div className={classes.root}>
      <IconButton
        onClick={handleFirstPageButtonClick}
        disabled={page === 0}
        aria-label="first page"
      >
        {theme.direction === 'rtl' ? <LastPageIcon /> : <FirstPageIcon />}
      </IconButton>
      <IconButton onClick={handleBackButtonClick} disabled={page === 0} aria-label="previous page">
        {theme.direction === 'rtl' ? <KeyboardArrowRight /> : <KeyboardArrowLeft />}
      </IconButton>
      <IconButton
        onClick={handleNextButtonClick}
        disabled={page >= Math.ceil(count / rowsPerPage) - 1}
        aria-label="next page"
      >
        {theme.direction === 'rtl' ? <KeyboardArrowLeft /> : <KeyboardArrowRight />}
      </IconButton>
      <IconButton
        onClick={handleLastPageButtonClick}
        disabled={page >= Math.ceil(count / rowsPerPage) - 1}
        aria-label="last page"
      >
        {theme.direction === 'rtl' ? <FirstPageIcon /> : <LastPageIcon />}
      </IconButton>
    </div>
  )
}

TablePaginationActions.propTypes = {
  count: PropTypes.number.isRequired,
  onChangePage: PropTypes.func.isRequired,
  page: PropTypes.number.isRequired,
  rowsPerPage: PropTypes.number.isRequired,
};


const useStyles = makeStyles({
  tableContainer: {
    margin: 0
  },
  table: {
    minWidth: 500
  },
});


export default function Review(){
  const [reviews, setReviews] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [page, setPage] = useState(0)
  const [rowsPerPage, setRowsPerPage] = useState(10)
  // const dispatch = useDispatch()
  const classes = useStyles()

  useEffect(() => {
    const fetchReviews = async () => {
      try {
        
        setReviews(null);
        
        setLoading(true);
        const response = await axios.get(
          `${c.url}/api/reviews`
        );

        setReviews(response.data.reivews);
        console.log(response.data.reivews)
      } catch (e) {
        setError(e);
      }
      setLoading(false);
    };

    fetchReviews();
  }, []);

  if (loading) return <div>..</div>;
  if (error) return <div>error</div>;
  if (!reviews) return null;  


  const emptyRows = rowsPerPage - Math.min(rowsPerPage, reviews.length - page * rowsPerPage)
  const handleChangePage = (event, newPage) => {
    setPage(newPage)
  }
  const handleChangeRowsPerPage = (event) => {
    setRowsPerPage(parseInt(event.target.value, 10))
    setPage(0)
  }

    return (<>
        <Container>
            {/* <button onClick={fnqAxios}>Fnq axios(검색어 입력창)</button> */}
            <PrimaryLink  margin="20em" href="/boardregister">검색</PrimaryLink>
            <PrimaryLink  margin="20em" href="/boardregister">게시글 작성</PrimaryLink>
            {/* <Paper className={classes.root}> */}
            {/* <Table className={classes.table}> */}
            {/* <TableContainer component={Paper} className={classes.tableContainer} > */}
            <TableContainer component={Paper} >
              <Table className={classes.table} aria-label="customized table">
                <TableHead>
                    <TableRow>
                        <TableCell>No</TableCell>
                        <TableCell>제목</TableCell>
                        <TableCell>내용</TableCell>
                    </TableRow>
                </TableHead>
                <TableBody>
                {(rowsPerPage > 0 
                  ? reviews.slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage)
                  : reviews
                  ).map(reviews =>  (
                    <TableRow key={reviews.review_no}>
                        <TableCell>{reviews.review_no}</TableCell>
                        <TableCell>{reviews.review_title}</TableCell>
                        <TableCell>{reviews.review_detail}</TableCell>
                    </TableRow> 
                ))}               
                {emptyRows > 0 && (
                  <TableRow style={{ height: 53 * emptyRows }}>
                    <TableCell colSpan={6}/>
                  </TableRow>
                )}     
                </TableBody>
                <TableFooter>
                  <TableRow>
                    <TablePagination
                      rowPerPageOptions={[10, 20, 30, { label: 'All', value: -1 }]}
                      colSpan={3}
                      count={reviews.length}
                      rowsPerPage={rowsPerPage}
                      page={page}
                      SelectProps={{
                        inputProps: { 'aria-label': 'row per page'},
                        native: true,
                      }}
                      onChangePage={handleChangePage}
                      onChangeRowsPerPage={handleChangeRowsPerPage}
                      ActionsComponent={TablePaginationActions}
                    />
                  </TableRow>
                </TableFooter>
              </Table>
            </TableContainer>
        </Container> 
    </>);
}


///////////////////////////////////////////////////////////////////////////////////////////////////


// import React from 'react';
// import tw from "twin.macro"; //eslint-disable-line
// import axios from 'axios'
// import { useEffect, useState } from 'react';
// import { context as c } from '../modules/context'
// // import { reviewActions } from '../modules/cop/rev/review/review.action'

// import '../App.css';
// import styled from "styled-components";
// import { css } from "styled-components/macro"; //eslint-disable-line

// import PropTypes from 'prop-types';
// import Paper from '@material-ui/core/Paper';
// import Table from '@material-ui/core/Table';
// import TableHead from '@material-ui/core/TableHead';
// import TableBody from '@material-ui/core/TableBody';
// import TableRow from '@material-ui/core/TableRow';
// import TableCell from '@material-ui/core/TableCell';
// import TableContainer from '@material-ui/core/TableContainer';

// import TableFooter from '@material-ui/core/TableFooter';
// // import TablePagination from '@material-ui/core/TablePagination';
// import Pagination from '@material-ui/lab/Pagination'
// import PaginationItem from '@material-ui/lab/Pagination'
// import IconButton from '@material-ui/core/IconButton';
// import FirstPageIcon from '@material-ui/icons/FirstPage';
// import KeyboardArrowLeft from '@material-ui/icons/KeyboardArrowLeft';
// import KeyboardArrowRight from '@material-ui/icons/KeyboardArrowRight';
// import LastPageIcon from '@material-ui/icons/LastPage';
// import { makeStyles, useTheme } from '@material-ui/core/styles';

// export const NavLink = tw.a`
//   text-lg my-2 lg:text-sm lg:mx-6 lg:my-0
//   font-semibold tracking-wide transition duration-300
//   pb-1 border-b-2 border-transparent hover:border-yellow-500 hocus:text-yellow-500
// `;

// export const PrimaryLink = tw(NavLink)`
//   lg:mx-0
//   px-8 py-3 rounded bg-yellow-500 text-black
//   hocus:bg-yellow-700 hocus:text-gray-200 focus:shadow-outline
//   border-b-0
// `;

// const Container = styled.div`
//   ${tw`relative -mx-3 px-10 bg-center bg-cover h-screen min-h-144 pt-10 `}`;


// const useStyles1 = makeStyles((theme) => ({
//   root: {
//     flexShrink: 0,
//     marginLeft: theme.spacing(2.5),
//   },
// }));
  

// function TablePaginationActions (props) {
//   const classes = useStyles1()
//   const theme = useTheme()
//   const { count, page, rowsPerPage, onChangePage } = props

//   const handleFirstPageButtonClick = (event) => {
//     onChangePage(event, 0)
//   }

//   const handleBackButtonClick = (event) => {
//     onChangePage(event, page - 1)
//   }

//   const handleNextButtonClick = (event) => {
//     onChangePage(event, page + 1)
//   }

//   const handleLastPageButtonClick = (event) => {
//     onChangePage(event, Math.max(0, Math.ceil(count / rowsPerPage) - 1))
//   }

//   return (
//     <div className={classes.root}>
//       <IconButton
//         onClick={handleFirstPageButtonClick}
//         disabled={page === 0}
//         aria-label="first page"
//       >
//         {theme.direction === 'rtl' ? <LastPageIcon /> : <FirstPageIcon />}
//       </IconButton>
//       <IconButton onClick={handleBackButtonClick} disabled={page === 0} aria-label="previous page">
//         {theme.direction === 'rtl' ? <KeyboardArrowRight /> : <KeyboardArrowLeft />}
//       </IconButton>
//       <IconButton
//         onClick={handleNextButtonClick}
//         disabled={page >= Math.ceil(count / rowsPerPage) - 1}
//         aria-label="next page"
//       >
//         {theme.direction === 'rtl' ? <KeyboardArrowLeft /> : <KeyboardArrowRight />}
//       </IconButton>
//       <IconButton
//         onClick={handleLastPageButtonClick}
//         disabled={page >= Math.ceil(count / rowsPerPage) - 1}
//         aria-label="last page"
//       >
//         {theme.direction === 'rtl' ? <FirstPageIcon /> : <LastPageIcon />}
//       </IconButton>
//     </div>
//   )
// }

// TablePaginationActions.propTypes = {
//   count: PropTypes.number.isRequired,
//   onChangePage: PropTypes.func.isRequired,
//   page: PropTypes.number.isRequired,
//   rowsPerPage: PropTypes.number.isRequired,
// };

// const useStyles = makeStyles((theme) => ({
//   root: {
//     '& > *': {
//       marginTop: theme.spacing(2),
//     },
//   },
// }));

// export default function Review(){
//   const [reviews, setReviews] = useState(null);
//   const [loading, setLoading] = useState(false);
//   const [error, setError] = useState(null);
//   const [page, setPage] = useState(0)
//   const [rowsPerPage, setRowsPerPage] = useState(5)
//   // const dispatch = useDispatch()

//   const classes = useStyles();
  
//   useEffect(() => {
//     const fetchReviews = async () => {
//       try {
        
//         setReviews(null);
        
//         setLoading(true);
//         const response = await axios.get(
//           `${c.url}/api/reviews`
//         );

//         setReviews(response.data.reivews);
//         console.log(response.data.reivews)
//       } catch (e) {
//         setError(e);
//       }
//       setLoading(false);
//     };

//     fetchReviews();
//   }, []);

//   if (loading) return <div>..</div>;
//   if (error) return <div>error</div>;
//   if (!reviews) return null;  


//   const emptyRows = rowsPerPage - Math.min(rowsPerPage, reviews.length - page * rowsPerPage)
//   const handleChangePage = (event, newPage) => {
//     setPage(newPage)
//   }
//   const handleChangeRowsPerPage = (event) => {
//     setRowsPerPage(parseInt(event.target.value, 10))
//     setPage(0)
//   }


//   return (<div className={classes.root}>
//         <Container>
//             {/* <button onClick={fnqAxios}>Fnq axios(검색어 입력창)</button> */}
//             <PrimaryLink  margin="10em" href="/boardregister">검색</PrimaryLink>
//             <PrimaryLink  margin="10em" href="/boardregister">게시글 작성</PrimaryLink>
//             {/* <Paper className={classes.root}> */}
//             {/* <Table className={classes.table}> */}
//             <TableContainer component={Paper}>
//               <Table >
//                 <TableHead>
//                     <TableRow>
//                         <TableCell>No</TableCell>
//                         <TableCell>제목</TableCell>
//                         <TableCell>내용</TableCell>
//                     </TableRow>
//                 </TableHead>
//                 <TableBody>
//                 {(rowsPerPage > 0 
//                   ? reviews.slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage)
//                   : reviews
//                   ).map(reviews =>  (
//                     <TableRow key={reviews.review_no}>
//                         <TableCell>{reviews.review_no}</TableCell>
//                         <TableCell>{reviews.review_title}</TableCell>
//                         <TableCell>{reviews.review_detail}</TableCell>
//                     </TableRow> 
//                 ))}               
//                 {emptyRows > 0 && (
//                   <TableRow style={{ height: 53 * emptyRows }}>
//                     <TableCell colSpan={6}/>
//                   </TableRow>
//                 )}     
//                 </TableBody>
//                 <TableFooter>
//                   <TableRow>
//                     {/* <TablePagination
//                       rowPerPageOptions={[5, 10, 25, { label: 'All', value: -1 }]}
//                       colSpan={3}
//                       count={reviews.length}
//                       rowsPerPage={rowsPerPage}
//                       page={page}
//                       SelectProps={{
//                         inputProps: { 'aria-label': 'row per page'},
//                         native: true,
//                       }}
//                       onChangePage={handleChangePage}
//                       onChangeRowsPerPage={handleChangeRowsPerPage}
//                       ActionsComponent={TablePaginationActions}
//                     /> */}
//                     <Pagination 
//                       // rowPerPageOptions={[10, 20, 30, { lable: 'All', value: -1 }]}
//                       // count={reviews.length} 
//                       count = {10}
//                       rowsPerPage={rowsPerPage}
//                       page={page}
//                       SelectProps={{
//                         inputProps: { 'aria-label': 'row per page'},
//                         native: true,
//                       }}
//                       variant="outlined" 
//                       color="green"
//                       onChangePage={handleChangePage}
//                       onChangeRowsPerPage={handleChangeRowsPerPage}
//                       ActionsCoponents={TablePaginationActions}
//                     />
//                   </TableRow>
//                 </TableFooter>
//               </Table>
//             </TableContainer>
//         </Container> 
//     </div>);
// }

