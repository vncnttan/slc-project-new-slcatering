<script>
    import ProgressItem from "./ProgressItem.svelte";
    import {tweened} from "svelte/motion";
    import {cubicOut} from "svelte/easing";

    let steps = [
        {stepNum: 1, description: "Complete Order Informations"},
        {stepNum: 2, description: "Payment Process"},
        {stepNum: 3, description: "Transaction Completed"},
    ]

    export let currentStep = 1;

    const progress = tweened(0, {
        duration: 1700,
        easing: cubicOut
    });

    $: progress.set((currentStep - 1) * 50);
</script>

<div class="w-full grid grid-cols-3 relative ">
    <div class="dash-container">
        <div class="dashed-line" style="width: 100%;"></div>
        <div class="completed-line" style="width: {$progress}%;"></div>
    </div>

    <ProgressItem item={steps[0]} active={currentStep >= 1} completed={currentStep > 1}/>
    <ProgressItem item={steps[1]} active={currentStep >= 2} completed={currentStep > 2}/>
    <ProgressItem item={steps[2]} active={currentStep >= 3} completed={currentStep > 3}/>
</div>


<style>
    .dash-container {
        position: absolute;
        transition: ease-in-out 1s;
        top: 29%;
        left: 0;
        right: 0;
        width: 65%;
        margin-left: auto;
        margin-right: auto;
    }

    .dashed-line {
        position: absolute;
        right: 0;
        height: 1px;
        border-top: 3px dashed #b9b9b9;
    }

    .completed-line {
        position: absolute;
        left: 0;
        height: 1px;
        border-top: 3px solid #FF461E;
    }
</style>