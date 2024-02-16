<script lang="ts">

    let customers = [
        {
            customer_id: 'customer1',
            name: 'NJ23-1',
            variant: 'Silver',
            status: 'Paid',
            total_paid: 1200,
        },
        {
            customer_id: 'customer2',
            name: 'JZ23-2',
            variant: 'White',
            status: 'Paid',
            total_paid: 10000,
        },
        {
            customer_id: 'customer3',
            name: 'WL23-1',
            variant: 'Black',
            status: 'Paid',
            total_paid: 12300,
        },
        {
            customer_id: 'customer4',
            name: 'ML23-1',
            variant: 'Gray',
            status: 'Paid',
            total_paid: 15000,
        },
        {
            customer_id: 'customer5',
            name: 'IC23-1',
            variant: 'Red',
            status: 'Paid',
            total_paid: 32000,
        },
        {
            customer_id: 'customer5',
            name: 'IC23-1',
            variant: 'Red',
            status: 'Paid',
            total_paid: 32000,
        },
        {
            customer_id: 'customer5',
            name: 'IC23-1',
            variant: 'Red',
            status: 'Paid',
            total_paid: 32000,
        },
        {
            customer_id: 'customer5',
            name: 'IC23-1',
            variant: 'Red',
            status: 'Paid',
            total_paid: 32000,
        },
        {
            customer_id: 'customer5',
            name: 'IC23-1',
            variant: 'Red',
            status: 'Paid',
            total_paid: 32000,
        },
        {
            customer_id: 'customer5',
            name: 'IC23-1',
            variant: 'Red',
            status: 'Paid',
            total_paid: 32000,
        },
        {
            customer_id: 'customer5',
            name: 'IC23-1',
            variant: 'Red',
            status: 'Paid',
            total_paid: 32000,
        }
    ]
</script>

<div class="relative overflow-x-auto sm:rounded-2xl rounded-md">
    <table class="w-full text-sm text-left rtl:text-right text-gray-500">
        <thead class="text-sm text-gray-800 uppercase bg-gray-300 rounded-t-xl">
        <tr>
            <th scope="col" class="px-6 py-3">
                Product name
            </th>
            <th scope="col" class="px-6 py-3">
                Variant
            </th>
            <th scope="col" class="hidden md:block px-6 py-3">
                Total Paid
            </th>
            <th scope="col" class="px-6 py-3">
                Status
            </th>
        </tr>
        </thead>
        <tbody>
        {#each customers as customer}
            <tr class="odd:bg-gray-200 even:bg-gray-300 even border-b">
                <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap">
                    {customer.name}
                </th>
                <td class="px-6 py-4">
                    {customer.variant}
                </td>
                <td class="px-6 py-4 hidden md:block">
                    Rp. {customer.total_paid}
                </td>
                <td class="px-6 py-4 ">
                    <div class="h-2.5 w-2.5 rounded-full {customer.status === 'Paid' ? 'bg-green-600' : 'bg-orange-sig'} me-1 inline-block"></div>
                    {customer.status}
                </td>
            </tr>
        {/each}
        </tbody>
    </table>
</div>
