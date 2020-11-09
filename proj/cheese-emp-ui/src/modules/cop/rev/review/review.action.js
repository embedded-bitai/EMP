import { createAction, handleActions } from 'redux-actions';
import { reviewService } from './review.service'
import { alertActions } from '../alert.action'

// Action Types
import history from '../history'

export const reviewConstants = {
    REGISTER_REQUEST: 'REVIEW_REGISTER_REQUEST',
    REGISTER_SUCCESS: 'REVIEW_REGISTER_SUCCESS',
    REGISTER_FAILURE: 'REVIEW_REGISTER_FAILURE',
}

export const registerSuccess = createAction(reviewConstants.REGISTER_SUCCESS);

// Initial State
const initialState = {
    review: {} 
}

// Reducer
const reviewReducer = handleActions(
    { [reviewConstants.REGISTER_SUCCESS]: (state, action) => ({ review: action.user }) },
    initialState,
  )