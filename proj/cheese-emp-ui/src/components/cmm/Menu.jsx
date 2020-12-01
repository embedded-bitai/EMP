import React from 'react'
import {Link} from 'react-router-dom'

export const UserMenu = () => (<nav>
    <ol>
        <li><Link to='/user-detail'>User 상세보기</Link></li>
        <li><Link to='/user-profile'>User 프로필</Link></li>
        <li><Link to='/modifying-user-info'>User 정보 수정</Link></li>
        <li><Link to='/membership-withdrawal'>Membership Withdrawal</Link></li>
        <li><Link to='/userlist'>User 리스트</Link></li>
        <li><Link to='/item'>[ Item ]</Link></li>
    </ol>
</nav>)