<script lang="ts">
    export let menuTitle: string
    export let merchantStoreName: string
</script>

<div class="grid grid-cols-2">
    <div class="item-set">
        <div class="font-medium font-karla text-gray-500 ">Item Name</div>
        <div class="font-inter font-bold text-xl">{menuTitle}</div>
    </div>
    <div class="item-set">
        <div class="font-medium font-karla text-gray-500">Merchant</div>
        <div class="font-inter font-bold text-xl">{merchantStoreName}</div>
    </div>
</div>