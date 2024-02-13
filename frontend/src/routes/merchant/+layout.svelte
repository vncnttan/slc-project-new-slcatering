<script lang="ts">
    import slcatering_logo from "$lib/assets/slcatering_logo.png";
    import {browser} from "$app/environment";
    import {onMount} from "svelte";
    import {page} from "$app/stores";

    let drawer: HTMLElement | null = null;
    let isDrawerOpen = false;
    let location: string = '';

    let toggleDrawer = () => {
        drawer?.classList.toggle('-translate-x-full');
        isDrawerOpen = !isDrawerOpen;

        if (isDrawerOpen && browser) {
            document.body.style.overflow = 'hidden';
        } else {
            document.body.style.overflow = 'auto';
        }
    }

    onMount(() => {
        // if (browser) {
        // }
        console.log(location)
        return page.subscribe(() => {
            if (browser) {
                document.body.style.overflow = 'auto';
                location = window.location.pathname;
            }
        });
    })

    let sidebar_options = [
        {
            name: "History Transaction",
            icon: [
                "M17 5.923A1 1 0 0 0 16 5h-3V4a4 4 0 1 0-8 0v1H2a1 1 0 0 0-1 .923L.086 17.846A2 2 0 0 0 2.08 20h13.84a2 2 0 0 0 1.994-2.153L17 5.923ZM7 9a1 1 0 0 1-2 0V7h2v2Zm0-5a2 2 0 1 1 4 0v1H7V4Zm6 5a1 1 0 1 1-2 0V7h2v2Z"
            ],
            link: "/merchant"
        },
        {
            name: "Create Menu",
            icon: [
                "M16.975 11H10V4.025a1 1 0 0 0-1.066-.998 8.5 8.5 0 1 0 9.039 9.039.999.999 0 0 0-1-1.066h.002Z",
                "M12.5 0c-.157 0-.311.01-.565.027A1 1 0 0 0 11 1.02V10h8.975a1 1 0 0 0 1-.935c.013-.188.028-.374.028-.565A8.51 8.51 0 0 0 12.5 0Z"
            ],
            link: "/merchant/create"
        },
    ]
</script>

<div
        bind:this={drawer}
        class="fixed top-0 left-0 z-40 w-64 h-screen transition-transform -translate-x-full sm:translate-x-0">
    <div class="h-full py-4 overflow-y-auto bg-gray-50 dark:bg-gray-800">
        <div class="flex flex-col justify-between font-medium h-full">
            <div>
                <a href="/" class="flex items-center ps-5 pe-2 mb-5">
                    <img src="{slcatering_logo}" alt="SLCatering Logo" class="h-24 object-cover"/>
                </a>
                <ul class="">
                    {#each sidebar_options as option}
                        <li>
                            <a href="{option.link}"
                               class="flex items-center p-2 h-14 text-gray-900 group
                                {location === option.link ? 'bg-red-sig !text-white' : 'hover:bg-red-100'}">
                                <svg class="flex-shrink-0 w-5 h-5 text-gray-500 transition duration-75
                                    {location === option.link ? 'bg-red-sig !text-white' : 'group-hover:text-red-900'}"
                                     aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor"
                                     viewBox="0 0 18 20">
                                    {#each option.icon as icon_path}
                                        <path d="{icon_path}"/>
                                    {/each}
                                </svg>
                                <span class="ms-3
                                {location === option.link ? 'bg-red-sig !text-white' : 'group-hover:text-red-900'}">{option.name}</span>
                            </a>
                        </li>

                    {/each}
                </ul>
            </div>
            <div class="flex flex-col gap-2 px-2">
                <form method="POST" action="/logout">
                    <button type="submit"
                            class="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-red-100 group">
                        <svg class="flex-shrink-0 w-5 h-5 text-gray-500 transition duration-75 group-hover:text-red-900"
                             aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 16">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                  d="M1 8h11m0 0L8 4m4 4-4 4m4-11h3a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2h-3"/>
                        </svg>
                        <span class="flex-1 ms-3 whitespace-nowrap group-hover:text-red-900">Logout</span>
                    </button>
                </form>
                <div class="flex flex-col px-2 font-inter">
                    <div class="font-bold text-xl">
                        NJuice Catering
                    </div>
                    <div>
                        njuice_catering@gmail.com
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<button
        on:click={toggleDrawer}
        class="{isDrawerOpen ? 'block' : 'hidden'} z-20 absolute bg-gray-800 w-full h-full opacity-50">
    Close Drawer
</button>

<div class="{isDrawerOpen ? 'overflow-hidden' : ''} sm:ml-64">
    <button on:click={toggleDrawer}
            class="inline-flex items-center p-4 mt-2 ms-3 text-sm text-gray-500 rounded-lg sm:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600">
        <span class="sr-only">Open sidebar</span>
        <svg class="w-6 h-6" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20"
             xmlns="http://www.w3.org/2000/svg">
            <path clip-rule="evenodd" fill-rule="evenodd"
                  d="M2 4.75A.75.75 0 012.75 4h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 4.75zm0 10.5a.75.75 0 01.75-.75h7.5a.75.75 0 010 1.5h-7.5a.75.75 0 01-.75-.75zM2 10a.75.75 0 01.75-.75h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 10z"></path>
        </svg>
    </button>
    <div class="w-full p-4 md:p-8">
        <slot/>
    </div>
</div>
