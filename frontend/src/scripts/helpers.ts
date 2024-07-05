import {toast} from "@zerodevx/svelte-toast";


const ERROR_TYPE_TOAST_OPTIONS = [{
    "--toastBackground": "#B02000",
    "--toastColor": "#fff",
    "--toastProgressBackground": "#fff",
    "--toastProgressColor": "#B02000",
}, {
    "--toastBackground": "#008000",
    "--toastColor": "#fff",
    "--toastProgressBackground": "#fff",
    "--toastProgressColor": "#008000"
}, {
    "--toastBackground": "#0000FF",
    "--toastColor": "#fff",
    "--toastProgressBackground": "#fff",
    "--toastProgressColor": "#0000FF"
}, {
    "--toastBackground": "#FFA500",
    "--toastColor": "#fff",
    "--toastProgressBackground": "#fff",
    "--toastProgressColor": "#FFA500"
}]

export enum TOAST_TYPE {
    ERROR = 0,
    SUCCESS = 1,
    INFO = 2,
    WARNING = 3
}

export const showToast = (message: string, type: TOAST_TYPE) => {
    toast.push(message, {
        theme: {...ERROR_TYPE_TOAST_OPTIONS[type],
            "--toastMsgPadding": "1rem 1rem",
            "--toastWidth": "20rem",
        },
    })
}

export interface MenuInformationType {
    imageLink: string,
    title: string,
    date: string,
    stock: string,
    price: string,
    catering_variants: VariantType[],
}

export interface VariantType {
    variant_name: string,
    additional_price: number | null,
}

export interface CateringType {
    id: string,
    title: string,
    imageLink: string | null,
    price: number,
    is_closed: boolean,
    merchant: string,
    date: string,
    created_by: {
        username: string
        role: string
        store_name: string
    }
}

export interface OrderType {
    id: string,
    catering: {
        price: number,
        title: string,
    },
    is_paid: boolean,
    notes: string,
    ordered_by: {
        id: string,
        username: string,
        role: string,
    },
    variant: {
        id: string,
        variant_name: string,
        additional_price: string,
    }
}