import {type Actions, type Cookies, redirect} from "@sveltejs/kit";
import {logout} from "../../../scripts/helper";

export const actions: Actions = {
    default: async ({ cookies, locals }: {cookies: Cookies, locals: App.Locals}) => {
        logout({cookies, locals})
        throw redirect(303, '/')
    }
}