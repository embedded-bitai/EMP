import { useRadioGroup } from '@material-ui/core';
import axios from 'axios'
import { context as c } from './context'


export const cheeseService = {
    pic2chs
};

async function pic2chs(cheese) {
    const req = {
        method: c.post,
        url: '${c.url}/api/acceess',
        data: {cheese}
    }
    const resp = await axios(req)
    const data = resp.data
    alert(' connection is successful !')
    return data
}
