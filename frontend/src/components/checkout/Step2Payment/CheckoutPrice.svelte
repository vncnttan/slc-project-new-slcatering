<script lang="ts">

    import type {CateringType, OrderRequestVariantDetailType} from "../../../scripts/custom-type-declarations";
    import {formatPrice} from "../../../scripts/helpers";

    export let selectedVariants: OrderRequestVariantDetailType[];
    export let menu: CateringType;

    let totalPrice = 0
    for (let i = 0; i < selectedVariants.length; i++) {
        totalPrice += (menu.price + selectedVariants[i].additional_price) * selectedVariants[i].quantity
    }
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
    <div class="dashed-line"></div>

    <div class="flex flex-row justify-between text-2xl font-bold">
        <div class="flex flex-row">
            Grand Total
        </div>
        <div>
            {formatPrice(totalPrice)}
        </div>
    </div>
</div>

<style>
    .dashed-line {
        border-top: 1px dashed #b9b9b9;
        width: 100%;
        margin-top: 1rem;
        margin-bottom: 1rem;
    }
</style>