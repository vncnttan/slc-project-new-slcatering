<script lang="ts">

    let products = [
        {
            product_id: 'product1',
            name: 'Mango Sagoo',
            color: 'Silver',
            status: 'Active',
            price: 1200,
        },
        {
            product_id: 'product2',
            name: 'Peach Lemonade',
            color: 'White',
            status: 'Closed',
            price: 10000,
        },
        {
            product_id: 'product3',
            name: 'Nasi Goreng',
            color: 'Black',
            status: 'Closed',
            price: 12300,
        },
        {
            product_id: 'product4',
            name: 'Nasi Bakar',
            color: 'Gray',
            status: 'Closed',
            price: 15000,
        },
        {
            product_id: 'product5',
            name: 'Ayam Betutu',
            color: 'Red',
            status: 'Closed',
            price: 32000,
        }
    ]
</script>

<div class="relative overflow-x-auto sm:rounded-2xl rounded-md">
    <table class="w-full text-sm text-left rtl:text-right text-gray-500">
        <thead class="text-sm text-gray-800 uppercase bg-gray-300">
        <tr>
            <th scope="col" class="px-6 py-3">
                Product name
            </th>
            <th scope="col" class="hidden md:block px-6 py-3">
                Price
            </th>
            <th scope="col" class="px-6 py-3">
                Status
            </th>
            <th scope="col" class="px-6 py-3">

            </th>
        </tr>
        </thead>
        <tbody>
        {#each products as product}
            <tr class="odd:bg-gray-200 even:bg-gray-300 even border-b">
                <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap">
                    {product.name}
                </th>
                <td class="px-6 py-4 hidden md:block">
                    Rp. {product.price}
                </td>
                <td class="px-6 py-4 ">
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
