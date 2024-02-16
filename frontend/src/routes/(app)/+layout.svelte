<!--Navbar Here-->
<script lang="ts">
    import Typewriter from "../../components/Typewriter.svelte";
    import slcatering_logo from "$lib/assets/slcatering_logo.png";
    import type {PageData} from "./$types";
    import {page} from "$app/stores";
    import {onMount} from "svelte";
    import {browser} from "$app/environment";
    import {goto} from "$app/navigation";

    export let data: PageData

    let menus = [
        {
            name: "Home",
            link: "/"
        },
        {
            name: "History",
            link: "/history"
        }
    ]

    let floatingDiv : HTMLElement | null = null;

    let navigateNavbar = (destinationLink: string) => {
        if(destinationLink === '/'){
            floatingDiv?.classList.add('home-selected-translate')
            floatingDiv?.classList.remove('history-selected-translate')
        } else {
            floatingDiv?.classList.add('history-selected-translate')
            floatingDiv?.classList.remove('home-selected-translate')
        }
        goto(destinationLink)
    }

    let location: string | null = null;
    onMount(() => {
        return page.subscribe(() => {
            if (browser) {
                location = window.location.pathname;

                if(location === '/'){
                    floatingDiv?.classList.add('home-selected-translate')
                    floatingDiv?.classList.remove('history-selected-translate')
                } else {
                    floatingDiv?.classList.add('history-selected-translate')
                    floatingDiv?.classList.remove('home-selected-translate')
                }
            }
        });
    })
</script>

<div id="navbar-container" class="font-inter fixed w-full">
    <div class="py-2 px-4 md:px-10 grid grid-cols-2 md:grid-cols-3 w-full h-24">
        <div class="h-full">
            <img src="{slcatering_logo}" alt="SLCatering Logo" class="h-20 w-64 object-contain"/>
        </div>
        {#if data.user && data.user.role === "customer"}
            <div class="hidden md:flex flex-row justify-center place-items-center font-karla">
                <div class="flex flex-row h-fit relative splace-items-center bg-gray-300 rounded-full text-lg">
                    {#each menus as menu}
                        <button on:click={() => navigateNavbar(menu.link)}
                                class="z-20 w-32 lg:w-40 xl:w-64 rounded-full h-full text-center p-2
                                {menu.link === location ? 'selected-navbar-btn' : ''}">
                            {menu.name}
                        </button>
                    {/each}

                    <div bind:this={floatingDiv} class="absolute z-0 w-32 right-1/2 translate-x-1/2 lg:w-40 xl:w-64 rounded-full h-full text-center p-2 floating-div-toggle">
                    </div>
                </div>
            </div>
        {/if}

        {#if !data.user || data?.user?.role === "merchant"}
            <div class="md:block hidden">
            </div>
        {/if}
        {#if data.user && data.user.role === "merchant"}
            <div class="flex justify-end place-items-center">
                <a href="/merchant" class="bg-orange-sig p-2 text-white rounded-md">Merchant Dashboard</a>
            </div>
        {:else}
            <div class="flex flex-row justify-end place-items-center gap-3">
                <div class="flex flex-col place-items-end">
                    {#if data.user}
                        <div class="flex flex-row gap-2">
                    <span class="text-xl font-extrabold">
                        {data.user?.username}
                    </span>
                        </div>
                    {:else}
                        <div class="flex flex-row gap-1 mb-1">
                            <a href="/login" class="py-1 px-3 bg-orange-sig text-white rounded-md">
                                Login
                            </a>
                        </div>
                    {/if}
                    <div class="flex-row gap-1">
                    <span class="hidden xl:inline">
                        Mau makan apa hari ini?
                    </span>
                        <Typewriter texts={["Budi 🤤", "Nasi Bakar", "Ayam Goreng", "Nasi Hainam", "Burger", "Bakpao"]}/>
                    </div>
                </div>
                {#if data.user}
                    <form method="POST" action="/logout">
                        <button class="w-fit h-fit rounded-full bg-gray-200 rotate-180 p-2">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                 stroke="currentColor" class="w-6 h-6">
                                <path stroke-linecap="round" stroke-linejoin="round"
                                      d="M8.25 9V5.25A2.25 2.25 0 0 1 10.5 3h6a2.25 2.25 0 0 1 2.25 2.25v13.5A2.25 2.25 0 0 1 16.5 21h-6a2.25 2.25 0 0 1-2.25-2.25V15m-3 0-3-3m0 0 3-3m-3 3H15"/>
                            </svg>
                        </button>
                    </form>
                {/if}
            </div>
        {/if}
    </div>
</div>
<div class="h-24 bg-white">
    <!--    Padding -->
</div>


<slot/>


<style>
    #navbar-container {
        background-image: linear-gradient(rgba(255, 255, 255, 1) 50%, rgba(255, 255, 255, 0.5));
        z-index: 40;
    }

    .floating-div-toggle {
        background-color: #FF461E;
        transition: all 0.5s ease-out;
    }

    .selected-navbar-btn {
        font-weight: bolder;
        color: white;
    }




</style>