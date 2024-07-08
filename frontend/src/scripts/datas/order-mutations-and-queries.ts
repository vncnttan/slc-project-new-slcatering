import axios from "axios";

const base_url = import.meta.env.VITE_BACKEND_BASE_URL;

export function getCateringOrders(id: string) {
    return axios.get(`${base_url}/order?id=${id}`, {
        headers: {
            "Content-Type": "application/json"
        }
    })
}

export function getUserOrders(access_token: string) {
    return axios.get(`${base_url}/order`, {
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${access_token}`
        }
    })
}
