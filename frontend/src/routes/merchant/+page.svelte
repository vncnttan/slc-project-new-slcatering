<script lang="ts">
    import MerchantTransactionsTable from "../../components/merchant/MerchantTransactionsTable.svelte";
    import type {PageData} from "./$types";

    export let data: PageData;
</script>

<div class="flex flex-col !mt-10 p-8 gap-8 responsive-container">
    <div class="text-4xl text-black font-bold">
        History Transaction
    </div>
    <MerchantTransactionsTable access_token={data.user?.token}/>
</div>
