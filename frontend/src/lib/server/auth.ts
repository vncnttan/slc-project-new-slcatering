import type {RequestEvent} from "@sveltejs/kit";


export const authenticateUser = (event: RequestEvent) => {
    // Get cookie
    const {cookies} = event

    // TODO: Get access token, then pass to backend to solve the username and full name
    // const access_token = cookies.get("slcatering-access_token")
    const name = cookies.get("slcatering-name")
    const username = cookies.get("slcatering-username")
    const role = cookies.get("slcatering-role")

    if(name && username && role) {
        return {
            name: name,
            username: username,
            role: role
        }
    }

    return null
}