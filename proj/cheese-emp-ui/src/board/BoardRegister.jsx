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
    const styles = () => ({
        th, tr, td: {
            border: "1px solid black",
            margin: 0
        },
        
        tab_layer: {
            width: 500
           
        }
    });
    
    return (<>
        <h1>UserRegister</h1><form>
        <table className={classes.tab_layer}>
            
                <tr>
                    <td>ID</td>
                    <td><input type="text" onChange={e => setUserid(e.target.value)}/></td>
                </tr>
                <tr>
                    <td>PASSWORD</td>
                    <td><input type="text" onChange={e => setPassword(e.target.value)}/></td>
                </tr>
                <tr>
                    <td>NAME</td>
                    <td><input type="text" onChange={e => setName(e.target.value)}/></td>
                </tr>
                <tr>
                    <td>PCLASS</td>
                    <td><input type="text" onChange={e => setPclass(e.target.value)}/></td>
                </tr>
                <tr>
                    <td>GENDER</td>
                    <td><input type="text" onChange={e => setGender(e.target.value)}/></td>
                </tr>
                <tr>
                    <td>BIRTH YEAR</td>
                    <td><input type="text" onChange={e => setBirthYear(e.target.value)}/></td>
                </tr>
                <tr>
                    <td>EMBARKED</td>
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