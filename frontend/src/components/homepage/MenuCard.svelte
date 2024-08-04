<script lang="ts">
    import {formatPrice} from "../../scripts/helpers";

    interface MenuType {
        name: string;
        price: number;
        merchant: string;
        date: string;
    }

    export let menu: MenuType;
</script>


<div class="bg-white text-black card-responsive-container-width rounded-md flex flex-col p-3 md:p-4 2xl:p-6">
    <div class="text-xs md:text-sm text-black font-normal">
        {menu.date}
    </div>
    <div class="flex flex-row justify-between">
        <div class="flex flex-col">
            <div>
                {menu.name}
            </div>
            <div class="text-xs md:text-base text-gray-400 font-normal">
                {menu.merchant}
            </div>
        </div>
        <div>
            {formatPrice(menu.price)}
        </div>
    </div>
    <div class="flex flex-row w-full justify-end gap-1 md:gap-2 mt-4">
        <a href="/product-detail/{menu.name}">
            <button class="bg-gray-400 hover:bg-gray-500 text-normal font-normal text-white rounded-xl p-1 md:p-2 w-20 md:w-24">Details
            </button>
        </a>
        <button class="bg-orange-sig hover:bg-red-700 text-normal font-normal text-white rounded-xl p-1 md:p-2 w-20 md:w-24">Order
        </button>
    </div>
</div>


<style>
    .card-responsive-container-width {
        width: 22rem;
    }

    @media (max-width: 1536px) {
        .card-responsive-container-width {
            width: 20rem;
        }
    }
</style>