<script lang="ts">
    import type {CateringType, SelectedType} from "../../../scripts/helpers";

    export let selectedVariants: SelectedType[];
    export let menu: CateringType;

    console.log(selectedVariants)
</script>

<div class="flex flex-col">
    {#each selectedVariants as v}
        <div class="flex flex-row justify-between text-lg">
            <div>
                {v.quantity}x {v.variant_name}
            </div>
            <div class="text-black font-bold text-xl">
                Rp. {menu.price * v.quantity}
            </div>
        </div>
    {/each}
</div>