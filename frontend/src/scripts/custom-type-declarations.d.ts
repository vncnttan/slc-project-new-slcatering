export interface MenuInformationType {
    imageLink: string,
    title: string,
    date: string,
    stock: string,
    price: string,
    catering_variants: VariantType[],
}


export interface VariantType {
    id: string,
    variant_name: string,
    additional_price: number,
}

export interface CateringType {
    id: string,
    title: string,
    imageLink: string | null,
    price: number,
    is_closed: boolean,
    merchant: string,
    date: string,
    order_count: number,
    created_by: {
        username: string
        role: string
        store_name: string
    },
    catering_variants: VariantType[]
}

export interface OrderType {
    id: string,
    catering: {
        id: string,
        price: number,
        title: string,
        date: string,
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
        additional_price: number,
    }
}

export interface OrderRequestVariantDetailType {
    variant_id: string,
    variant_name: string,
    quantity: number,
    additional_price: number,
}

export interface OrderRequestType {
    catering_id: string,
    variants: OrderRequestVariantDetailType[],
    notes: string,
}

export type CustomerType = {
    id: string,
    username: string,
    role: string,
    store_name: string,
    total_order: number,
}