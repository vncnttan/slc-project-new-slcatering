<script lang="ts">
    import {formatPrice} from "../../scripts/helpers";

    interface MenuType {
        name: string;
        price: number;
        merchant: string;
    }

    export let menu: MenuType;
</script>

<div class="text-black flex flex-col gap-3 p-2 md:p-4 responsive-admin-container border-2 border-red-600 !border-opacity-20 rounded-lg">
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
    <div class="flex flex-row w-full justify-end gap-1 md:gap-2">
        <a href="/details/{menu.name}" class="bg-gray-400 text-normal font-normal text-white rounded-xl p-1 md:p-2 w-20 md:w-24">
            Details
        </a>
        <button class="bg-orange-sig text-normal font-normal text-white rounded-xl p-1 md:p-2 w-20 md:w-24">
            Close
        </button>
    </div>
</div>


<style>
    .responsive-admin-container {
        width: 60%;
    }

    @media (max-width: 640px) {
        .responsive-admin-container {
            width: 80%;
        }
    }

    @media (max-width: 1536px) {
        .responsive-admin-container {
            width: 100%;
        }
    }
</style>