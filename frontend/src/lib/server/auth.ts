import {type RequestEvent} from "@sveltejs/kit";
import axios from "axios";
import {logout} from "../../scripts/datas/user-mutations-and-queries";

export const authenticateUser = async (event: RequestEvent) => {
    // Get cookie
    const {cookies} = event

    // Cache
    const access_token = cookies.get("slcatering-access_token")
    let username = ""
    let role = ""

    try {
        // Decipher Token To User Information
        const searchResult = await axios.get(`${import.meta.env.VITE_BACKEND_BASE_URL}/user`, {
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + access_token,
            },
        });
        username = searchResult.data.username
        role = searchResult.data.role
    } catch (err) {
        if(err instanceof Error){
            console.log("An error occured on Auth: ", err.message)
        }
        // Logout here to invalidate cookies
        logout({cookies, locals: event.locals})
    }
    if (access_token) {
        return {
            token: access_token,
            username: username,
            role: role
        }
    }

    return null
}