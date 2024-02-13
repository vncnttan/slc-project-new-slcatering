<script lang="ts">
    import {toast} from "@zerodevx/svelte-toast";

    interface VariantType {
        name: string;
        additional_price: number | null;
    }

    let variants : VariantType[] = [] ;

    let addNewVariant = () => {
        for (let i = 0; i < variants.length; i++) {
            if (variants[i].name === '' || variants[i].additional_price === null) {
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
        variants = [...variants, {
            name: '',
            additional_price: null
        }]
    }

</script>

<div class="w-full mx-auto flex flex-col gap-4">
    <div class="grid md:grid-cols-2 md:gap-6">
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
                       dark:focus:ring-blue-500 dark:focus:border-blue-500"
                       value="0" disabled readonly/>
            </div>
        </div>
    </div>
    {#each variants as variant}
        <div class="grid md:grid-cols-2 md:gap-6">
            <div class="relative z-0 w-full group">
                <input type="text" name="floating_variant_name" id="floating_variant_name"
                       class="block w-full p-2.5
                          text-sm text-gray-900 bg-transparent border-0 border-b-2
                          border-gray-300 appearance-none focus:outline-none
                          focus:ring-0 focus:border-red-600"
                       value="{variant.name}"
                       placeholder="Custom Variant (ex. Jumbo)"/>
            </div>

            <div class="flex flex-row place-items-end gap-2 relative z-0 w-full group">
                <div class="mb-2">
                    + Rp.
                </div>
                <div>
                    <input type="number" name="floating_additional_price" id="floating_variant_name"
                           value="{variant.additional_price}"
                           class="block p-2.5 w-40
                          text-sm text-gray-900 bg-transparent border-0 border-b-2
                          border-gray-300 appearance-none focus:outline-none
                          focus:ring-0 focus:border-red-600" placeholder="Additional Price"/>
                </div>
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