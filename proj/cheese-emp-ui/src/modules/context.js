export const context = {
    get : 'GET', 
    post : 'POST', 
    put : 'PUT', 
    delete : 'DELETE', 
    // url : `http://192.168.0.5:8080`,
    // url : `http://192.168.0.21:8080`, 
    url : `http://127.0.0.1:8080`, 
    auth : () => (
        {headers: { "Access-Control-Allow-Origin" : "*",
        "Content-Type": "application/json;charset=UTF-8",
        "Accept":"application/json",
        "Authorization": `JWT fefege...`}})
}
export default context 

