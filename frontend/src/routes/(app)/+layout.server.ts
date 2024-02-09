import type {PageServerLoad} from "../../../.svelte-kit/types/src/routes/(app)/$types";

export const load: PageServerLoad = async ({ locals }) => {
    console.log(locals.user)
    return {
        user: locals.user
    }
}