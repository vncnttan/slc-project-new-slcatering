import type {Actions, Cookies} from "@sveltejs/kit";
import {redirect} from "@sveltejs/kit";

export const actions: Actions = {
    default: async ({ cookies, locals }: {cookies: Cookies, locals: App.Locals}) => {
        // eslint-disable-next-line @typescript-eslint/ban-ts-comment
        // @ts-expect-error
        locals.user = null
        cookies.delete("slcatering-token", { path: "/" })
        cookies.delete("slcatering-name", { path: "/" })
        cookies.delete("slcatering-username", { path: "/" })

        throw redirect(303, '/')
    }
}