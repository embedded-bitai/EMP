import React, { useContext } from 'react';
import { Link } from "react-router-dom";
import { CartContextProvider } from '../contexts';
import {CartIcon} from '../Icons';
// import styles from './header.module.scss';

const Header = () => {

    const {itemCount} = useContext(CartContextProvider);

    return ( 
        // <header className={styles.header}>
        <header>
            <Link to='/'>Store</Link>
            <Link to='/about'>About</Link>
            <Link to='/cart'> <CartIcon/> Cart ({itemCount})</Link>
        </header>
     );
}
 
export default Header;