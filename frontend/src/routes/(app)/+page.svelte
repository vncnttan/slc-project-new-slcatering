<script lang="ts">
    import MenuCard from "../../components/homepage/MenuCard.svelte";
    import TopCustomer from "../../components/homepage/TopCustomer.svelte";
    import TopMenu from "../../components/homepage/TopMenu.svelte";

    let menus = [{
        name: 'Burger',
        price: 10000,
        merchant: 'Burger King',
        date: '2021-08-01'
    }, {
        name: 'Pizza',
        price: 20000,
        merchant: 'Pizza Hut',
        date: '2021-08-01'
    }, {
        name: 'Mango Sagoo',
        price: 15000,
        merchant: 'NJ23-1',
        date: '2021-08-01'
    }];
</script>

<div class="!my-8 responsive-container flex flex-col gap-16">
    <div class="p-4 md:p-6 2xl:p-10 bg-red-sig-gradient rounded-xl flex flex-col gap-16 font-inter">
        <div class="text-2xl text-white font-semibold">
            Today's Menu
        </div>
        <div class="flex flex-col gap-2">
            <div class="text-sm md:text-lg text-white font-semibold flex flex-row gap-2 flex-wrap">
                {#each menus as menu}
                    <MenuCard menu={menu}/>
                {/each}
            </div>
            <div class="text-white text-sm">
               * Ask the respective merchant for more information and pickup location
            </div>
        </div>
    </div>

    <div class="flex flex-col gap-4 m-4 md:m-0">
        <div class="text-2xl font-semibold">
            Leaderboards
            <div class="text-base text-gray-500">
                Points are calculated based on the number of transactions and the total amount of money spent
            </div>
        </div>
        <div class="grid grid-rows-2 md:grid-rows-1 md:grid-cols-2 gap-8">
            <div class="flex flex-col bg-gray-300 rounded-2xl">
                <div class="text-xl font-semibold p-4 text-center">Top Customer</div>
                <TopCustomer/>
            </div>
            <div class="flex flex-col bg-gray-300 rounded-2xl">
                <div class="text-xl font-semibold p-4 text-center">Most Popular Menu</div>
                <TopMenu/>
            </div>
        </div>
    </div>

</div>
