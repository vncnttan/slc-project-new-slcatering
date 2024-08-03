<script lang="ts">
    import {page} from "$app/stores";
    import CheckoutLayout from "../../../components/checkout/CheckoutLayout.svelte";
    import type {CateringType} from "../../../scripts/helpers";
    import {onMount} from "svelte";
    import {getCateringDetailsById} from "../../../scripts/datas/catering-mutations-and-queries";
    import CompleteOrderInfo from "../../../components/checkout/Step1OrderInfo/CompleteOrderInfo.svelte";
    import Payment from "../../../components/checkout/Step2Payment/Payment.svelte";

    let id = $page.params.id;
    let menu = {} as CateringType;
    let selectedVariants = [{
        variant_id: "Reguler",
        quantity: 1
    }]
    onMount(async () => {
        menu = (await getCateringDetailsById(id)).data
    })
    let currentStep = 1;

</script>

<CheckoutLayout currentStep={currentStep}>

    {#if currentStep === 1}
        <CompleteOrderInfo bind:currentStep menu={menu} bind:selectedVariants/>
    {:else if currentStep === 2}
        <Payment menu={menu} />
    {/if}
</CheckoutLayout>