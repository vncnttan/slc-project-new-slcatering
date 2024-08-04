<script lang="ts">
    import CheckoutBasicInfo from "../CheckoutBasicInfo.svelte";
    import CheckoutPrice from "./CheckoutPrice.svelte";
    import type {
        CateringType,
        OrderRequestType,
    } from "../../../scripts/custom-type-declarations";
    export let menu: CateringType
    export let orderRequest: OrderRequestType
</script>
<div class="container lg:px-20 flex flex-col gap-8 py-8">
    <CheckoutBasicInfo menuTitle={menu.title} merchantStoreName={menu.created_by?.store_name} />
        <div class="item-set">
            <div class="font-medium font-karla text-gray-500 ">Notes</div>
            <div class="font-inter font-bold text-xl">{orderRequest.notes}</div>
        </div>
    <CheckoutPrice selectedVariants={orderRequest.variants} menu={menu}/>
</div>