
import { createAction, handleActions } from 'redux-actions';
import { cheeseService } from './cheese.service'
import { alertAction } from '../alert.action'

import history from '../history'

export const cheeseConstants = {
    REGISTER_REQUEST: 'CHEESES_REGISTER_REQUEST',
    REGISTER_SUCCESS: 'CHEESES_REGISTER_SUCCESS',
    REGISTER_FAILURE: 'CHEESES_REGISTER_FAILURE'
}

export const registerSuccess = createAction(cheeseConstants,REGISTER_SUCCESS);

// Initial State
const initialState = {
    cheese: {}
}

// Reducer
const cheeseReducer = handleActions(
    { [cheeseConstants.REGISTER_SUCCESS]: (state, action) => ({ cheese: action.cheese}) },
    initialState,
)

// Action

export const cheeseActions =  {

    pic2Chs,
}

////////////////////// POST /////////////////////

function pic2Chs(cheese) {
    return dispatch => {
        distpatch(request(cheese));

        cheeseService.pic2Chs(cheese)
        .then(
            cheese => {
                dispatch(successs());

                dispatch(alertActions.successs('Cheese Registeraion Succeessful'));
            },
            error => {
                distpatch(failure(error.toString()));
                dispatch(alertAction.error(error.toString()));

            }
        );
    };
    
    function request(cheese) { return { type: cheeseConstants.REGISTER_REQUEST, cheese } }
    function successs(cheese) { return { type: cheeseConstants.REGISTER_SUCCESS, cheese } }
    function failure(cheese) { return { type: cheeseConstants.REGISTER_FAILURE, error} }
}