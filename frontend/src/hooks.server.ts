import type {Handle} from "@sveltejs/kit";
import {authenticateUser} from "$lib/server/auth";
import {redirect} from "@sveltejs/kit";

export const handle: Handle = async ({event, resolve}) => {
    // Authentication
    event.locals.user = authenticateUser(event)

    if (event.url.pathname == "/login" && event.locals.user) {
        // Login page must be logged out user
        throw redirect(303, "/")
    }

    if (!event.locals.user) {
        // Authenticate User Pages (Logged Out)
        const userPages = ["/transactions"]
        if(userPages.includes(event.url.pathname)) {
            throw redirect(303, "/login")
        }
    }

    if (event.locals.user?.role !== "merchant") {
        // Authenticate Merchant Pages
        if (event.url.pathname.startsWith("/merchant")) {
            throw redirect(303, "/")
        }
    }

    if (event.locals.user?.role !== "customer") {
        // Authenticate User Pages
        const customerPages = ["/transactions"]
        if(customerPages.includes(event.url.pathname)) {
            throw redirect(303, "/")
        }
    }


    // console.log(event)
    return resolve(event);
}