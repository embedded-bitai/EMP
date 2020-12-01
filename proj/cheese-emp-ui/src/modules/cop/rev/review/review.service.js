import axios from 'axios'
import { context as c } from '../../../context'


export const reviewService = {
    getReviews
};

async function getReviews(reviews) {
    const req = {
        method: c.get,
        url: `${c.url}/api/reviews/${reviews}`,
        // data: {cheese}
    }
    const resp = await axios(req)

    const data = resp.data

    alert(' connection is successful !')
    return data
}
