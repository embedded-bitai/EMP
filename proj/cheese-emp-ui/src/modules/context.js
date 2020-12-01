export const context = {
    get : 'GET', 
    post : 'POST', 
    put : 'PUT', 
    delete : 'DELETE', 
    url : `http://127.0.0.1:8080`, 
    auth : () => (
        {headers: { "Access-Control-Allow-Origin" : "*",
        "Content-Type": "application/json;charset=UTF-8",
        "Accept":"application/json",
        "Authorization": `JWT fefege...`}})
}
export default context 

