<script lang="ts">
    import {afterNavigate, goto} from "$app/navigation";
    import CustomerList from "../../../components/details/CustomerList.svelte";
    import {base} from "$app/paths";

    let menu = {
        name: 'Nasi Bakar',
        price: '10.000',
        merchant: 'Catering Vasang',
        date: '12 September 2023'
    };

    let previousPage: string = base;

    afterNavigate(({from}) => {
        previousPage = from?.url.pathname || previousPage
    })
</script>

<div class="w-full h-screen flex flex-col md:flex-row">
    <button on:click={()=>{goto(previousPage)}}
            class="flex flex-row gap-3 place-items-center mt-5 ms-5 py-3 px-5 w-fit hover:bg-gray-200 rounded font-semibold relative md:absolute">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
             class="w-6 h-6">
            <path stroke-linecap="round" stroke-linejoin="round" d="M6.75 15.75 3 12m0 0 3.75-3.75M3 12h18"/>
        </svg>
        Back to history
    </button>

    <div class="py-5 my-5 md:my-0 h-screen flex-grow flex flex-col justify-center place-items-center bg-gray-100">
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

    <div class="h-screen flex-grow flex flex-col justify-center place-items-center">
        <div class="overflow-y-auto my-24 responsive-cols w-full flex flex-col justify-center place-items-center">
            <div class="h-full w-full">
                <CustomerList/>
            </div>
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