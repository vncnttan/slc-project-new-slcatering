import type {MenuInformationType} from "../helpers";
import axios from "axios";


const base_url = import.meta.env.VITE_BACKEND_BASE_URL;

export function createMenu(menu: MenuInformationType, access_token: string) {
    return axios.post(`${base_url}/catering`, menu, {
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${access_token}`
        }
    })
}

export function getActiveMenus() {
    return axios.get(`${base_url}/catering?active=true`, {
        headers: {
            "Content-Type": "application/json"
        }
    })
}

export function getCateringByMerchantId(access_token: string) {
    console.log(access_token)
    return axios.get(`${base_url}/catering?active=false`, {
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${access_token}`
        }
    })

}

export function getCateringDetailsById(id: string) {
    return axios.get(`${base_url}/catering?id=${id}`, {
        headers: {
            "Content-Type": "application/json"
        }
    })
}