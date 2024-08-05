<script lang="ts">
    import {showToast, TOAST_TYPE} from "../../../scripts/helpers";
    import TextField from "../../form/TextField.svelte";
    import OrderMultipleVariants from "./OrderMultipleVariants.svelte";
    import CheckoutBasicInfo from "../CheckoutBasicInfo.svelte";
    import type {CateringType, OrderRequestType} from "../../../scripts/custom-type-declarations";


    export let currentStep = 1
    export let menu: CateringType
    export let orderRequest: OrderRequestType;

    function progressToNextStep() {
        if (orderRequest.variants.length === 0) {
            showToast("Please select at least one variant", TOAST_TYPE.ERROR)
            return
        }

        if (!orderRequest.notes || orderRequest.notes === "") {
            orderRequest.notes = "-"
        }

        let newVariants = []
        const uniqueVariants = new Set()

        for (let i = 0; i < orderRequest.variants.length; i++) {
            const variant = orderRequest.variants[i]

            if (variant.quantity == 0) {
                continue;
            }

            if (uniqueVariants.has(variant.variant_id)) {
                newVariants.forEach((v) => {
                    if (v.variant_id === variant.variant_id) {
                        v.quantity += variant.quantity
                    }
                })
                continue
            }

            uniqueVariants.add(variant.variant_id)
            newVariants.push(variant)
        }

        orderRequest.variants = newVariants
        if (orderRequest.variants.length === 0) {
            showToast("Please select at least one variant with non-zero quantity", TOAST_TYPE.ERROR)
            return
        }
        currentStep += 1
    }

</script>

<div class="information-container">
    <!--    TODO: Responsive Checkout -->
    <!--    Pertanyaan: Disini gabisa liat harga? -->
    <div class="w-full h-full">
        <!--        Image Section-->
        <img src={menu.imageLink} alt="Food" class="w-full h-[50vh] rounded-xl object-contain lg:object-cover"/>
    </div>
    <div class="w-full h-full py-4 flex flex-col gap-12 text-lg">
        <CheckoutBasicInfo menuTitle={menu.title} merchantStoreName={menu.created_by?.store_name}/>
        <OrderMultipleVariants variants={menu.catering_variants} bind:selectedVariants={orderRequest.variants}/>
        <div class="flex flex-col gap-1">
            <div class="font-medium font-karla text-gray-500">Notes</div>
            <TextField bind:inputValue={orderRequest.notes} placeholder="Insert Notes (ex. Jangan pedas)">
                <path stroke-linecap="round" stroke-linejoin="round"
                      d="M8.625 12a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm0 0H8.25m4.125 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm0 0H12m4.125 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm0 0h-.375M21 12c0 4.556-4.03 8.25-9 8.25a9.764 9.764 0 0 1-2.555-.337A5.972 5.972 0 0 1 5.41 20.97a5.969 5.969 0 0 1-.474-.065 4.48 4.48 0 0 0 .978-2.025c.09-.457-.133-.901-.467-1.226C3.93 16.178 3 14.189 3 12c0-4.556 4.03-8.25 9-8.25s9 3.694 9 8.25Z"/>
            </TextField>
        </div>
        <div class="grid grid-cols-2 gap-2">
            <a href="/" class="text-center py-3 bg-gray-400 hover:bg-gray-500 rounded-lg text-white text-xl">Back</a>
            <button class="py-3 bg-orange-sig hovered-bg-orange-sig rounded-lg text-white text-xl" on:click={progressToNextStep}> Continue</button>
        </div>
    </div>
</div>

<style>
    .information-container {
        display: grid;
        grid-template-columns: 4fr 5fr;
        gap: 4rem;
    }
</style>