import React, {useState} from 'react'
import axios from 'axios'
import '../styles/table.style.css'



const UserRegister = () => {
    const [userid, setUserid] = useState()
    const [password, setPassword] = useState()
    const [name, setName] = useState()
    const [pclass, setPclass] = useState()
    const [gender, setGender] = useState()
    const [birthYear, setBirthYear] = useState()
    const [embarked, setEmbarked] = useState()

    const register = e => {
        e.preventDefault()
        axios.post(`http:localhost:8080/user/register`,  {
            userid,password,name,pclass,gender,birthYear,embarked
        })
        .then(
            console.log(`signup SUCCESS`)
        )
        .error(
            console.log(`signup FAIL`)
        )

    }

    
    return (<>
        <h1>UserRegister</h1><form>
        <table className='tab_layer'>
            
                
                <tr className='tab_layer'>
                    <td className='tab_layer'>ID</td>
                    <td className='tab_layer'><input type="text" onChange={e => setUserid(e.target.value)}/></td>
                </tr>
                

                <tr className='tab_layer'> 
                    <td className='tab_layer'>PASSWORD</td>
                    <td><input type="text" onChange={e => setPassword(e.target.value)}/></td>
                </tr>
                <tr className='tab_layer'>
                    <td className='tab_layer'>NAME</td>
                    <td className='tab_layer'><input type="text" onChange={e => setName(e.target.value)}/></td>
                </tr>
                <tr className='tab_layer'>
                    <td className='tab_layer'>PCLASS</td>
                    <td><input type="text" onChange={e => setPclass(e.target.value)}/></td>
                </tr>
                <tr className='tab_layer'>
                    <td className='tab_layer'>GENDER</td>
                    <td><input type="text" onChange={e => setGender(e.target.value)}/></td>
                </tr>
                <tr className='tab_layer'>
                    <td className='tab_layer'>BIRTH YEAR</td>
                    <td><input type="text" onChange={e => setBirthYear(e.target.value)}/></td>
                </tr>
                <tr className='tab_layer'>
                    <td className='tab_layer'>EMBARKED</td>
                    <td><input type="text" onChange={e => setEmbarked(e.target.value)}/></td>
                </tr>
                {/* <tr>
                    <td>RANK</td> 
                    <td>Do not enter ratings..</td>
                </tr> */}
                <tr>
                    <td colspan={2}><button onClick={register}>Register</button>
                    <button>Cancel</button></td>
                </tr>
            
        </table></form>
    </>)
}

export default UserRegister