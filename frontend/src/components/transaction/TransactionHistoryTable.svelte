<script lang="ts">

    let products = [
        {
            date: '2021-10-10',
            name: 'Product 1',
            price: 100000,
            variant: 'Jumbo',
            status: 'Active',
            product_id: 1
        },
        {
            date: '2021-10-10',
            name: 'Product 2',
            price: 200000,
            variant: 'Reguler',
            status: 'Inactive',
            product_id: 2
        },
        {
            date: '2021-10-10',
            name: 'Product 3',
            price: 300000,
            variant: 'Reguler',
            status: 'Active',
            product_id: 3
        },
        {
            date: '2021-10-10',
            name: 'Product 4',
            price: 400000,
            variant: 'Reguler',
            status: 'Inactive',
            product_id: 4
        },
        {
            date: '2021-10-10',
            name: 'Product 5',
            price: 500000,
            variant: 'Reguler',
            status: 'Active',
            product_id: 5
        },
        {
            date: '2021-10-10',
            name: 'Product 6',
            price: 600000,
            variant: 'Reguler',
            status: 'Inactive',
            product_id: 6
        },
        {
            date: '2021-10-10',
            name: 'Product 7',
            price: 700000,
            variant: 'Reguler',
            status: 'Active',
            product_id: 7
        },
        {
            date: '2021-10-10',
            name: 'Product 8',
            price: 800000,
            variant: 'Jumbo',
            status: 'Inactive',
            product_id: 8
        },
        {
            date: '2021-10-10',
            name: 'Product 9',
            price: 900000,
            variant: 'Reguler',
            status: 'Active',
            product_id: 9
        },
        {
            date: '2021-10-10',
            name: 'Product 10',
            price: 1000000,
            variant: 'Reguler',
            status: 'Inactive',
            product_id: 10
        }
    ]
</script>

<div class="relative overflow-x-auto sm:rounded-2xl rounded-md">
    <table class="w-full text-sm text-left rtl:text-right text-gray-500">
        <thead class="text-sm text-gray-800 uppercase bg-gray-300">
        <tr>
            <th scope="col" class="hidden md:inline-block px-6 py-3">
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
                <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap hidden md:inline-block">
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
                <td class="px-6 py-4">
                    <a href="/merchant/product-detail/{product.product_id}"
                       class="font-medium text-blue-600 hover:underline">Details</a>
                </td>
            </tr>
        {/each}
        </tbody>
    </table>
</div>
