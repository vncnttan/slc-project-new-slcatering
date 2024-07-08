<script lang="ts">
    import {onMount} from "svelte";
    import type {OrderType} from "../../scripts/helpers";
    import {getUserOrders} from "../../scripts/datas/order-mutations-and-queries";
    import {fade} from 'svelte/transition';

    export let access_token: string | undefined;
    let orders: OrderType[] = [];
    let loading = true

    onMount(async () => {
        if (!access_token) {
            return;
        }
        orders = (await getUserOrders(access_token)).data
        loading = false
    });
</script>

<div class="relative overflow-x-auto sm:rounded-2xl rounded-md">
    {#if loading}
        <div in:fade={{ delay: 500 }} out:fade class="text-center p-4">
            <p class="text-gray-500">Loading...</p>
        </div>
    {:else}
        {#if orders.length === 0}
            <div in:fade={{ delay: 500 }} out:fade class="text-center p-4">
                <p class="text-gray-500">You haven't made any orders yet</p>
            </div>
        {:else}
            <table in:fade={{ delay: 500 }} out:fade class="w-full text-sm text-left rtl:text-right text-gray-500">
                <thead class="text-sm text-white uppercase bg-gradient-to-b from-slate-700 to-gray-600">
                <tr>
                    <th scope="col" class="hidden md:block px-6 py-3 text-center">
                        Date
                    </th>
                    <th scope="col" class="px-6 py-3">
                        Product name
                    </th>
                    <th scope="col" class="hidden md:inline-block px-6 py-3">
                        Total Paid
                    </th>
                    <th scope="col" class="px-6 py-3">
                        Variant
                    </th>
                    <th scope="col" class="px-6 py-3 hidden md:inline-block">
                        Status
                    </th>
                    <th scope="col" class="px-6 py-3">

                    </th>
                </tr>
                </thead>
                <tbody>
                {#each orders as order}
                    <tr class="odd:bg-gray-200 even:bg-gray-300 even border-b">
                        <th scope="row"
                            class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap hidden text-center md:block">
                            {order.catering.date}
                        </th>
                        <td class="px-6 py-4">
                            {order.catering.title}
                        </td>
                        <td class="px-6 py-4 hidden md:inline-block">
                            Rp. {order.variant?.additional_price ?? + order.catering.price}
                        </td>
                        <td class="px-6 py-4 ">
                            {order.variant?.variant_name ?? "Regular"}
                        </td>
                        <td class="px-6 py-4 hidden md:inline-block">
                            <div class="h-2.5 w-2.5 rounded-full {order.is_paid ? 'bg-green-600' : 'bg-orange-sig'} me-1 inline-block"></div>
                            {order.is_paid ? "Paid" : "Not Paid"}
                        </td>
                        <td class="px-6 py-3 text-center">
                            <a href="/product-detail/{order.catering.id}"
                               class="font-medium text-blue-600 hover:underline">Details</a>
                        </td>
                    </tr>
                {/each}
                </tbody>
            </table>
        {/if}
    {/if}
</div>
