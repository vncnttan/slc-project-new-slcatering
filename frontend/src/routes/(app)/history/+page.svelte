<script lang="ts">
    import TransactionHistoryTable from "../../../components/transaction/TransactionHistoryTable.svelte";
    import type {PageData} from "./$types";

    export let data: PageData;
</script>

<div class="!my-8 responsive-container flex flex-col gap-8">
    <div class="text-2xl font-inter font-semibold">
        Transaction History
    </div>

    <TransactionHistoryTable access_token={data.user?.token} />
</div>