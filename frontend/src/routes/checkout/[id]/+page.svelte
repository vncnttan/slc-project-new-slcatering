<script lang="ts">
    import {page} from "$app/stores";
    import CheckoutLayout from "../../../components/checkout/CheckoutLayout.svelte";
    import type {CateringType} from "../../../scripts/helpers";
    import {onMount} from "svelte";
    import {getCateringDetailsById} from "../../../scripts/datas/catering-mutations-and-queries";
    import Checkout1CompleteOrderInformation
        from "../../../components/checkout/Step1OrderInfo/CompleteOrderInfo.svelte";

    let id = $page.params.id;
    let menu = {} as CateringType;

    onMount(async () => {
        menu = (await getCateringDetailsById(id)).data
    })
    let currentStep = 1;

</script>

<CheckoutLayout currentStep={currentStep}>
    <!--{#if currentStep === 1}-->
        <Checkout1CompleteOrderInformation bind:currentStep menu={menu}/>
    <!--{/if}-->
</CheckoutLayout>