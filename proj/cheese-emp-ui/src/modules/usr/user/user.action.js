import { createAction, handleActions } from 'redux-actions';
import { userService } from './user.service'
import { alertActions } from '../../alert.action'
import history from '../../history'


// Action Types
export const userConstants = {
  REGISTER_REQUEST: 'USERS_REGISTER_REQUEST',
  REGISTER_SUCCESS: 'USERS_REGISTER_SUCCESS',
  REGISTER_FAILURE: 'USERS_REGISTER_FAILURE',

  LOGIN_REQUEST: 'USERS_LOGIN_REQUEST',
  LOGIN_SUCCESS: 'USERS_LOGIN_SUCCESS',
  LOGIN_FAILURE: 'USERS_LOGIN_FAILURE',
  
  LOGOUT: 'USERS_LOGOUT',

  GETALL_REQUEST: 'USERS_GETALL_REQUEST',
  GETALL_SUCCESS: 'USERS_GETALL_SUCCESS',
  GETALL_FAILURE: 'USERS_GETALL_FAILURE',

  DELETE_REQUEST: 'USERS_DELETE_REQUEST',
  DELETE_SUCCESS: 'USERS_DELETE_SUCCESS',
  DELETE_FAILURE: 'USERS_DELETE_FAILURE'    
}

// let sessionUser = JSON.parse(sessionStorage.getItem("user"));

export const loginSuccess = createAction(userConstants.LOGIN_SUCCESS);

// Initial State
const initialState = {
    user: {}, 
    loggingIn: false
}
// Reducer
const userReducer = handleActions(
    { [userConstants.LOGIN_SUCCESS]: (state, action) => ({ loggingIn: true, user: action.user }) },
    initialState,
  )


// Actions




export const userActions = {
  
  register, login, logout, update, remove,
  getAll, getById, getByOption, goToDest, 
}

///////////////////////////////////////
///////////////////////////////////////
//////////////    POST   //////////////
///////////////////////////////////////
///////////////////////////////////////

function register(user) {
    return dispatch => {
        dispatch(request(user));
        //alert(user.data)
        // alert('user action: ' + JSON.stringify(user))
        userService.register(user)
            .then(
                user => { 
                    // alert(JSON.stringify(user))
                    dispatch(success());
                    dispatch(alertActions.success('Registration successful'));
                    history.push('/login')
                    window.location.reload('/login')
                },
                error => {
                    dispatch(failure(error.toString()));
                    dispatch(alertActions.error(error.toString()));
                }
            );
    };
  
    function request(user) { return { type: userConstants.REGISTER_REQUEST, user } }
    function success(user) { return { type: userConstants.REGISTER_SUCCESS, user } }
    function failure(error) { return { type: userConstants.REGISTER_FAILURE, error } }
}


function login(user_id, password){
    alert(`BBBBB ${user_id} & ${password}`)
    return dispatch => {
        dispatch(request({ user_id }))

        userService.login(user_id, password)
            .then(
                user => { 
                    console.log(`이름 ========== : ${user.name}`)
                    alert(`이름 ======== : ${user.name}`)
                    sessionStorage.setItem("sessionUser", user.data['user_id'])
                    dispatch(success(user))
                    history.push('/user-detail')
                    window.location.reload()
             },
            error => {
                dispatch(failure(error.toString()));
                dispatch(alertActions.error(error.toString()));
            }
          )
    }

  function request(user) { return { type: userConstants.LOGIN_REQUEST, user } }
  function success(user) { 
    console.log(`#2 Login User Name is ${user.name}`)
    return { type: userConstants.LOGIN_SUCCESS, user } 
  }
  function failure(error) { return { type: userConstants.LOGIN_FAILURE, error } }
}

function logout() {
    userService.logout();
    return { type: userConstants.LOGOUT };
}

function update() {
    userService.update();
    return { type: userConstants.LOGOUT };
  }

function remove(id) {
    return dispatch => {
        dispatch(request(id));
  
        userService.delete(id)
            .then(
                user => dispatch(success(id)),
                error => dispatch(failure(id, error.toString()))
            );
    };
  
    function request(id) { return { type: userConstants.DELETE_REQUEST, id } }
    function success(id) { return { type: userConstants.DELETE_SUCCESS, id } }
    function failure(id, error) { return { type: userConstants.DELETE_FAILURE, id, error } }
  }





///////////////////////////////////////
///////////////////////////////////////
//////////////    GET   //////////////
///////////////////////////////////////
///////////////////////////////////////


function getAll() {
    return dispatch => {
        dispatch(request());

        userService.getAll()
            .then(
                users => dispatch(success(users)),
                error => dispatch(failure(error.toString()))
            );
    };

    function request() { return { type: userConstants.GETALL_REQUEST } }
    function success(users) { return { type: userConstants.GETALL_SUCCESS, users } }
    function failure(error) { return { type: userConstants.GETALL_FAILURE, error } }
}
function getById() {
    return  dispatch => {
        userService.getById().then(
        resp => { 
            
        },
        error => {alert(`Error`)}
        )
  }
}
function goToDest(dest) {history.push(dest)}
// function bulk(){
//     return dispatch => {
//         userService.bulk().then(
//             resp => {},
//             error => {}
//         )
//     }
// }
// function count (){
//     return dispatch => {
//         userService.count().then(
//             resp => {},
//             error => {}
//         )
//     }
// }
function getByOption(){
    return dispathc => {
        
    }
}
/*
const fetchAllUsers = useCallback(async () => {
    try{
        const req = {
            method: c.get, 
            url: `${c.url}/api/users`
        }
        const res = await axios(req)   
        setUsers(res.data)
    }catch(error){
        alert(`fetchAllUsers failure`)
        throw(error)
    }
},[]) 
const fetchSomeUsers = useCallback(async e=>{
    e.preventDefault()
    try {
        const req = {
            method: c.get,
            url: `${c.url}/api/users`,
            data: {params: e.target.getAttribute('user_id')},
            auth: c.auth
        }
        const res = await axios(req)   
    } catch (error) {
        alert(`fetchSomeUsers failure`)
        throw(error)
    }
},[])
const fetchOneUser = useCallback(async e => {
    e.preventDefault()
    try {
        
        const user_id = e.target.getAttribute('user_id')
        console.log(`Search Id is ${user_id}`) 
        const req = {
            method: c.get,
            url: `${c.url}/api/user/${user_id}`,
            auth: c.auth
        }
        const res = await axios(req)   
        const data = JSON.parse(res.data)
        setUser(data)
        console.log(`${data.name}`) 
        history.push("/user-detail");
    } catch (error) {
        console.log(`Error ${error}`) 
    }
},[])
*/
export default userReducer