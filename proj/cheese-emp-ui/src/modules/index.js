import userReducer  from './usr/user/user.action'
import cheeseReducer from './cop/itm/cheese/cheese.action'
// import reviewReducer from './cop/rev/review/review.action'

import { combineReducers } from 'redux'
const rootReducer = combineReducers({
    userReducer,
    cheeseReducer
    // reviewReducer
})

export default rootReducer