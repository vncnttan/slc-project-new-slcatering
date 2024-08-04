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

export const formatPrice = (price: number) => {
    return new Intl.NumberFormat("id-ID", {
        style: "currency",
        currency: "IDR"
    }).format(price);
}