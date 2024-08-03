<script lang="ts">
    import SelectField from "../../form/SelectField.svelte";
    import type {VariantType} from "../../../scripts/helpers";
    import QuantitySelector from "../../form/QuantitySelector.svelte";
    import CreateVariant from "../../form/CreateVariant.svelte";
    import DeleteVariant from "../../form/DeleteVariant.svelte";

    export let variants = [] as VariantType[];

    let selectedVariants = [{
        variant_id: "-",
        quantity: 0
    }];
</script>

<div class="flex flex-col gap-2">
    <div class="flex flex-row justify-between place-items-end">
        <div class="font-medium font-karla text-gray-500">Variants</div>
        <CreateVariant />
    </div>
    {#each selectedVariants as sv}
        <div class="flex flex-row gap-2">
            <SelectField variants={variants}/>
            <QuantitySelector inputValue={sv.quantity}/>
            <DeleteVariant />
        </div>
    {/each}
</div>