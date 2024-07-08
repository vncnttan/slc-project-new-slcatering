<script lang="ts">
    import {afterNavigate, goto} from "$app/navigation";
    import CustomerList from "../../../components/details/CustomerList.svelte";
    import {base} from "$app/paths";
    import {page} from "$app/stores";
    import {onMount} from "svelte";
    import {getCateringDetailsById} from "../../../scripts/datas/catering-mutations-and-queries";
    import type {CateringType} from "../../../scripts/helpers";

    let id = $page.params.id;
    let menu = {} as CateringType

    let previousPage: string = base;

    afterNavigate(({from}) => {
        previousPage = from?.url.pathname || previousPage
    })

    onMount(async () => {
        menu = (await getCateringDetailsById(id)).data
    })
</script>

<div class="w-full h-screen flex flex-col xl:flex-row">
    <button on:click={()=>{goto(previousPage)}}
            class="flex flex-row gap-3 place-items-center mt-5 ms-5 py-3 px-5 w-fit hover:bg-gray-200 rounded font-semibold relative xl:absolute">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
             class="w-6 h-6">
            <path stroke-linecap="round" stroke-linejoin="round" d="M6.75 15.75 3 12m0 0 3.75-3.75M3 12h18"/>
        </svg>
        Back to {previousPage === '/' ? 'Home' : previousPage}
    </button>

    <div class="pb-5 pt-12 my-5 xl:my-0 h-screen flex-grow flex flex-col justify-center place-items-center bg-gray-100 xl:max-w-2xl">
        <div class="responsive-cols flex flex-col gap-12 font-inter">
            <div class="flex flex-row xl:flex-col gap-6">
                {#if menu.imageLink}
                    <img src={menu.imageLink} alt={menu.title} class="h-40 w-40 xl:h-72 xl:w-72 my-2 rounded-xl object-cover"/>
                {/if}
                <div class="flex flex-col">
                    <div class="text-black text-xs">
                        {menu.date}
                    </div>
                    <div class="text-red-sig text-5xl font-semibold">
                        {menu.title}
                    </div>
                    <div class="text-gray-800 text-lg">
                        {menu.created_by?.store_name}
                    </div>

                    <div class="mt-4 xl:mt-12 flex flex-col gap-1">
                        <div class="font-semibold text-3xl">
                            Rp. {menu.price}
                        </div>
                        <div class="text-xs">
                            * Price may vary depends on your variant and merchant
                        </div>
                    </div>
                </div>
            </div>

        </div>
    </div>

    <div class="h-screen flex-grow flex flex-col justify-center place-items-center">
        <div class="overflow-y-auto xl:my-24 responsive-cols w-full flex flex-col justify-center place-items-center">
            <div class="h-full w-full">
                <CustomerList catering_id={id}/>
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