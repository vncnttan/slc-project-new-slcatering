<script lang="ts">
    import {onMount} from "svelte";
    import {getCateringByMerchantId} from "../../scripts/datas/catering-mutations-and-queries";
    import type {CateringType} from "../../scripts/helpers";

    export let access_token: string | undefined;
    let products: CateringType[] = [];

    onMount(async () => {
        if (!access_token) {
            return;
        }
        products = (await getCateringByMerchantId(access_token)).data
    });
</script>

<div class="relative overflow-x-auto sm:rounded-2xl rounded-md">
    <table class="w-full text-sm text-left rtl:text-right text-gray-500">
        <thead class="text-sm text-gray-800 uppercase bg-gray-300">
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
        {#each products as product}
            <tr class="odd:bg-gray-200 even:bg-gray-300 even border-b">
                <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap hidden text-center md:block">
                    {product.date}
                </th>
                <td class="px-6 py-4">
                    {product.name}
                </td>
                <td class="px-6 py-4 hidden md:inline-block">
                    Rp. {product.price}
                </td>
                <td class="px-6 py-4 ">
                    {product.variant}
                </td>
                <td class="px-6 py-4 hidden md:inline-block">
                    <div class="h-2.5 w-2.5 rounded-full {product.status === 'Active' ? 'bg-green-600' : 'bg-orange-sig'} me-1 inline-block"></div>
                    {product.status}
                </td>
                <td class="px-6 py-3 text-center">
                    <a href="/product-detail/{product.product_id}"
                       class="font-medium text-blue-600 hover:underline">Details</a>
                </td>
            </tr>
        {/each}
        </tbody>
    </table>
</div>
