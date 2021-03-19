import Axios from "axios"

const API_URL = process.env.VUE_APP_API_URL

const apiClient = Axios.create({
    baseURL: API_URL
})

export const login = async ({password, email}) => {
    const params = new URLSearchParams()
    params.append('password', password)
    params.append('username', email)
    const response = await apiClient.post("/auth/jwt/login", params, {headers:{
        'Content-Type':"application/x-www-form-urlencoded"
        }})
    console.log(response.status)
    return response.data
}
export const register = async ({password, email}) => {
    const params = {password, email}
    const response = await apiClient.post("/auth/register", params, {headers:{
        'Content-Type':"application/json"
        }})
    return response.data
}