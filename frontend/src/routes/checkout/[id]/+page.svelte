<script lang="ts">
    import {page} from "$app/stores";
    import CheckoutLayout from "../../../components/checkout/CheckoutLayout.svelte";
    import {onMount} from "svelte";
    import {getCateringDetailsById} from "../../../scripts/datas/catering-mutations-and-queries";
    import CompleteOrderInfo from "../../../components/checkout/Step1OrderInfo/CompleteOrderInfo.svelte";
    import Payment from "../../../components/checkout/Step2Payment/Payment.svelte";
    import type {CateringType, OrderRequestType} from "../../../scripts/custom-type-declarations";

    let id = $page.params.id;
    let menu = {} as CateringType;

    let orderRequest = {
        variants: [{
            variant_id: "Reguler",
            variant_name: "Reguler",
            additional_price: 0,
            quantity: 1
        }]
    } as OrderRequestType

    onMount(async () => {
        menu = (await getCateringDetailsById(id)).data
        orderRequest.catering_id = menu.id
    })
    let currentStep = 1;

</script>

<CheckoutLayout currentStep={currentStep}>

    {#if currentStep === 1}
        <CompleteOrderInfo bind:currentStep menu={menu} bind:orderRequest/>
    {:else if currentStep === 2}
        <Payment menu={menu} selectedVariants={orderRequest.variants}/>
    {/if}
</CheckoutLayout>