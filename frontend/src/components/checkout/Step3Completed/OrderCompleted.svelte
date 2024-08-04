<script lang="ts">
    import slcatering_logo from "$lib/assets/slcatering_logo.png"
</script>

<div class="flex flex-col gap-12 w-full place-items-center">
    <div class="flex flex-col w-full place-items-center font-karla gap-8">
        <div class="flex flex-col gap-2 place-items-center">
            <img src={slcatering_logo} alt="SLCatering Logo" class="w-24"/>
            <div class="text-gray-600">Order Code: ASDF2342DSFSE</div>
        </div>
        <iframe src="https://lottie.host/embed/01da3271-fc39-4055-9977-19d3fa8acf9a/GZritMBiEU.json"
                title="Checkmark animation"></iframe>
        <div class="flex flex-col gap-2 place-items-center">
            <div class="text-3xl font-bold">Order Completed!</div>
            <div class="text-base text-gray-500">Your order will arrived on [Insert Response Date here]</div>
        </div>
    </div>
    <div class="grid grid-cols-2 gap-2 w-[100%] lg:w-[50%] ">
        <a href="/" class="text-center py-3 bg-gray-400 hover:bg-gray-500 rounded-lg text-white text-xl">Order
            Details</a>
        <a href="/history" class="text-center py-3 bg-orange-sig hovered-bg-orange-sig rounded-lg text-white text-xl">Transaction
            History</a>
    </div>
</div>
