<script>
    let menus = [{
        name: 'Burger',
        price: 10000,
        merchant: 'Burger King'
    }, {
        name: 'Pizza',
        price: 20000,
        merchant: 'Pizza Hut'
    }, {
        name: 'Mango Sagoo',
        price: 15000,
        merchant: 'NJ23-1'
    }];
</script>

<div class="responsive-container p-10 !my-8 bg-red-sig-gradient rounded-xl flex flex-col gap-16 font-inter">
    <div class="text-2xl text-white font-semibold">
        Today's Menu
    </div>
    <div class="text-lg text-white font-semibold flex flex-row gap-2 flex-wrap">
        {#each menus as menu}
            <div class="bg-white text-black w-96 rounded-md flex flex-col gap-3 p-6">
                <div class="flex flex-row justify-between">
                    <div class="flex flex-col">
                        <div>
                            {menu.name}
                        </div>
                        <div class="text-base text-gray-400 font-normal">
                            {menu.merchant}
                        </div>
                    </div>
                    <div>
                        {menu.price}
                    </div>
                </div>
                <div class="flex flex-row w-full justify-end gap-2">
                    <button class="bg-gray-400 text-normal font-normal text-white rounded-xl p-2 w-24">Details</button>
                    <button class="bg-orange-sig text-normal font-normal text-white rounded-xl p-2 w-24">Order</button>
                </div>
            </div>
        {/each}
    </div>
</div>

<div class="h-96 bg-red-400">
asdf
</div>

<div class="h-96 bg-red-400">
asdf
</div>
