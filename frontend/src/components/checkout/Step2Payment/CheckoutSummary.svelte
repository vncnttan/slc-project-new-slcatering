<script lang="ts">
    import CheckoutBasicInfo from "../CheckoutBasicInfo.svelte";
    import CheckoutPrice from "./CheckoutPrice.svelte";
    import type {CateringType, OrderRequestVariantDetailType} from "../../../scripts/custom-type-declarations";
    export let menu: CateringType
    export let selectedVariants: OrderRequestVariantDetailType[]

</script>
<div class="container lg:px-20 flex flex-col gap-8 py-8">
    <CheckoutBasicInfo menuTitle={menu.title} merchantStoreName={menu.created_by?.store_name} />
    <CheckoutPrice selectedVariants={selectedVariants} menu={menu}/>
</div>