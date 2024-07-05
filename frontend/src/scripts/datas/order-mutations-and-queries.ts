import axios from "axios";

const base_url = import.meta.env.VITE_BACKEND_BASE_URL;

export function getCateringOrders(id: string) {
    return axios.get(`${base_url}/order?id=${id}`, {
        headers: {
            "Content-Type": "application/json"
        }
    })
}