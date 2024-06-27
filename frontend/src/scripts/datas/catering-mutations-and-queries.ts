import type {MenuInformationType} from "../helpers";
import axios from "axios";


const base_url = import.meta.env.VITE_BACKEND_BASE_URL;

export function createMenu(menu: MenuInformationType) {
    return axios.post(`${base_url}/catering`, menu, {
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${localStorage.getItem("slcatering-access_token")}`
        }
    })
}