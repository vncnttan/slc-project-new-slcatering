<script lang="ts">
    import {onMount} from "svelte";
    import {getCateringOrders} from "../../scripts/datas/order-mutations-and-queries";
    import type {OrderType} from "../../scripts/helpers";

    export let catering_id: string
    let orders: OrderType[] = []
    onMount(async () => {
        orders = (await getCateringOrders(catering_id)).data
    })
</script>

<div class="relative overflow-x-auto sm:rounded-2xl rounded-md">
    {#if orders.length === 0}
        <div class="text-center py-4 flex flex-col gap-2 text-2xl text-gray-500">
            <div class="font-bold text-8xl">404</div>
            No Orders yet...
        </div>
    {:else}
        <table class="w-full text-sm text-left rtl:text-right text-gray-500">
            <thead class="text-sm text-gray-800 uppercase bg-gray-300 rounded-t-xl">
            <tr>
                <th scope="col" class="pl-6 py-3">
                    No
                </th>
                <th scope="col" class="px-4 py-3">
                    Customer
                </th>
                <th scope="col" class="px-4 py-3">
                    Variant
                </th>
                <th scope="col" class="py-3">
                    Notes
                </th>
                <th scope="col" class="hidden md:block px-4 py-3">
                    Total Paid
                </th>
                <th scope="col" class="px-4 py-3">
                    Status
                </th>
            </tr>
            </thead>
            <tbody>
            {#each orders as order, idx}
                <tr class="odd:bg-gray-200 even:bg-gray-300 even border-b text-medium">
                    <th scope="row" class="px-4 py-4 text-gray-900 whitespace-nowrap">
                        {idx + 1}
                    </th>
                    <th scope="row" class="px-4 py-4 text-gray-900 whitespace-nowrap">
                        {order.ordered_by.username}
                    </th>
                    <td class="px-4 py-4">
                        {order.variant.variant_name}
                    </td>
                    <td class="py-4">
                        {order.notes}
                    </td>
                    <td class="px-4 py-4 hidden md:block">
                        Rp. {order.variant.additional_price + order.catering.price}
                    </td>
                    <td class="px-4 py-4 ">
                        <div class="h-2.5 w-2.5 rounded-full {order.is_paid ? 'bg-green-600' : 'bg-orange-sig'} me-1 inline-block"></div>
                        {order.is_paid ? "Paid" : "Not Paid"}
                    </td>
                </tr>
            {/each}
            </tbody>
        </table>
    {/if}
</div>
