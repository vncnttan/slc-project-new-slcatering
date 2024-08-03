<script lang="ts">
    export let selectedVariants: {variant_id: string, quantity: number}[]

    function addVariant() {
        selectedVariants = [...selectedVariants, {
            variant_id: "Reguler",
            quantity: 1
        }];
    }
</script>

<button on:click={addVariant} class="flex justify-center place-items-center flex-row gap-1
    text-orange-sig hover:bg-gray-200 hover:cursor-pointer rounded-md px-3 p-1">
    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor"
    class="w-4 h-4 mb-0.5">
        <path stroke-linecap="round" stroke-linejoin="round" d="M12 4.5v15m7.5-7.5h-15"/>
    </svg>
    Add Variant
</button>