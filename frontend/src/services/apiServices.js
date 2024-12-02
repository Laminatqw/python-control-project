import axios from "axios";
import {baseURL} from "../constants/urls";

const apiServices = axios.create({baseURL})

apiServices.interceptors.request.use(req => {
    const token = localStorage.getItem('access');

    if (token) {
        req.headers.Authorization = `Bearer ${token}`
    }

    return req
})

export {
    apiServices
}