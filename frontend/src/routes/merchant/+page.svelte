<script>
    import AdminMenuCard from "../../components/homepage/AdminMenuCard.svelte";

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

<div class="text-3xl">
    <div class="mt-4 mb-12 text-center font-semibold">
        Today's Menu
    </div>
    <div class="text-sm md:text-lg text-black font-semibold flex flex-col gap-4 flex-wrap place-items-center">
        {#each menus as menu}
            <AdminMenuCard menu={menu}/>
        {/each}
    </div>
</div>
