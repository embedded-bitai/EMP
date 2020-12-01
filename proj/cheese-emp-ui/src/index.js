import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
// import * as serviceWorker from './serviceWorker';
import Modal from "react-modal"; //eslint-disable-line
import { createStore, applyMiddleware } from 'redux';
import { Provider } from 'react-redux';

import rootReducer from './modules';
import logger from 'redux-logger';
import { composeWithDevTools } from 'redux-devtools-extension';
import ReduxThunk from 'redux-thunk';
import { Router } from 'react-router-dom';
import history from './modules/history';

const store = createStore(
  rootReducer,
  // If you use logger , the logger should be the last.
  composeWithDevTools(
    applyMiddleware(
      ReduxThunk.withExtraArgument({ history: history }),
      logger
    )
  )
); // You can apply multiple middleware.


ReactDOM.render(
  <Router history={ history }>
    <Provider store={store}>
    <App />
    </Provider>
  </Router>,
  document.getElementById('root')
);