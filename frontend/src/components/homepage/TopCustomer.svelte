<script>

    let highscoreCustomers = [
        {
            rank: 1,
            name: 'NJ23-1',
            points: 19500
        },
        {
            rank: 2,
            name: 'XD23-1',
            points: 18500
        },
        {
            rank: 3,
            name: 'WL23-1',
            points: 10500
        },
        {
            rank: 4,
            name: 'MY23-1',
            points: 9500
        },
        {
            rank: 5,
            name: 'PB23-1',
            points: 500
        },
        {
            rank: 6,
            name: 'ML23-1',
            points: 300
        },
    ];
</script>

<div class="relative overflow-x-auto font-inter">
    <table class="w-full text-sm text-left rtl:text-right text-gray-500 z-0">
        <tbody>
        {#each highscoreCustomers as customer}
            <tr class="odd:bg-gray-200">
                <th scope="row" class="pl-6 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                    <div class="w-10 h-10 flex flex-row justify-center place-items-center rounded-full font-bold
                              {customer.rank === 1 ? 'bg-yellow-500' : customer.rank === 2 ? 'bg-gray-400' : customer.rank === 3 ? 'bg-orange-700' : '' }">
                        {customer.rank}
                    </div>
                </th>
                <td class="px-6 py-4 text-xl text-black font-bold">
                    {customer.name}
                </td>
                <td class="px-6 py-4 text-end text-black font-semibold">
                    {customer.points} pts
                </td>
            </tr>
        {/each}
        </tbody>
    </table>
</div>
