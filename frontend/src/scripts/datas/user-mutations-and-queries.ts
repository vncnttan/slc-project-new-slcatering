import type {Cookies} from "@sveltejs/kit";
import axios from "axios";

const base_url = import.meta.env.VITE_BACKEND_BASE_URL;

export function logout({cookies, locals}: { cookies: Cookies, locals: App.Locals }) {
    // eslint-disable-next-line @typescript-eslint/ban-ts-comment
    // @ts-expect-error
    locals.user = null
    cookies.delete("slcatering-access_token", {path: "/"})
}

export async function login(usernameInput: string, passwordInput: string) {
    return await axios.post(`${base_url}/login`, {
        username: usernameInput,
        password: passwordInput
    })
}