import type {LocalType} from "../../../../types";

export const load = async ({ locals }: {locals: LocalType}) => {
    // console.log(locals.user)
    return {
        user: locals.user
    }
}

