<script lang="ts">

    import type {OrderRequestVariantDetailType, VariantType} from "../../scripts/custom-type-declarations";
    import {formatPrice} from "../../scripts/helpers.js";

    export let variants = [] as VariantType[]
    export let selectedVariant: OrderRequestVariantDetailType

</script>

<div class="relative border border-gray-300 grow">
    <select bind:value={selectedVariant.variant_id}
            on:change={()=>{
                const selected = variants.find(v => v.id === selectedVariant.variant_id);
                if (selected) {
                    selectedVariant.variant_name = selected.variant_name;
                    selectedVariant.additional_price = selected.additional_price;
                } else if (selectedVariant.variant_id === "Reguler") {
                    selectedVariant.variant_name = "Reguler";
                    selectedVariant.additional_price = 0;
                }

            }}
            class="bg-white text-gray-900 outline-red-sig text-base rounded-sm focus:ring-red-900
                               focus:border-red-sig focused-text-red-sig block w-full px-5 p-2.5 dark:bg-gray-700 dark:border-gray-600
                               dark:placeholder-gray-400 dark:text-white dark:focus:ring-red-900 dark:focus:border-red-sig">
        <option value="Reguler" >Reguler</option>
        {#each variants as v}
            <option value="{v.id}">{v.variant_name}   (+ {formatPrice(v.additional_price)})</option>
        {/each}
    </select>

</div>

<style>
    select {
        border-right: 16px solid transparent;
    }
</style>