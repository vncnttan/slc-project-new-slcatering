<script lang="ts">
    import {onMount} from "svelte";
    import {getCateringOrders} from "../../scripts/datas/order-mutations-and-queries";
    import type {OrderType} from "../../scripts/helpers";
    import {fade} from 'svelte/transition';

    export let catering_id: string
    let orders: OrderType[] = []
    let loading = true

    onMount(async () => {
        orders = (await getCateringOrders(catering_id)).data
        loading = false
    })
</script>

{#if loading}
    <div in:fade={{ delay: 500 }} out:fade class="text-center py-4 flex flex-col gap-2 text-2xl text-gray-500">
        Loading...
    </div>
{:else if orders.length === 0}
    <div in:fade={{ delay: 500 }} out:fade class="text-center py-4 flex flex-col gap-2 text-2xl text-gray-500">
        <div class="font-bold text-8xl">404</div>
        No Orders yet...
    </div>
{:else}
    <div class="relative overflow-x-auto sm:rounded-2xl rounded-md">
        <table in:fade={{ delay: 500 }} out:fade class="w-full text-sm text-left rtl:text-right text-gray-500">
            <thead class="text-sm uppercase text-white bg-gradient-to-b from-slate-700 to-gray-700 rounded-t-xl">
            <tr>
                <th scope="col" class="px-2 py-3 text-center">
                    No
                </th>
                <th scope="col" class="px-4 py-3">
                    Customer
                </th>
                <th scope="col" class="px-4 py-3 text-center">
                    Variant
                </th>
                <th scope="col" class="py-3 text-center">
                    Notes
                </th>
                <th scope="col" class="hidden md:block px-4 py-3 text-center">
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
                    <th scope="row" class="px-6 py-4 text-gray-900 whitespace-nowrap text-center">
                        {idx + 1}.
                    </th>
                    <th scope="row" class="px-4 py-4 text-gray-900 whitespace-nowrap">
                        {order.ordered_by.username}
                    </th>
                    <td class="px-4 py-4 text-center">
                        {order.variant?.variant_name ?? "Regular"}
                    </td>
                    <td class="py-4 text-center">
                        {order.notes !== "" ? order.notes : "-"}
                    </td>
                    <td class="px-4 py-4 hidden md:block text-center">
                        Rp. {order.variant?.additional_price ?? + order.catering.price}
                    </td>
                    <td class="px-4 py-4 font-bold">
                        <div class="h-2.5 w-2.5 rounded-full {order.is_paid ? 'bg-green-600' : 'bg-orange-sig'} me-1 inline-block"></div>
                        {order.is_paid ? "Paid" : "Not Paid"}
                    </td>
                </tr>
            {/each}
            </tbody>
        </table>
    </div>
{/if}
