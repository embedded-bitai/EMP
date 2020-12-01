import React, {useEffect, useCallback, useState} from 'react'
import {useHistory } from "react-router-dom"
import { context as c } from '../../../modules/context'
import axios from 'axios'
import Button from '@material-ui/core/Button'
import CssBaseline from '@material-ui/core/CssBaseline'
import TextField from '@material-ui/core/TextField'
// import FormControlLabel from '@material-ui/core/FormControlLabel'
// import Checkbox from '@material-ui/core/Checkbox'
import Link from '@material-ui/core/Link'
import Grid from '@material-ui/core/Grid'
import Box from '@material-ui/core/Box'
// import LockOutlinedIcon from '@material-ui/icons/LockOutlined'
import Typography from '@material-ui/core/Typography'
import { makeStyles } from '@material-ui/core/styles'
import Container from '@material-ui/core/Container'
  
import { userActions } from '../../../modules/usr/user/user.action' //eslint-disable-line

const useStyles = makeStyles((theme) => ({
  paper: {
    marginTop: theme.spacing(8),
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
  },
  avatar: {
    margin: theme.spacing(1),
    backgroundColor: theme.palette.secondary.main,
  },
  form: {
    width: '100%', // Fix IE 11 issue.
    marginTop: theme.spacing(3),
  },
  submit: {
    margin: theme.spacing(5, 1, 0),
  },
}))


const UserInfo = () => {
  /*
  유저 정보를 보여주고 수정 할 수 있다.
  */
  const classes = useStyles()
  const [password, setPassword] = useState()
  const [name, setName] = useState()
  const [gender, setGender] = useState()
  const [age, setAge] = useState()
  const [phone, setPhone] = useState()
  const [email, setEmail] = useState()

  const edit = (id) => {
    // 수정을 가능 하게 만들어 준다.
    document.getElementById(id).disabled = false
  }

const [data, setData] = useState([])
const fetchOneUser = () => {
  /*
  로그인 된 유저 정보를 불러온다. 
  */
  const user_id = sessionStorage.getItem('sessionUser')
  axios.get(`${c.url}/api/user/${user_id}`)
    .then(res=>{
      // alert('user_profile'+ JSON.stringify(res))
      // alert('user_profile'+ JSON.stringify(res.data))
      setPassword(res.data['password'])
      setName(res.data['name'])
      setGender(res.data['gender'])
      setAge(res.data['age'])
      setPhone(res.data['phone'])
      setEmail(res.data['email'])

      setData(res.data)
    })
    .catch( e => {alert(`Search failed`) 
    }

  )
}

  useEffect(() => {fetchOneUser()},[])

  const editConfirm = e => {
    // 유저 정보를 수정한다
    e.preventDefault()
    const user_id = sessionStorage.getItem('sessionUser')
    axios.put(`${c.url}/api/user/${user_id}`, {
        'user_id':user_id, 'password':password, 'name':name, 'gender':gender,  'age':age, 'phone': phone, 'email':email
    })
    .then(res=>{
        alert(`회원정보 업데이트 완료`)
        setData(res.data)
        
    })
    .catch( e=> {
        alert(`회원정보 업데이트 실패`)
        throw(e)
    })
}
  const history = useHistory()
  const deleteConfirm = useCallback(async () => {
    // 해당 유저를 삭제 한다
    const user_id = sessionStorage.getItem('sessionUser')
    try {
      alert("정말 탈퇴하시겠습니까?")
      const req = {
        method: c.delete,
        url: `${c.url}/api/user/${user_id}`,
        auth: c.auth
      }
      axios(req)
      sessionStorage.removeItem("sessionUser") 
      history.push('/')
      window.location.reload()
      // isAuth = false

    } catch (error) {
      console.log(`Error ${error}`) 
      alert('회원 탈퇴 실패')
    }
  })
  
  // const show = e => {
  //   alert('data: ' + JSON.stringify(data))
  //   alert('data: ' + JSON.stringify(data[0].name))
  //   // alert('data: ' + JSON.stringify(data.name))
  // }

  return (<>
    <Container component="main" >
      <CssBaseline />
      <div className={classes.paper}>
        {/* <button onClick={show}>show</button> */}
        {/* <Avatar className={classes.avatar}>

        </Avatar> */}
        <Typography component="h1" variant="h5">
          회원정보
        </Typography> <br/>
        <form className={classes.form} noValidate>
          <Grid container spacing={3}>
          <Grid item xs={10} sm={5} >
            <h1>ID</h1>
          </Grid>
          <Grid item xs={12} sm={5}>
            <TextField
              variant="outlined"
              required
              fullWidth
              id="Name"
              label= {(data['user_id'])}
              name="user_id"
              autoComplete="user_id"
              onChange={e => {setName(`${e.target.value}`)}}
              // defaultValue = {(data['user_id'])}
              disabled
            />
          </Grid> 
          <Grid item xs={2}> 
            <Button variant="contained" color="primary" onClick = {e => edit("name")}>
              Edit
            </Button>
          </Grid>
          <Grid item xs={10} sm={5} >
            <h1>Name</h1>
          </Grid>
          <Grid item xs={12} sm={5}>
              <TextField
                variant="outlined"
                required
                fullWidth
                id="name"
                label= {(data['name'])}
                name="name"
                autoComplete="name"
                onChange={e => {setName(`${e.target.value}`)}}
                // defaultValue = {(data['name'])}
                // disabled
              />
            </Grid>
            <Grid item xs={2}> 
              <Button variant="contained" color="primary" onClick = {e => edit("name")}>
                Edit
              </Button>
            </Grid>

            <Grid item xs={12} sm ={5}>
              <h1>Email</h1>
            </Grid>
            <Grid item xs={12} sm ={5}>
              <TextField
                variant="outlined"
                required
                fullWidth
                id="email"
                label={data['email']}
                name="email"
                autoComplete="email"
                // onChange={e => {setEmail(`${e.target.value}`)}}
                // defaultValue = {(data['email'])}
                disabled
              />
            </Grid>
            <Grid item xs={2}> 
              <Button variant="contained" color="primary" onClick = {e => alert("You cannot change Email Address")}>
                Edit
              </Button>
            </Grid>

            <Grid item xs={12} sm ={5}>
              <h1>Password</h1>
            </Grid>

            <Grid item xs={12} sm ={5}>
              <TextField
                variant="outlined"
                required
                fullWidth
                id="password"
                label="Password"
                name="password"
                autoComplete="password"
                onChange={e => {setPassword(`${e.target.value}`)}}
                // defaultValue = {data['password']}
                // disabled
              />
            </Grid>
            <Grid item xs={2}> 
              <Button variant="contained" color="primary" onClick = {e => edit("password")}>
                Edit
              </Button>
            </Grid>

            <Grid item xs={5}>
              <h1>Phone</h1>
            </Grid>
            <Grid item xs={12} sm ={5}>
              <TextField
                variant="outlined"
                required
                fullWidth
                id="phone"
                label={(data['phone'])}
                name="phone"
                autoComplete="phone"
                onChange={e => {setPhone(`${e.target.value}`)}}
                // defaultValue = {data['phone']}
                disabled
              />
            </Grid>
            <Grid item xs={2}> 
              <Button variant="contained" color="primary" onClick = {e => edit("phone")}>
                Edit
              </Button>
            </Grid>

            <Grid item xs={5}>
              <h1>Gender</h1>
            </Grid>
            <Grid item xs={5}>
              <TextField
                variant="outlined"
                required
                fullWidth
                name="gender"
                label={(data['gender'])}
                type="gender"
                id="gender"
                autoComplete="current-gender"
                onChange={e => {setGender(`${e.target.value}`)}}
                // DefaultValue = {(data['gender'])}
                // disabled
              />
            </Grid>
            <Grid item xs={2}> 
              <Button variant="contained" color="primary" onClick = {e => edit("gender")}>
                Edit
              </Button>
            </Grid>

            <Grid item xs={5} >
              <h1>Age</h1>
            </Grid>
            <Grid item xs={5}>
              <TextField
                variant="outlined"
                required
                fullWidth
                name="age"
                label={(data['age'])}
                type="age"
                id="age"
                autoComplete="current-age"
                // DefaultValue = {(data['age'])}
                onChange={e => {setAge(`${e.target.value}`)}}
                // disabled
              />
            </Grid>
            <Grid item xs={2}> 
              <Button variant="contained" color="primary" onClick = {e => edit("age")}>
                Edit
              </Button>
            </Grid>
          </Grid>
          <Grid container justify="center">
            <Button
              type="submit"
              variant="contained"
              color="primary"
              className={classes.submit}
              onClick ={editConfirm}
            >
              회원정보 수정
            </Button>
            <Button
              type="submit"
              variant="contained"
              color="primary"
              className={classes.submit}
              onClick ={deleteConfirm}
            >
              회원 탈퇴
            </Button>
            {/* <Button
              type="submit"
              variant="contained"
              color="primary"
              className={classes.submit}
              onClick ={e => userActions.remove()}
            >
              회원 탈퇴
            </Button> */}
          </Grid>
          {/* <Grid container justify="flex-end"> */}
          <br/>
          <Grid container justify="center">
            <Grid item>
              <Link href="/" variant="body1">
                Go back to Home
              </Link>
            </Grid>
          </Grid>
        </form>
      </div>
      <Box mt={5}>
      </Box>
    </Container>
  </>)
}

export default UserInfo