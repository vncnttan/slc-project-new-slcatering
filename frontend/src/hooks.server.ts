import type {Handle} from "@sveltejs/kit";
import {authenticateUser} from "$lib/server/auth";
import {redirect} from "@sveltejs/kit";

export const handle: Handle = async ({event, resolve}) => {
    // Authentication
    // eslint-disable-next-line @typescript-eslint/ban-ts-comment
    // @ts-expect-error
    event.locals.user = await authenticateUser(event)

    // eslint-disable-next-line @typescript-eslint/ban-ts-comment
    // @ts-expect-error
    if (event.url.pathname == "/login" && event.locals.user) {
        // Login page must be logged out user
        throw redirect(303, "/")
    }

    // eslint-disable-next-line @typescript-eslint/ban-ts-comment
    // @ts-expect-error
    if (!event.locals.user) {
        // Authenticate User Pages (Logged Out)
        const userPages = ["/transactions"]
        if(userPages.includes(event.url.pathname)) {
            throw redirect(303, "/login")
        }
    }

    // eslint-disable-next-line @typescript-eslint/ban-ts-comment
    // @ts-expect-error
    if (event.locals.user?.role !== "merchant") {
        // Authenticate Merchant Pages
        if (event.url.pathname.startsWith("/merchant")) {
            throw redirect(303, "/")
        }
    }

    // eslint-disable-next-line @typescript-eslint/ban-ts-comment
    // @ts-expect-error
    if (event.locals.user?.role !== "customer") {
        // Authenticate User Pages
        const customerPages = ["/transactions"]
        if(customerPages.includes(event.url.pathname)) {
            throw redirect(303, "/")
        }
    }


    return resolve(event);
}