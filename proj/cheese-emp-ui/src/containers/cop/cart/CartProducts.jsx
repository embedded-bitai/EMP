import React, { useContext } from 'react';
import { CartContextProvider } from './contexts';
import Cart from './CartMain'
import CartItem from './CartItem';
// import styles from './CartProducts.module.scss';

const CartProducts = () => {

    const { cartItems } = useContext(CartContextProvider);

    return ( <Cart> 
        {/* <div className={styles.p__container}> */}
        <div>
            <div className="card card-body border-0">

                {
                    cartItems.map(product =>  <CartItem key={product.id} product={product}/>)
                }

            </div>
        </div>
        </Cart> 
     );
}
 
export default CartProducts;