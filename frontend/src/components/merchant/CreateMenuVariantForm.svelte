<script lang="ts">
    import {toast} from "@zerodevx/svelte-toast";
    import type {MenuInformationType} from "../../scripts/helpers";


    export let menuInformation: MenuInformationType;

    let addNewVariant = () => {
        for (let i = 0; i < menuInformation.variants.length; i++) {
            if (menuInformation.variants[i].name === '' || menuInformation.variants[i].additional_price === null) {
                toast.push("Fill variant before adding new ones", {
                    theme: {
                        "--toastBackground": "#B02000",
                        "--toastColor": "#fff",
                        "--toastProgressBackground": "#fff",
                        "--toastProgressColor": "#B02000"
                    }
                })
                return;
            }
        }
        menuInformation.variants = [...menuInformation.variants, {
            name: '',
            additional_price: null
        }]
    }

    let removeVariant = (index: number) => {
        menuInformation.variants = menuInformation.variants.filter((_, i) => i !== index);
    }

</script>

<div class="w-full mx-auto flex flex-col gap-8 md:gap-4">
    <div class="grid md:grid-cols-2 md:gap-6 gap-2">
        <div class="relative z-0 w-full group">
            <label for="floating_variant_name" class="block mb-1 text-sm font-medium text-gray-900 dark:text-white">Variant
                name</label>
            <input type="text" name="floating_variant_name" id="floating_variant_name"
                   class="bg-gray-100 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 cursor-not-allowed dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500"
                   value="Reguler" disabled readonly/>
        </div>

        <div class="flex flex-row place-items-end gap-2 relative z-0 w-full group">
            <div class="mb-2">
                + Rp.
            </div>
            <div>
                <label for="floating_additional_price"
                       class="block mb-1 text-sm font-medium text-gray-900 dark:text-white">Additional Price</label>
                <input type="number" name="floating_additional_price" id="floating_variant_name"
                       class="bg-gray-100 border border-gray-300 text-gray-900 text-sm rounded-lg
                       focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 cursor-not-allowed
                       dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400
                       dark:focus:ring-blue-500 dark:focus:border-blue-500" min="0"
                       value="0" disabled readonly/>
            </div>
        </div>
    </div>
    {#each menuInformation.variants as variant, index}
        <div class="grid md:grid-cols-2 md:gap-6 gap-2">
            <div class="relative z-0 w-full group">
                <input type="text" name="floating_variant_name" id="floating_variant_name"
                       class="block w-full p-2.5
                          text-sm text-gray-900 bg-transparent border-0 border-b-2
                          border-gray-300 appearance-none focus:outline-none
                          focus:ring-0 focus:border-red-600"
                       bind:value="{variant.name}"
                       placeholder="Custom Variant (ex. Jumbo)"/>
            </div>

            <div class="flex flex-row place-items-end gap-2 relative z-0 w-full group">
                <div class="mb-2">
                    + Rp.
                </div>
                <div>
                    <input type="number" name="floating_additional_price" id="floating_variant_name"
                           bind:value="{variant.additional_price}"
                           min="0"
                           class="block p-2.5 w-40
                          text-sm text-gray-900 bg-transparent border-0 border-b-2
                          border-gray-300 appearance-none focus:outline-none
                          focus:ring-0 focus:border-red-600" placeholder="Additional Price"/>
                </div>
                <button on:click={() => removeVariant(index)} type="button"
                        class="ms-4 flex place-items-center rounded-md bg-red-sig text-white p-2">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" class="w-5 h-5">
                        <path stroke-linecap="round" stroke-linejoin="round" d="m14.74 9-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 0 1-2.244 2.077H8.084a2.25 2.25 0 0 1-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 0 0-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 0 1 3.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 0 0-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 0 0-7.5 0" />
                    </svg>
                </button>
            </div>
        </div>
    {/each}
    <button on:click={addNewVariant} type="button" class="text-red-sig flex flex-row gap-2 text-sm place-items-center">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
             class="w-5 h-5">
            <path stroke-linecap="round" stroke-linejoin="round" d="M12 9v6m3-3H9m12 0a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z"/>
        </svg>
        Add new variant
    </button>
</div>