import {apiServices} from "./apiServices";
import {urls} from "../constants/urls";

const carServices = {
    getAll() {
        return apiServices.get(urls.listing)
    },

    create(data) {
        return apiServices.post(urls.listing, data)
    },
    getOneCar(id){
        return apiServices.get(urls.listing + `/${id}`)
    },
    getCarStats(id){
        return apiServices.get(urls.listing + `${id}` + '/stats')
    }
}

export {
    carServices
}