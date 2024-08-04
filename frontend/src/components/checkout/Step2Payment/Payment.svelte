<script lang="ts">
    import CheckoutSummary from "./CheckoutSummary.svelte";
    import type {CateringType, OrderRequestVariantDetailType} from "../../../scripts/custom-type-declarations";

    export let menu: CateringType
    export let selectedVariants: OrderRequestVariantDetailType[]
</script>

<div class="page-container">
    <div class="border-box-container">
        <!--        Summary -->
        <CheckoutSummary menu={menu} selectedVariants={selectedVariants}/>
    </div>
    <div class="border-box-container">
        <!--        QR Code -->
        s
    </div>
</div>

<style>
    .page-container {
        display: grid;
        grid-template-columns: 5fr 3fr;
        gap: 3rem;
    }

    .border-box-container {
        border: 1px solid #D7D7D7;
        padding: 1rem;
        border-radius: 0.5rem;
    }
</style>