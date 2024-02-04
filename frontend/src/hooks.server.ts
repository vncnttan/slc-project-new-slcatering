import type {Handle} from "@sveltejs/kit";

export const handle: Handle = async ({ event, resolve }) => {
    // const res =
    console.log(event)
    const response = await resolve(event);

    return response
}