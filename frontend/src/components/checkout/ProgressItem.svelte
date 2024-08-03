<script lang="ts">
    export let item: {
        stepNum: number
        description: string
    };
    export let active: boolean;
    export let completed: boolean;
</script>

<div class="z-10 flex flex-col gap-2 place-items-center">
    <div class="rounded-full w-8 lg:w-16 h-8 lg:h-16 flex justify-center place-items-center text-xs lg:text-2xl
border-white border-8 border-solid">
        <div class="w-full h-full  rounded-full flex justify-center place-items-center font-bold p-3
            {active ? 'bg-orange-sig text-white' : 'bg-white text-gray-400 border-gray-400 border-[3px]'}">
            {#if completed}

                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="3"
                     stroke="currentColor" >
                    <path stroke-linecap="round" stroke-linejoin="round" d="m4.5 12.75 6 6 9-13.5"/>
                </svg>
            {:else}

                {item.stepNum}
            {/if}

        </div>
    </div>
    <div>
        <p class="text-center text-xs lg:text-xl {active ? 'text-orange-sig font-bold' : 'text-gray-400 text-opacity-70 font-medium'}">
            {item.description}
        </p>
    </div>
</div>