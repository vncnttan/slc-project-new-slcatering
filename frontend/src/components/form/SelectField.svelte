<script lang="ts">
    import type {VariantType} from "../../scripts/helpers";

    export let variants = [] as VariantType[]
    export let selectedVariantId: string

</script>

<div class="relative border border-gray-300 grow">
    <select bind:value={selectedVariantId}
            class="bg-white text-gray-900 outline-red-sig text-base rounded-sm focus:ring-red-900
                               focus:border-red-sig focused-text-red-sig block w-full px-5 p-2.5 dark:bg-gray-700 dark:border-gray-600
                               dark:placeholder-gray-400 dark:text-white dark:focus:ring-red-900 dark:focus:border-red-sig">
        <option value="Reguler" >Reguler</option>
        {#each variants as v}
            <option value="{v.id}">{v.variant_name}   (+ Rp. {v.additional_price})</option>
        {/each}
    </select>

</div>

<style>
    select {
        border-right: 16px solid transparent;
    }
</style>