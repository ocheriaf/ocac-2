import {login} from "@/api/api";
const token = localStorage.getItem("truthy/token")
export const authModule = {
    state:()=>({
        token: token,
    }),
    getters:{
        isAuthenticated(
            state
        ){
            return !!state.token
        }
    },
    mutations:{
        updateToken(state, token){
            state.token = token
        },
        updateIsAuthentified(state, isAuthentified){
            state.isAuthentified = isAuthentified
        }
    },
    actions:{
        async login({commit},{email, password, rememberMe}){
            console.log("Login actions on store", {email, password, rememberMe})
            try{
                const data = await login({email, password})
                commit("updateToken", data["access_token"])
                commit("updateIsAuthentified", true)
                if(rememberMe){
                    localStorage.setItem("truthy/token", data["access_token"])
                }
            }catch(e){
                console.log(e)
            }
        }
    }
}