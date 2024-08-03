<script lang="ts">
    import CheckoutBasicInfo from "../CheckoutBasicInfo.svelte";
    import type {CateringType} from "../../../scripts/helpers";
    import CheckoutPrice from "./CheckoutPrice.svelte";
    export let menu: CateringType

</script>
<div class="container lg:px-20 flex flex-col gap-8 py-8">
    <CheckoutBasicInfo menuTitle={menu.title} merchantStoreName={menu.created_by?.store_name} />
    <CheckoutPrice />
</div>