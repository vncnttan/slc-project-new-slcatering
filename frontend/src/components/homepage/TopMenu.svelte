<script lang="ts">

    import {onMount} from "svelte";
    import {getMostPopularMenu} from "../../scripts/datas/catering-mutations-and-queries";
    import type {CateringType} from "../../scripts/custom-type-declarations";

    let menus: CateringType[] = []

    onMount(async ()=> {
        menus = (await getMostPopularMenu()).data
    })
</script>

<div class="grid-rows-5 grid h-full w-full">
    {#each menus as menu, i}
        <div class="{ i === 0 ? 'bg-first-place' :
                i === 1 ? 'bg-second-place' :
                i === 2 ? 'bg-third-place' : '' } py-3 px-6 flex flex-row justify-between">
            <div class="flex flex-col justify-center">
                <div class="text-2xl font-inter font-bold">
                    {menu.title}
                </div>
                <div class="text-xs font-inter text-gray-600 font-semibold">
                    {menu.date}
                </div>
            </div>
            <div class="text-sm font-inter text-black font-semibold flex justify-center place-items-center">
                {menu.order_count} order(s)
            </div>
        </div>
    {/each}
</div>