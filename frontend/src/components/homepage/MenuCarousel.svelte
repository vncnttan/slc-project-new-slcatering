<script lang="ts">
    import Siema from "siema";
    import {onMount} from "svelte";
    import {getActiveMenus} from "../../scripts/datas/catering-mutations-and-queries";

    let slider: Siema | null = null;
    let prev: () => void
    let next: () => void

    let select = 0

    interface Catering {
        title: string,
        imageLink: string | null,
        price: number,
        merchant: string,
        date: string,
        created_by: {
            username: string
            role: string
            store_name: string
        }
    }

    let menus = [] as Catering[]

    $: if (menus.length > 0) {
        setTimeout(() => {
            initializeSlider()
        }, 100)
        console.log("Slider Initialized")
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
                console.log("Just initialized Carousel")
            },
            onChange: () => {
                console.log("Just changed Carousel")
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

    onMount(async () => {
        slider?.destroy()
        menus = (await getActiveMenus()).data
    })

</script>

<div class="relative">
    <div id="siema-div" class="siema w-full justify-center justify-items-center rounded-xl">
        {#if menus.length === 0}
            <div class="w-full h-96 flex flex-row justify-center items-center">
                <div class="text-2xl font-semibold text-gray-500">
                    No Menus Available
                </div>
            </div>
        {:else}
            <!-- Black gradient overlay -->
            {#each menus as m}
                <div class="h-96 relative bg-no-repeat bg-cover bg-top rounded-xl slide-container"
                     style="background-image: {m.imageLink ? `url('${m.imageLink}')` : 'linear-gradient(90deg, #B02000, #FF370B)'}">
                    <div class="absolute w-full h-96 bg-gradient-to-t from-black/100 to-black/15"></div>
                    <div class="w-full h-96 flex flex-row justify-between place-items-end absolute font-inter p-4 md:p-6 2xl:p-10">
                        <a href="/product-detail/{m.title}" class="flex flex-row gap-3 place-items-center">
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
                                    Rp. {m.price}
                                </div>
                            </div>
                        </a>
                        <button class="bg-red-700 hover:bg-red-800 text-normal font-normal text-white rounded-xl p-1 md:p-2 w-20 md:w-24">
                            Order
                        </button>
                    </div>
                </div>
            {/each}
        {/if}
    </div>


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
