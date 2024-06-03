import {type Cookies} from "@sveltejs/kit";


export function logout({ cookies, locals }: {cookies: Cookies, locals: App.Locals}) {
    // eslint-disable-next-line @typescript-eslint/ban-ts-comment
    // @ts-expect-error
    locals.user = null
    cookies.delete("slcatering-access_token", { path: "/" })
}