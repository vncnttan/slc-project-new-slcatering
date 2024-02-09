<script lang="ts">
    export let inputValue: string;

    let fieldIcon: HTMLElement | null = null;

    let fieldFocus = () => {
        console.log(fieldIcon)
        fieldIcon?.classList.remove("text-gray-500")
        fieldIcon?.classList.add("text-red-sig")
    }

    let fieldBlur = () => {
        fieldIcon?.classList.remove("text-red-sig")
        fieldIcon?.classList.add("text-gray-500")
    }

</script>

<div class="relative">
    <div bind:this={fieldIcon}
         class="absolute inset-y-0 start-0 flex items-center ps-3.5 pointer-events-none text-gray-400">
        <svg fill="currentColor" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" class="w-5 h-5">
            <slot />
        </svg>
    </div>
    <input type="text"
           class="bg-white border border-gray-300 text-gray-900 outline-red-sig text-base rounded-sm focus:ring-red-900
                           focus:border-red-sig focused-text-red-sig block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600
                           dark:placeholder-gray-400 dark:text-white dark:focus:ring-red-900 dark:focus:border-red-sig"
           on:focus={fieldFocus}
           on:blur={fieldBlur}
           bind:value="{inputValue}"
           placeholder="Username">
</div>