<script lang="ts">

    import {onMount} from "svelte";
    import {getTopCustomer} from "../../scripts/datas/user-mutations-and-queries";
    import type {CustomerType} from "../../scripts/custom-type-declarations";

    let highscoreCustomers: CustomerType[] = [];
    onMount(async () => {
        highscoreCustomers = (await getTopCustomer()).data;
    });
</script>

<div class="relative overflow-x-auto font-inter">
    <table class="w-full text-sm text-left rtl:text-right text-gray-500 z-0">
        <tbody>
        {#each highscoreCustomers as customer, idx}
            <tr class="odd:bg-gray-200">
                <th scope="row" class="pl-6 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                    <div class="w-10 h-10 flex flex-row justify-center place-items-center rounded-full font-bold
                              {idx + 1 === 1 ? 'bg-first-place' : idx + 1 === 2 ? 'bg-second-place' : idx + 1 === 3 ? 'bg-third-place' : '' }">
                        {idx + 1}
                    </div>
                </th>
                <td class="px-6 py-4 text-xl text-black font-bold">
                    {customer.username}
                </td>
                <td class="px-6 py-4 text-end text-black font-semibold">
                    {customer.total_order ? customer.total_order * 1000 : 0} pts
                </td>
            </tr>
        {/each}
        </tbody>
    </table>
</div>
