import {apiServices} from "./apiServices";
import {urls} from "../constants/urls";

const authServices = {
    async login(user) {
        const {data: {access}} = await apiServices.post(urls.auth.login, user);
        localStorage.setItem('access', access)
    },

}

export {
    authServices
}