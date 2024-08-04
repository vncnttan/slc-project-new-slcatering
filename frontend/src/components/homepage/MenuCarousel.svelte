<script lang="ts">
    import Siema from "siema";
    import {onMount} from "svelte";
    import {getActiveMenus} from "../../scripts/datas/catering-mutations-and-queries";
    import {fade} from 'svelte/transition';
    import type {CateringType} from "../../scripts/custom-type-declarations";
    import {formatPrice} from "../../scripts/helpers";

    let slider: Siema | null = null;
    let prev: () => void
    let next: () => void

    let select = 0


    let menus = [] as CateringType[]

    $: if (menus.length > 0) {
        setTimeout(() => {
            initializeSlider()
        }, 100)
    }

    function initializeSlider() {
        slider = new Siema({
            selector: '.siema',
            duration: 200,
            easing: 'ease-in-out',
            perPage: 1,
            startIndex: 0,
            draggable: true,
            multipleDrag: true,
            threshold: 10,
            loop: true,
            rtl: false,
            onInit: () => {
            },
            onChange: () => {
            },
        });

        prev = () => {
            slider?.prev()
            if (select > 0) {
                select--
                select %= menus.length
            }
        }

        next = () => {
            slider?.next()
            if (select >= 0) {
                select++
                select %= menus.length
            }
        }
    }

    let loading = true

    onMount(async () => {
        slider?.destroy()
        menus = (await getActiveMenus()).data
        loading = false
    })

</script>

<div class="relative h-96">
    {#if loading}
        <div in:fade={{ delay: 500 }} out:fade
             class="w-full h-96 flex flex-row justify-center items-center animate-pulse bg-gray-200">

        </div>
    {:else if menus.length === 0}
        <div in:fade={{ delay: 500 }} out:fade class="w-full h-96 flex flex-row justify-center items-center">
            <div class="text-2xl font-semibold text-gray-500">
                No Menus Available
            </div>
        </div>
    {:else}
        <div id="siema-div" in:fade={{ delay: 500 }} out:fade
             class="siema w-full h-96 justify-center justify-items-center rounded-xl">
            <!-- Black gradient overlay -->
            {#each menus as m}
                <div class="h-96 relative bg-no-repeat bg-cover bg-center rounded-xl slide-container"
                     style="background-image: {m.imageLink ? `url('${m.imageLink}')` : 'linear-gradient(90deg, #B02000, #FF370B)'}">
                    <div class="absolute w-full h-96 bg-gradient-to-t from-black/100 to-black/15"></div>
                    <div class="w-full h-96 flex flex-row justify-between place-items-end absolute font-inter p-4 md:p-6 2xl:p-10">
                        <a href="/product-detail/{m.id}" class="flex flex-row gap-3 place-items-center">
                            <img src="{m.imageLink ?? 'https://img.freepik.com/premium-vector/default-image-icon-vector-missing-picture-page-website-design-mobile-app-no-photo-available_87543-11093.jpg'}"
                                 alt="Menu Preview" class="w-20 h-20 rounded-md object-cover"/>
                            <div class="flex flex-col">
                                <div class="text-white">
                                    {m.created_by.store_name}
                                </div>
                                <div class="text-4xl text-white font-semibold">
                                    {m.title}
                                </div>
                                <div class="text-sm text-white">
                                    {formatPrice(m.price)}
                                </div>
                            </div>
                        </a>
                        <div class="flex flex-row gap-3">
                            <a href="/product-detail/{m.id}">
                                <button class="bg-gray-600 hover:bg-gray-700 text-normal text-lg text-white rounded-xl p-1 md:p-3  tracking-wide w-20 md:w-28">
                                    Details
                                </button>
                            </a>
                            <a href="/checkout/{m.id}">
                                <button class="bg-red-600 hover:bg-red-700 text-normal text-lg text-white rounded-xl p-1 md:p-3 font-semibold tracking-wide w-20 md:w-28">
                                    Order
                                </button>
                            </a>
                        </div>
                    </div>
                </div>
            {/each}
        </div>
    {/if}


    <!--    Slider Radio Button -->
    {#if menus.length > 1}
        <div class="md:flex justify-center items-center">
            {#each menus as _, i} <!-- eslint-disable-line @typescript-eslint/no-unused-vars -->
                <button class={"w-2 h-2 rounded-full mx-1 mt-4 cursor-pointer " + (select === i ? "bg-gray-400" : "bg-gray-300")}
                        on:click={() => {
                slider?.goTo(i)
                select = i
            }}></button>
            {/each}
        </div>
        <button on:click={prev} class="hidden md:block absolute top-[45%] left-[-3rem] text-black">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                 stroke="currentColor"
                 class="size-8">
                <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 19.5 8.25 12l7.5-7.5"/>
            </svg>
        </button>
        <button on:click={next} class="hidden md:block absolute top-[45%] right-[-3rem] text-black">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                 stroke="currentColor"
                 class="size-8">
                <path stroke-linecap="round" stroke-linejoin="round" d="m8.25 4.5 7.5 7.5-7.5 7.5"/>
            </svg>
        </button>
    {/if}
</div>
