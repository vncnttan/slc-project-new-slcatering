<script lang="ts">

    import type {CateringType, OrderRequestVariantDetailType} from "../../../scripts/custom-type-declarations";
    import {formatPrice} from "../../../scripts/helpers";

    export let selectedVariants: OrderRequestVariantDetailType[];
    export let menu: CateringType;

    console.log(selectedVariants)
</script>

<div class="flex flex-col">
    {#each selectedVariants as v}
        <div class="flex flex-row justify-between text-lg text-gray-600">
            <div class="flex flex-row">
                <div class="w-24">
                    {v.quantity} pc(s)
                </div>
                <div>
                    {v.variant_name}
                </div>
            </div>
            <div class="text-black font-bold">
                {formatPrice((menu.price + v.additional_price) * v.quantity)}
            </div>
        </div>
    {/each}

<!--    Grand Total Section-->
</div>