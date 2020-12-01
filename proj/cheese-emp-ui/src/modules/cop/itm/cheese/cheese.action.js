import { createAction, handleActions } from 'redux-actions';
import { cheeseService } from './cheese.service'
import { alertActions } from '../../../alert.action'
import history from '../../../history'

export const cheeseConstants = {
    CHEESELIST_REQUEST: 'CHEESELIST_GET_REQUEST',
    CHEESELIST_SUCCEESS: 'CHEESELIST_GET_SUCCESS',
    CHEESELIST_FAILURE: 'CHEESELIST_GET_FAILURE'
}
export const getCheeseSuccess = createAction(cheeseConstants.CHEESELIST_SUCCEESS);
// Initial State
const initialState = {
    cheeses: []
}
// Reducer
const cheeseReducer = handleActions(
    { [cheeseConstants.CHEESELIST_SUCCEESS]: (state, action) => ({ cheeses: action.cheeses})
},
    initialState
)
// Action
export const cheeseActions =  {
    getCheese
}
////////////////////// GET /////////////////////
function getCheese() {
    return dispatch => {
        dispatch(request());
        cheeseService.getCheese()
        .then(
            cheeses => {
                dispatch(success(cheeses));
                history.push('api/cheeses')
                dispatch(alertActions.success('Cheese Registeraion Succeessful'));
            },
            error => {
                dispatch(failure(error.toString()));
                dispatch(alertActions.error(error.toString()));
            }
        );
    };
    function request() { return { type: cheeseConstants.CHEESELIST_REQUEST } }
    function success(cheeses) { return { type: cheeseConstants.CHEESELIST_SUCCEESS, cheeses } }
    function failure(error) { return { type: cheeseConstants.CHEESELIST_FAILURE, error} }
}
export default cheeseReducer