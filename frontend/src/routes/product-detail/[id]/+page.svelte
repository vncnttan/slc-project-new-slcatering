<script lang="ts">
    import {goto} from "$app/navigation";

    let menu = {
        name: 'Nasi Bakar',
        price: '10.000',
        merchant: 'Catering Vasang',
        date: '12 September 2023'
    };
</script>


<div class="w-full h-screen grid grid-cols-2">
    <button class="flex flex-row gap-3 place-items-center mt-5 ms-5 py-3 px-5 w-fit hover:bg-gray-200 rounded font-semibold absolute">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
             class="w-6 h-6">
            <path stroke-linecap="round" stroke-linejoin="round" d="M6.75 15.75 3 12m0 0 3.75-3.75M3 12h18"/>
        </svg>
        Back to history
    </button>

    <div class="h-full flex flex-col justify-center place-items-center bg-gray-100">
        <div class="responsive-cols flex flex-col gap-12 font-inter">
            <div class="flex flex-col gap-1">
                <div class="text-black text-base font-bold">
                    {menu.date}
                </div>
                <div class="text-red-sig text-7xl font-semibold">
                    {menu.name}
                </div>
                <div class="text-gray-400 text-xl font-bold">
                    {menu.merchant}
                </div>
            </div>
            <div class="flex flex-col gap-1">
                <div class="font-semibold text-3xl">
                    Rp. {menu.price}
                </div>
                <div class="text-xs">
                    * Price may vary depends on your variant and merchant
                </div>
            </div>

            <button class="font-bold bg-red-sig-gradient text-white w-fit p-4 rounded-md"
                    on:click={()=>{goto("/")}}>
                Go to today's menu
            </button>
        </div>
    </div>

    <div class="h-full flex flex-col p-4">
        <div class="h-full flex flex-col justify-center place-items-center bg-gray-100">
            Buyer
        </div>
    </div>

</div>

<style>
    .responsive-cols {
        width: 95%;
    }

    @media (min-width: 640px) {
        .responsive-cols {
            width: 90%;
        }
    }

    @media (min-width: 768px) {
        .responsive-cols {
            width: 80%;
        }
    }
</style>