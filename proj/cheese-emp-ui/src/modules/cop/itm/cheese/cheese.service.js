import axios from 'axios'
import { context as c } from '../../../context'


export const cheeseService = {
    getCheese
};

async function getCheese() {
    const req = {
        method: c.get,
        url: `${c.url}/api/cheeses`,
    }
    const resp = await axios(req)

    const data = resp.data

    // alert(' connection is successful !')
    return data
}
