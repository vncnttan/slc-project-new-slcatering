<script lang="ts">
    import {onMount} from "svelte";
    import {getCateringByMerchantId} from "../../scripts/datas/catering-mutations-and-queries";
    import type {CateringType} from "../../scripts/custom-type-declarations";
    import {formatPrice} from "../../scripts/helpers";

    export let access_token: string | undefined;
    let products: CateringType[] = [];

    onMount(async () => {
        if(!access_token) {
            return
        }
        products = (await getCateringByMerchantId(access_token)).data
    });
</script>

<div class="relative overflow-x-auto sm:rounded-2xl rounded-md">
    <table class="w-full text-sm text-left rtl:text-right text-gray-500">
        <thead class="text-sm text-white uppercase bg-gradient-to-b from-slate-700 to-gray-600">
        <tr>
            <th scope="col" class="text-center px-6 py-3">
                Product name
            </th>
            <th scope="col" class="text-center hidden md:block px-6 py-3">
                Price
            </th>
            <th scope="col" class="text-center px-6 py-3">
                Status
            </th>
            <th scope="col" class="text-center px-6 py-3">

            </th>
        </tr>
        </thead>
        <tbody>
        {#each products as product}
            <tr class="odd:bg-gray-200 even:bg-gray-300 even border-b">
                <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap text-center">
                    {product.title}
                </th>
                <td class="text-center px-6 py-4 hidden md:block">
                    {formatPrice(product.price)}
                </td>
                <td class="text-center px-6 py-4 ">
                    <div class="h-2.5 w-2.5 rounded-full {!product.is_closed ? 'bg-green-600' : 'bg-orange-sig'} me-1 inline-block"></div>
                    {product.is_closed ? "Closed" : "Open"}
                </td>
                <td class="text-center px-6 py-4">
                    <a href="/product-detail/{product.id}"
                       class="font-medium text-blue-600 hover:underline">Details</a>
                </td>
            </tr>
        {/each}
        </tbody>
    </table>
</div>
